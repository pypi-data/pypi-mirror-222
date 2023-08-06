

from twisted.internet.task import LoopingCall
from twisted.internet.defer import inlineCallbacks

from .announce import SXMApiEngineAnnounce


class SXMApiEngineCore(SXMApiEngineAnnounce):
    _api_announce = 'api_announce'
    _api_probe = '_api_ping'
    _api_ep_ping = 'iot/ping'

    def __init__(self, *args, **kwargs):
        super(SXMApiEngineCore, self).__init__(*args, **kwargs)
        self._api_ping_task = None

    """ Ping API """

    def _api_ping_handler(self, response):
        self.log.info("API Ping successful")

    @inlineCallbacks
    def _api_ping_request_builder(self):
        rv = yield self._api_basic_params()
        status = yield self._actual.sysinfo.status.render()
        rv['status'] = status
        return rv

    def _api_ping(self, *_):
        self.log.debug("Executing API Ping")
        return self._api_execute(
            self._api_ep_ping,
            self._api_ping_request_builder,
            self._api_ping_handler
        )

    @property
    def api_ping_task(self):
        if self._api_ping_task is None:
            self._api_ping_task = LoopingCall(self._api_ping)
        return self._api_ping_task
