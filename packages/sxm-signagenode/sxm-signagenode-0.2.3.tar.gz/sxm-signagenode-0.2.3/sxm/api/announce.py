


from twisted.internet.defer import succeed
from ebs.linuxnode.modapi.engine import ServerReportsNotReady
from ebs.linuxnode.modapi.engine import ConnectionRequirementsNotReady
from .auth import SXMApiEngineAuth


class SXMApiEngineAnnounce(SXMApiEngineAuth):
    _api_ep_announce = 'iot/announce'

    def __init__(self, *args, **kwargs):
        super(SXMApiEngineAnnounce, self).__init__(*args, **kwargs)

    """ API Endpoint Implementations """

    def _api_annouce_precheck(self):
        return self._api_announce_precheck_succeeded

    def _api_announce_builder(self):
        return succeed({
            'id': self.id.lower(),
            'appname': self.appname,
            'have_credentials': self.api_credentials_available
        })

    def _api_announce_handler(self, response):
        if 'password' in response.keys() and response['password']:
            self.log.info(f"Got password {response['password']}")
            self.api_password = response['password']
        if response['status'] == "NEW":
            if self.api_password:
                self.api_password_reset()
        if response['status'] == "ACTIVE":
            if self._auth_password_required and not self.api_password:
                # We need a password. The server will only give one
                # to us after a manual reset. We've already signalled
                # this requirement, so for now we just continue on the
                # reconnect polling cycle.
                raise ConnectionRequirementsNotReady()
        else:
            raise ServerReportsNotReady()

    def api_announce(self, *_):
        return self._api_execute(
            self._api_ep_announce,
            self._api_announce_builder,
            self._api_announce_handler,
        )
