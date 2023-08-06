

import os
from six.moves.urllib.parse import urlparse
from twisted.internet.task import LoopingCall

from ebs.linuxnode.core.constants import WEBRESOURCE
from .events import SXMApiEngineEvents


class SXMApiEngineMedia(SXMApiEngineEvents):
    _api_ep_media = 'iot/load-video-ads'
    _api_ep_media_ack = 'iot/video-ads-received'
    _api_ep_media_cancellation_ack = 'iot/video-cancel-ads-received'
    _api_ep_media_success = 'iot/video-ads-success'

    def __init__(self, *args, **kwargs):
        super(SXMApiEngineMedia, self).__init__(*args, **kwargs)
        self._api_media_task = None

    """ Retrieve Media Queue Items API """
    def _api_handle_media_item(self, item):
        # self.log.debug("Got media event from the server : \n{item}", item=item)
        url = item['path']
        fname = os.path.basename(urlparse(url).path)
        self._actual.resource_manager.insert(fname, url=url)
        self._actual.event_manager(WEBRESOURCE).insert(
            item['id'], etype=WEBRESOURCE, duration=item['duration'],
            start_time=item['start'], resource=fname
        )
        return item['id']

    def _api_handle_media_item_cancellation(self, item):
        success = self._actual.event_manager(WEBRESOURCE).remove(item['id'])
        if success:
            return item['id']
        else:
            return None

    def _api_get_media_handler(self, response):
        return self._api_get_events_handler(response,
                                            self._api_handle_media_item,
                                            self.api_media_ack,
                                            self._api_handle_media_item_cancellation,
                                            self.api_media_cancellation_ack)

    def api_get_media(self):
        self.log.debug("Checking for new media events")
        return self._api_get_events(self._api_ep_media,
                                    self._api_get_media_handler)

    """ Ack Media Queue Items API """
    def api_media_ack(self, items):
        return self._api_events_ack(items, self._api_ep_media_ack)

    def api_media_cancellation_ack(self, items):
        return self._api_cancellation_ack(items, self._api_ep_media_cancellation_ack)

    """ Report Success Media Queue Items API """
    def api_media_success(self, items):
        return self._api_events_success(items, self._api_ep_media_success)

    """ API Media Queue Management Task """
    @property
    def api_media_task(self):
        if self._api_media_task is None:
            self._api_media_task = LoopingCall(self.api_get_media)
        return self._api_media_task
