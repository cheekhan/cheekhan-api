from src.api.demoApi import demo_api_bing
from src.api.module import demoModule
from .baseCase import BaseCase


class DemoBingCase(BaseCase):
    def __init__(self, base_url):
        super().__init__(base_url, demo_api_bing)

    def next(self):
        print("具体执行了用例，验证了字段")


demoModule.use(DemoBingCase)
