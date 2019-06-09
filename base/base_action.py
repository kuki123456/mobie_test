from base.base_driver import BaseDriver


class BaseAction:
    def __init__(self,driver):
        self.driver=driver
    def find_element(self,features):
        feature_by, feature_value = features
        return self.driver.find_element(feature_by,feature_value)
    def click_element(self,features):
        self.find_element(features).click()
    def input_text(self,features,text):
        self.find_element(features).send_keys(text)
