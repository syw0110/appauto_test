import unittest
from time import sleep

from logic.login_logic import LoginLogic
from utils.base_utils import driver
from loguru import logger
from data.int_data import nick_data, username, password, logout_info
import warnings


class TsetLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter("ignore", ResourceWarning)
        warnings.simplefilter("ignore", DeprecationWarning)
        cls.login = LoginLogic()
        cls.driver = driver()
        sleep(8)
        cls.username = username
        cls.password = password

    def setUp(self) -> None:
        sleep(1)

    def test01_login(self):
        # 调用登录方法
        self.login.login(self.driver, self.username, self.password)
        sleep(1)
        login_info = self.login.get_login_info(self.driver)
        logger.info(f"获取到的昵称是:{login_info}")

        # 断言
        self.assertEqual(nick_data, login_info)

    def test02_logout(self):
        self.login.logout(self.driver)
        sleep(1)
        get_logout_info = self.login.get_logout_info(self.driver)
        logger.info(f"获取到的登出信息:{get_logout_info}")

        # 断言
        self.assertEqual(logout_info, get_logout_info)


if __name__ == '__main__':
    unittest.main()
