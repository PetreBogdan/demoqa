from selenium.webdriver.common.by import By
from driver import Driver


class RadioButtons(Driver):

    def get_labels(self):
        list_of_labels = []
        label_xpath = "//div[contains(@class, 'custom-radio')]//label"
        labels = self.driver.find_elements(By.XPATH, label_xpath)
        for label in labels:
            list_of_labels.append(label.text)
        return list_of_labels

    def check_radio(self):
        list_of_labels = self.get_labels()
        input_xpath = "//div[label[text() = '{}']]/input"
        label_xpath = "//div[contains(@class, 'custom-radio')]//label[text() = '{}']"
        for label in list_of_labels:
            radio = self.driver.find_element(By.XPATH, label_xpath.format(label))
            radio_selected = self.driver.find_element(By.XPATH, input_xpath.format(label))
            radio.click()
            try:
                assert radio_selected.is_selected()
            except AssertionError:
                print("Radio button {} could not be pressed".format(radio.text))