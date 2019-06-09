import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ContactListPage(BaseAction):
    add_contactor=By.ID,"com.android.contacts:id/floating_action_button"
    @allure.step(title="点击增加信息")
    def click_add_contactor(self):
        self.click_element(self.add_contactor)

