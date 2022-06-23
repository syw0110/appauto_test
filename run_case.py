from HTMLTestRunner import HTMLTestRunner
import unittest


test_report = "./test_report.html"


if __name__ == '__main__':
    # 进行一次登录

    # 创建一个套件
    suite = unittest.TestLoader().discover("cases",pattern="test*.py")

    with open(test_report,"wb") as f:
        runner = HTMLTestRunner(f,title="测试报告",description='简化版的测试用例')
        runner.run(suite)