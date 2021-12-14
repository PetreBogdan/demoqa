from selenium import webdriver
from selenium.webdriver.common.by import By


class RadioButtons:


    driver = None
    
    def navigate_to(self, url):
        RadioButtons.driver = webdriver.Chrome()
        RadioButtons.driver.maximize_window()
        RadioButtons.driver.get(url)

    
    def get_labels(self):
        list_of_labels = []
        label_xpath = "//div[contains(@class, 'custom-radio')]//label"
        labels = RadioButtons.driver.find_elements(By.XPATH, label_xpath)
        for label in labels:
            list_of_labels.append(label.text)
        return list_of_labels

    def check_radio(self):
        list_of_labels = self.get_labels()
        input_xpath = "//div[label[text() = '{}']]/input"
        label_xpath = "//div[contains(@class, 'custom-radio')]//label[text() = '{}']"
        for label in list_of_labels:
            radio = RadioButtons.driver.find_element(By.XPATH, label_xpath.format(label))
            radio_selected = RadioButtons.driver.find_element(By.XPATH, input_xpath.format(label))
            radio.click()
            try:
                assert radio_selected.is_selected()
            except AssertionError:
                print("Radio button {} could not be pressed".format(radio.text))
        RadioButtons.driver.quit()
#
#
# if __name__ == '__main__':
#
#     radio = RadioButtons()
#     lista = radio.get_labels()
#     radio.check_radio()