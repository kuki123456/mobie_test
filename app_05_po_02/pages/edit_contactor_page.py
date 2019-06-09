import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditContactorPage(BaseAction):
    name=By.XPATH,"//*[@text='姓名']"
    phone=By.XPATH,"//*[@text='电话']"
    @allure.step(title="输入姓名")
    def input_name(self,name):
        self.input_text(self.name,name)
    @allure.step(title="输入电话")
    def input_phone(self,phone):
        self.input_text(self.phone,phone)
        allure.attach("截图：",self.driver.get_screenshot_as_png(),allure.attach_type.PNG)
