"""
调度所有的模块
执行测试用例，并且保存测试结果
"""
from src.case.demo import demoModule


def run(config):
    """
    运行测试用例
    :param config:模块和用例的白名单,暂不开发
    :return:
    """
    print('整体运行参数：%s' % config)
    demoModule.run()
