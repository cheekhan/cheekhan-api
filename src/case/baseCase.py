"""
一个测试用例的基类
用于遍历用例的字段
"""


class BaseCase:

    def __init__(self, base_url, url):
        self.base_url = base_url
        self.url = url
        print('运行API测试用例 : %s' % (base_url + url))

    def next(self):
        """
        遍历检测字段
        :return:
        """
        pass
