from pages.caontact_list_page import ContactListPage
from pages.edit_contactor_page import EditContactorPage


class Page:
    def __init__(self,driver):
        self.driver=driver
    def contact_list_page(self):
        return ContactListPage(self.driver)
    def edit_contactor_page(self):
        return EditContactorPage(self.driver)
