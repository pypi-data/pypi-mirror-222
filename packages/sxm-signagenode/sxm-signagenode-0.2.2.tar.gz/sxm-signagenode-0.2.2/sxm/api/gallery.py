

import os
from six.moves.urllib.parse import urlparse
from twisted.internet.task import LoopingCall

from .core import SXMApiEngineCore


class SXMApiEngineGallery(SXMApiEngineCore):
    _api_ep_gallery_load = 'iot/load-device-gallery'

    def __init__(self, *args, **kwargs):
        super(SXMApiEngineGallery, self).__init__(*args, **kwargs)
        self._api_gallery_task = None

    def _api_gallery_load_handler(self, response):
        items = []
        for item in response['data']:
            url = item['path']
            fname = os.path.basename(urlparse(url).path)
            self._actual.resource_manager.insert(fname, url=url)
            items.append((fname, None))
        self._actual.gallery_load(items)

    def api_gallery_load(self):
        return self._api_execute(
            self._api_ep_gallery_load,
            self._api_basic_params,
            self._api_gallery_load_handler
        )

    @property
    def api_gallery_task(self):
        if self._api_gallery_task is None:
            self._api_gallery_task = LoopingCall(self.api_gallery_load)
        return self._api_gallery_task
