

from twisted.internet.task import LoopingCall
from ebs.linuxnode.core.constants import TEXT
from .events import SXMApiEngineEvents


class SXMApiEngineText(SXMApiEngineEvents):
    _api_ep_text = 'iot/load-text-ads'
    _api_ep_text_ack = 'iot/text-ads-received'
    _api_ep_text_cancellation_ack = 'iot/text-cancel-ads-received'
    _api_ep_text_success = 'iot/text-ads-success'

    def __init__(self, *args, **kwargs):
        super(SXMApiEngineText, self).__init__(*args, **kwargs)
        self._api_text_task = None

    """ Retrieve Text Queue Items API """
    def _api_handle_text_item(self, item):
        # self.log.debug("Got text event from the server : \n{item}", item=item)
        text = item['ads_text']
        self._actual.event_manager(TEXT).insert(
            item['id'], etype=TEXT, duration=item['duration'],
            start_time=item['start'], resource=text
        )
        return item['id']

    def _api_handle_text_item_cancellation(self, item):
        success = self._actual.event_manager(TEXT).remove(item['id'])
        if success:
            return item['id']
        else:
            return None

    def _api_get_text_handler(self, response):
        return self._api_get_events_handler(response,
                                            self._api_handle_text_item,
                                            self.api_text_ack,
                                            self._api_handle_text_item_cancellation,
                                            self.api_text_cancellation_ack)

    def api_get_text(self):
        self.log.debug("Checking for new text events")
        return self._api_get_events(self._api_ep_text,
                                    self._api_get_text_handler)

    """ Ack Text Queue Items API """
    def api_text_ack(self, items):
        return self._api_events_ack(items, self._api_ep_text_ack)

    def api_text_cancellation_ack(self, items):
        return self._api_cancellation_ack(items, self._api_ep_text_cancellation_ack)

    """ Report Success Text Queue Items API """
    def api_text_success(self, items):
        d = self._api_events_success(items, self._api_ep_text_success)
        return d

    """ API Media Queue Management Task """
    @property
    def api_text_task(self):
        if self._api_text_task is None:
            self._api_text_task = LoopingCall(self.api_get_text)
        return self._api_text_task
