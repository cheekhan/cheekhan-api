class BaseModule:
    """模块的基类"""
    name = ""
    base_host = ""  # 域名+端口
    # base_port = ""  # 端口
    base_url = ""  # API前缀
    is_token = False  # 是否需要登录
    cases = []  # 测试用例列表

    def __init__(self, name='默认模块', base_host="http://127.0.0.1:8080", base_url="", is_token=False):
        self.name = name
        self.base_url = base_url
        self.base_host = base_host
        self.is_token = is_token

    def use(self, cls):
        """挂载测试用例"""
        self.cases.append(cls)

    def run(self):
        """执行模块的所有用例"""
        print("模块 - %s - 正在运行测试用例......" % self.name)
        base_uri = self.base_host + self.base_url
        for cls in self.cases:
            case = cls(base_uri)
            case.next()


class DemoModule(BaseModule):
    """示例项目"""

    def __init__(self, name="示例模块", base_host="https://cn.bing.com", base_url="", is_token=False):
        super().__init__(name, base_host, base_url, is_token)


demoModule = DemoModule()
