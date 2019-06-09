from appium import webdriver
class BaseDriver:
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    # 可以中文输入
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 不重置应用
    desired_caps['noReset'] = True
    def __init__(self,packagename,activity):
        # app信息
        self.desired_caps['appPackage']=packagename
        self.desired_caps['appActivity']=activity
        self.desired_caps['deviceName'] ="192.168.194.101:5555"
    @classmethod
    def init_driver(cls):
        return  webdriver.Remote('http://127.0.0.1:4723/wd/hub',cls.desired_caps)