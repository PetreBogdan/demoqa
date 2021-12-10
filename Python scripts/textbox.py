from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from builtins import staticmethod


class TextBox:
    
    driver = None
    
    
    def navigate_to(self, url):
        TextBox.driver = webdriver.Chrome()
        TextBox.driver.maximize_window()
        TextBox.driver.get(url)
    
    def get_labels(self):
        list_of_labels = []
        elements = TextBox.driver.find_elements(By.XPATH, '//div/form//div//label')
        for element in elements:
            list_of_labels.append(element.text)
        return list_of_labels
    
    def input_data(self, input_dict):
        list_of_labels = self.get_labels()
        input_xpath = "//div[div/label[text()='{}']]//*[contains(@class, \"form-control\")]"
        for label in list_of_labels:
            input_text = TextBox.driver.find_element(By.XPATH,input_xpath.format(label))
            try:
                input_text.send_keys(input_dict[label])
            except KeyError:
                print("Input label not found")
        wait = WebDriverWait(TextBox.driver, 10)
        send = wait.until(ec.element_to_be_clickable((By.ID, 'submit')))
        TextBox.driver.execute_script("window.scrollBy(0,100)", send)
        send.click()
        
    def verify_output(self, input_dict):
        outputs = TextBox.driver.find_elements(By.XPATH, "//div[@id='output']//p")
        output_dict = {}
        for output in outputs:
            if output.text.count('Name') == 1:
                output_dict['Full Name'] = output.text[output.text.find(":") + 1:]
            elif output.text.count('Email') == 1:
                output_dict['Email'] = output.text[output.text.find(":") + 1:]
            elif output.text.count('Current Address ') == 1:
                output_dict['Current Address'] = output.text[output.text.find(":") + 1:]
            elif output.text.count('Permananet Address ') == 1:
                output_dict['Permanent Address'] = output.text[output.text.find(":") + 1:]
    
        for key in input_dict:
            assert input_dict[key] == output_dict[key]
        TextBox.driver.quit()
