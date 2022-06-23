from appium import webdriver

from setting import BASE_URL,CAPS


# 初始化driver

def driver():
    return webdriver.Remote(BASE_URL, CAPS)
