

import os
from six.moves.urllib.parse import urlparse
from twisted.internet.task import LoopingCall
from twisted.internet.defer import inlineCallbacks
from twisted.internet.defer import DeferredList
from ebs.linuxnode.core.constants import ASSET
from ebs.linuxnode.core.background import BackgroundSpec

from .core import SXMApiEngineCore


class SXMApiEngineSettings(SXMApiEngineCore):
    _api_ep_settings = 'iot/settings'

    def __init__(self, *args, **kwargs):
        super(SXMApiEngineSettings, self).__init__(*args, **kwargs)
        self._api_settings_task = None

    """ Device Settings API """
    def _display_settings_handler(self, settings):
        self.log.info("Got orientation settings from the server : "
                      "{portrait} {flip}",
                      portrait=settings['portrait'], flip=settings['flip'])
        old_p = self.config.portrait
        self.config.portrait = settings['portrait']
        old_f = self.config.flip
        self.config.flip = settings['flip']
        if old_p != self.config.portrait or old_f != self.config.flip:
            self._actual.orientation_update()

    def _local_usb_settings_handler(self, settings):
        self.log.info("Got local USB setting from the server : "
                      "{allowed}", allowed=settings['allow'])
        if settings['allow']:
            self.config.exim_local_background = True
        else:
            self.config.exim_local_background = False

    def _get_content_uri(self, content):
        formats = content['formats']
        # TODO Select Format Here
        for fmt in formats:
            if fmt['format_class'] == 'file_media':
                selected_format = fmt
                self.log.info(f"Using format {fmt['uri']}")
                break
        else:
            self.log.error("Media content has no usable formats. Not using.")
            return
        return selected_format['uri'], selected_format['duration']

    def _prepare_content(self, uri):
        self.log.info(f"Preparing background from {uri}")
        fname = os.path.basename(urlparse(uri).path)
        self._actual.resource_manager.insert(fname, url=uri, rtype=ASSET)
        r = self._actual.resource_manager.get(fname)
        d = self._actual.resource_manager.prefetch(r)
        return r, d

    def _process_sequence(self, sequence):
        default_duration = sequence['default_duration']
        seq = {}
        deferreds = []
        for content_spec in sequence['contents']:
            uri, content_duration = self._get_content_uri(content_spec['content'])
            r, d = self._prepare_content(uri)
            spec_duration = content_spec['duration']
            duration = default_duration
            if spec_duration:
                duration = spec_duration
            elif content_duration:
                duration = content_duration
            if duration < 0:
                duration = -1 * (duration * (default_duration + 1)) - 1
            seq[content_spec['position']] = BackgroundSpec(r.cache_path, duration=duration)
            deferreds.append(d)
        d = DeferredList(deferreds)
        seq = [seq[x] for x in sorted(seq.keys())]
        self.log.info(f"Setting background sequence with contents : {seq}")
        return seq, d

    def _content_settings_handler(self, settings):
        if 'default' in settings.keys():
            self.log.info("Got default content settings from the server : "
                          "{default_content}", default_content=settings['default'])
            default = settings['default']
            if not default:
                self._actual.background_set(None)
                return
            if default['content_type'] == 'structured':
                ldefault = "structured:{0}".format(default['path'])
                self._actual.background_set(ldefault)
            elif default['content_type'] == 'media':
                uri, _ = self._get_content_uri(default)
                r, d = self._prepare_content(uri)
                d.addCallback(lambda _: self._actual.background_set(r.cache_path))
                d.addCallback(lambda _: self._actual.background_sequence_set([]))
            elif default['content_type'] == 'sequence':
                seq, d = self._process_sequence(default)
                d.addCallback(lambda _: self._actual.background_sequence_set(seq))
                pass
            else:
                self.log.error(f"content_type {default['content_type']} not supported. Not setting.")

    def _api_settings_handler(self, response):
        self.log.info("Got device settings from the API")
        if 'display' in response.keys():
            self._display_settings_handler(response['display'])
        if 'local_usb' in response.keys():
            self._local_usb_settings_handler(response['local_usb'])
        if 'content' in response.keys():
            self._content_settings_handler(response['content'])

    @inlineCallbacks
    def _api_settings_request_builder(self):
        rv = yield self._api_basic_params()
        rv['appname'] = self._actual.appname
        return rv

    def _api_settings(self, *_):
        self.log.debug("Requesting Device Settings from the API")
        return self._api_execute(
            self._api_ep_settings,
            self._api_settings_request_builder,
            self._api_settings_handler
        )

    @property
    def api_settings_task(self):
        if self._api_settings_task is None:
            self._api_settings_task = LoopingCall(self._api_settings)
        return self._api_settings_task
