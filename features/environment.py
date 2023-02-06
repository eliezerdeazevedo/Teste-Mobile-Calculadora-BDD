from selenium import webdriver

def before_all(context):
        context.driver = driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
caps = {"platformName": "Android", "appium:platformVersion": "6.0", "appium:deviceName": "Android 6.0 x86",
        "appium:automationName": "uiautomator2", "appium:appPackage": "com.android.calculator2",
        "appium:appActivity": "com.android.calculator2.Calculator", "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True, "appium:newCommandTimeout": 3600, "appium:connectHardwareKeyboard": True}
