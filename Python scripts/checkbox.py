from selenium.webdriver.common.by import By
from driver import Driver



class CheckBox(Driver):

    def expand_all(self):
        expand_button = self.driver.find_element(By.XPATH, "//button[@aria-label= \"Expand all\"]")
        expand_button.click()


    def complete_checkboxes(self, input_dict):
        click_xpath = "//div[contains(@class, 'check-box-tree')]//span[text()='{}']"
        is_selected_xpath = "//label[span[text()='{}']]//input"
        self.driver.execute_script("window.scrollBy(0,200)")

        for key, value in input_dict.items():
            button = self.driver.find_element(By.XPATH, click_xpath.format(key))
            if value == 'checked':
                check_button = self.driver.find_element(By.XPATH, is_selected_xpath.format(key))
                if not check_button.is_selected():
                    button.click()



    def verify_checked_boxes(self, input_dict):
        list_of_outputs = []
        output_xpath = "//div[span[contains(text(),  'You have selected')]]//span[@class='text-success']"
        outputs = self.driver.find_elements(By.XPATH, output_xpath)
        for output in outputs:
            list_of_outputs.append(output.text)

        for key, value in input_dict.items():
            if value == 'checked':
                if key == 'Word File.doc':
                    verify = 'wordFile'
                elif key == 'Excel File.doc':
                    verify = 'excelFile'
                else:
                    verify = key.lower()
                assert verify in list_of_outputs