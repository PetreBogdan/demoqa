from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TextBox:
    
    
    def test_boxes(self, input_dict):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demoqa.com/text-box")
        
        # input_dict = {'userName': 'test', 'userEmail': 'test@test.com',
        #               'currentAddress': 'addresstest',
        #               'permanentAddress': 'permanentaddress'}
        
        for key in input_dict:
            input_text = driver.find_element(By.ID, key)
            input_text.send_keys(input_dict[key])
        
        
        wait = WebDriverWait(driver, 10)
        send = wait.until(ec.element_to_be_clickable((By.ID, 'submit')))
        send.click()
        
        outputs = driver.find_elements(By.CLASS_NAME, 'mb-1')
        output_dict = {}
        for output in outputs:
            if output.text.count('Name') == 1:
                output_dict['userName'] = output.text[output.text.find(":") + 1:]
            elif output.text.count('Email') == 1:
                output_dict['userEmail'] = output.text[output.text.find(":") + 1:]
            elif output.text.count('Current Address ') == 1:
                output_dict['currentAddress'] = output.text[output.text.find(":") + 1:]
            elif output.text.count('Permananet Address ') == 1:
                output_dict['permanentAddress'] = output.text[output.text.find(":") + 1:]
        
        for key in input_dict:
            assert input_dict[key] == output_dict[key]
        
        time.sleep(1)
        
        driver.quit()
