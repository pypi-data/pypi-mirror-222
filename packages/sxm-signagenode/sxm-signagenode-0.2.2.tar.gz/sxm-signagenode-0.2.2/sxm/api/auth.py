

from twisted.internet.defer import succeed
from twisted.internet.defer import inlineCallbacks
from ebs.linuxnode.modapi.engine import ModularHttpApiEngine
from ebs.linuxnode.modapi.engine import PrimaryAuthenticationFailure
from ebs.linuxnode.modapi.engine import ConnectionRequirementsNotReady


class SXMApiEngineAuth(ModularHttpApiEngine):
    _prefix = "sxm"
    _api_baseurl = 'config:sxm_api_url'
    _api_headers = {'Content-Type': 'application/json',
                    'Accept': 'application/json'}
    _auth_url = 'config:sxm_auth_url'
    _auth_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    _auth_password_required = True

    def __init__(self, *args, **kwargs):
        super(SXMApiEngineAuth, self).__init__(*args, **kwargs)

    """ Proxy to Core Engine """

    @property
    def id(self):
        return self._actual.id

    @property
    def appname(self):
        return self._actual.appname

    """ Common API Utils """

    @inlineCallbacks
    def _api_basic_params(self):
        token = yield self.api_token
        return {
            'id': self.id.lower(),
            '_token': token,
        }

    """ API Token Management """
    @inlineCallbacks
    def _api_generate_token(self):
        url = self.auth_url
        headers = self._auth_headers
        password = yield self.api_password
        if not password and self._auth_password_required:
            raise ConnectionRequirementsNotReady()
        data = dict(
            grant_type='password',
            username=f'{self.appname}-{self.id.lower()}',
            password=password,
            audience=self.config.sxm_auth_audience,
            client_id=self.config.sxm_auth_client_id,
            client_secret=self.config.sxm_auth_client_secret
        )
        self.log.info(f"Attempting to obtain API token from {url}")

        try:
            response = yield self.http_post(url, data=data, headers=headers)
            content = yield response.json()
            self.api_token = content['access_token']
            return content['access_token']
        except Exception as e:
            raise PrimaryAuthenticationFailure(e)

    def _api_get_password(self):
        return self.api_engine_reconnect()

    @property
    def api_token(self):
        if not self.config.sxm_api_token:
            return self._api_generate_token()
        else:
            return succeed(self.config.sxm_api_token)

    @api_token.setter
    def api_token(self, value):
        self.log.info("Got a new API Token.")
        self.config.sxm_api_token = value

    def api_token_reset(self):
        self.log.warn("Clearing API token.")
        self.config.sxm_api_token = None

    @property
    def api_password(self):
        if not self.config.sxm_api_password:
            return self._api_get_password()
        return self.config.sxm_api_password

    @api_password.setter
    def api_password(self, value):
        self.config.sxm_api_password = value

    def api_password_reset(self):
        self.log.warn("Clearing API password.")
        self.config.sxm_api_password = None

    @property
    def api_credentials_available(self):
        if self.config.sxm_api_password:
            return True
        return False
