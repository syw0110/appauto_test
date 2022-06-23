
# 请求url
BASE_URL = "http://127.0.0.1:4723/wd/hub"

# app启动参数
CAPS = {
  "platformName": "Android",
  "platformVersion": "6",
  "deviceName": "127.0.0.1:7555",
  "appPackage": "com.lchr.diaoyu",
  "appActivity": "com.lchr.diaoyu.SplashActivity",
  "noReset": True,
  "newCommandTimeout": 6000,
  "skipServerInstallation": False,
  "automationName": "UiAutomator2",
  "ensureWebviewsHavePages": True,
  "appWaitForLaunch": False,
  "enableWebviewDetailsCollection": False
}