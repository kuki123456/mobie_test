import time

import pytest

from base.base_build_data import build_data
from base.base_driver import BaseDriver
from pages.page import Page
class TestContact:
    def setup(self):
        self.basedriver=BaseDriver("com.android.contacts",".activities.PeopleActivity")
        self.driver=self.basedriver.init_driver()
        self.page=Page(self.driver)
    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize("argus",build_data("test_contact","contact.yaml"))
    def test_contact(self,argus):
        name=argus["name"]
        phone=argus["phone"]
        self.page.contact_list_page().click_add_contactor()
        self.page.edit_contactor_page().input_name(name)
        self.page.edit_contactor_page().input_phone(phone)
        self.driver.press_keycode(4)
        time.sleep(3)



