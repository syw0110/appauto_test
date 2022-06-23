from selenium.webdriver.common.by import By


class SetPage():

    # 设置按钮
    set_btn = [(695,80)]

    # 退出登录
    logout = (By.ID, "com.lchr.diaoyu:id/rtv_setting_logout")

    # 确认
    submit = (By.ID, "android:id/button1")
