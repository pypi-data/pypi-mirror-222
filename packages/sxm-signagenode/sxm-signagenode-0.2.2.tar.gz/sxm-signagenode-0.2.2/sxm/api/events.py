
from functools import partial
from twisted.internet.defer import succeed
from twisted.internet.defer import DeferredList

from .core import SXMApiEngineCore


class SXMApiEngineEvents(SXMApiEngineCore):
    def __init__(self, *args, **kwargs):
        super(SXMApiEngineEvents, self).__init__(*args, **kwargs)

    """ Retrieve Event Queue Items API """
    def _api_get_events_handler(self, response, event_handler, ack_func,
                                cancellation_handler, cancellation_ack_func):
        items = response.get('data', [])
        acks = []
        self.log.info("Got {n} events from server", n=len(items))
        for item in items:
            result = event_handler(item)
            if result:
                acks.append(result)

        events_d = ack_func(acks)

        cancellations = response.get('cancelled', [])
        cancellation_acks = []
        self.log.info("Got {n} cancellations from server", n=len(cancellations))
        for item in cancellations:
            result = cancellation_handler(item)
            if result:
                cancellation_acks.append(result)

        cancellation_d = cancellation_ack_func(cancellation_acks)

        return DeferredList([events_d, cancellation_d])

    def _api_get_events(self, events_endpoint, events_handler):
        return self._api_execute(
            events_endpoint,
            self._api_basic_params,
            events_handler
        )

    """ Items API Primitives """
    def _api_items_params(self, token, items=None):
        params = self._api_basic_params(token)
        params['ads'] = ','.join([str(x) for x in items])
        return params

    def _api_items_request(self, items, endpoint, handler):
        if not items:
            return succeed(True)
        deferred = self._api_execute(
            endpoint,
            partial(self._api_items_params, items=items),
            partial(handler, items=items)
        )
        return deferred

    """ Ack Events Queue Items API """
    def _api_events_ack_response_handler(self, response, items=None):
        # assert response['message'] == "Ads marked success successfully"
        self.log.debug(
            "Server responded to ack message for items {items}.",
            items=items
        )

    def _api_events_ack(self, items, ack_endpoint):
        if items:
            self.log.debug("Sending Ack for items : {0}".format(items))
        return self._api_items_request(
            items, ack_endpoint,
            self._api_events_ack_response_handler
        )

    def _api_cancellation_ack_response_handler(self, response, items=None):
        self.log.debug(
            "Server responded to ack message for items {items}.",
            items=items
        )

    def _api_cancellation_ack(self, items, cancellation_ack_endpoint):
        if items:
            self.log.debug("Sending Ack for cancellations : {0}".format(items))
        return self._api_items_request(
            items, cancellation_ack_endpoint,
            self._api_cancellation_ack_response_handler
        )

    """ Report Success Media Queue Items API """
    def _api_events_success_response_handler(self, response, items=None):
        # assert response['message'] == "Ads marked success successfully"
        self.log.debug(
            "Server responded to success message for items {items}.",
            items=items
        )

    def _api_events_success(self, items, success_endpoint):
        if items:
            self.log.debug("Sending Success for items : {0}".format(items))
        d = self._api_items_request(
            items, success_endpoint,
            self._api_events_success_response_handler
        )

        def _enqueue_retry(failure):
            print("Attempting to enqueue : {0}, {1}"
                  "".format(items, success_endpoint))
            self._api_queue.enqueue_action('_api_events_success',
                                           items, success_endpoint)
            return failure
        d.addErrback(_enqueue_retry)
        return d
