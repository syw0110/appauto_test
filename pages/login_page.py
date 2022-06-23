from selenium.webdriver.common.by import By


class LoginPage():

    # 我的
    my_btn = (By.ID, "com.lchr.diaoyu:id/btn_tab_mine")

    # 点击登录
    login = (By.ID, "com.lchr.diaoyu:id/tv_click2login")

    # 点击密码登录
    login_by_pwd = (By.ID, "com.lchr.diaoyu:id/login_by_pwd")

    # 输入手机号或邮箱
    iphone = (By.ID, "com.lchr.diaoyu:id/et_account")

    # 输入密码
    password = (By.ID, "com.lchr.diaoyu:id/et_pwd")

    # 协议复选框
    login_checkbox = [(50,600)]

    # 登录按钮
    btn_login = (By.ID, "com.lchr.diaoyu:id/btn_login")

    # 昵称
    nick_name = (By.ID, "com.lchr.diaoyu:id/user_nick_name")

