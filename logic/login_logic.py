from time import sleep

from pages.set_page import SetPage
from pages.login_page import LoginPage


class LoginLogic():

    # 登录操作
    def login(self, driver, username, password):
        # 1.点击我
        driver.find_element(*LoginPage.my_btn).click()
        sleep(2)
        # 2.点击登录
        driver.find_element(*LoginPage.login).click()
        sleep(2)
        # 3.点击密码登录
        driver.find_element(*LoginPage.login_by_pwd).click()

        # 4.输入手机号
        driver.find_element(*LoginPage.iphone).send_keys(username)

        # 5.输入密码
        driver.find_element(*LoginPage.password).send_keys(password)

        # 6.选择复选框
        driver.tap(LoginPage.login_checkbox)

        # 7.点击登录
        driver.find_element(*LoginPage.btn_login).click()

    def get_login_info(self, driver):
        # 获取登录成功后的昵称
        return driver.find_element(*LoginPage.nick_name).text

    def logout(self, driver):
        # 点击设置
        driver.tap(SetPage.set_btn)
        sleep(1)

        # 点击退出按钮
        # 如果屏幕小，需要滑动
        # driver.swipe(x1,y1,x1,-300)
        driver.find_element(*SetPage.logout).click()
        sleep(0.5)

        # 点击确认按钮
        driver.find_element(*SetPage.submit).click()

    def get_logout_info(self, driver):
        return driver.find_element(*LoginPage.login).text


# if __name__ == '__main__':
#     driver = driver()
#     sleep(8)
#     login = LoginLogic()
#     login.login(driver, "17364813531", "s123456")
