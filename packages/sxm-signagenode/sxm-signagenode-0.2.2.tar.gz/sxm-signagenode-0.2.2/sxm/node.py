

from kivy_garden.ebs.core.colors import GuiPalette
from ebs.linuxnode.core.config import ElementSpec, ItemSpec

from ebs.signagenode.node import SignageNode
from ebs.linuxnode.modapi.manager import ModularApiEngineManagerMixin
from ebs.linuxnode.gui.kivy.modapi.mixin import ModularApiEngineManagerGuiMixin
from streamwatcher.mixin import StreamWatcherMixin

from .api import SXMApiEngine


class StarXMediaNode(ModularApiEngineManagerGuiMixin,
                     ModularApiEngineManagerMixin,
                     StreamWatcherMixin,
                     SignageNode):
    _palette = GuiPalette(
        background=(0x00 / 255, 0x00 / 255, 0x00 / 255),
        foreground=(0xff / 255, 0xff / 255, 0xff / 255),
        color_1=(0x6d / 255., 0xc0 / 255., 0x66 / 255., 1),
        color_2=(0xff / 255., 0x00 / 255., 0x00 / 255., 1)
    )

    _gui_supports_overlay_mode = True
    # _default_sxm_api_url = 'https://localhost:8039/v1'
    _default_sxm_api_url = 'https://edge.starxmedia.in/v1'
    _default_sxm_auth_url = 'https://starxmedia.eu.auth0.com/oauth/token'
    _default_auth_audience = 'https://edge.starxmedia.in/v1'
    _default_auth_client_id = 'AyWYobSWwpYKUVKusantgt8Qw7RARwO2'
    _default_auth_client_secret = 'jRuJKTG6MI7ltjEaBI26WfQaqgr5hp0vQZ580ybJxoY7-6azPhbxaqA62s5pVzBR'

    def sysinfo_install(self):
        super(StarXMediaNode, self).sysinfo_install()
        self.sysinfo.app.versions.register_package('sxm-signagenode')

    def install(self):
        super(StarXMediaNode, self).install()

        _elements = {
            'sxm_api_url': ElementSpec('sxm', 'url',
                                       ItemSpec(str, fallback=self._default_sxm_api_url)),
            'sxm_api_password': ElementSpec('sxm', 'password',
                                            ItemSpec(str, read_only=False, fallback=None, masked=True)),
            'sxm_api_token': ElementSpec('sxm', 'token',
                                         ItemSpec(str, read_only=False, fallback=None, masked=True)),
            'sxm_auth_url': ElementSpec('sxm', 'auth_url',
                                        ItemSpec(str, fallback=self._default_sxm_auth_url)),
            'sxm_auth_audience': ElementSpec('sxm', 'audience',
                                             ItemSpec(str, fallback=self._default_auth_audience)),
            'sxm_auth_client_id': ElementSpec('sxm', 'client_id',
                                              ItemSpec(str, fallback=self._default_auth_client_id, masked=True)),
            'sxm_auth_client_secret': ElementSpec('sxm', 'client_secret',
                                                  ItemSpec(str, fallback=self._default_auth_client_secret, masked=True))
        }

        for name, spec in _elements.items():
            self.config.register_element(name, spec)

        sxm_api_engine = self.modapi_engine('sxm')
        if not sxm_api_engine:
            self.log.info("Installing StarXMedia Tendril Api Engine")
            sxm_api_engine = SXMApiEngine(self)
            self.modapi_install(sxm_api_engine)

        sxm_api_engine.install_task('api_ping_task', 60)
        sxm_api_engine.install_task('api_settings_task', 600)
        # sxm_api_engine.install_task('api_media_task', 120)
        # sxm_api_engine.install_task('api_text_task', 120)
        # sxm_api_engine.install_task('api_gallery_task', 1800)
        self._success_api_engine = sxm_api_engine
