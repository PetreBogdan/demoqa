import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from builtins import staticmethod

class RadioButtons:
    
    def check_radio_buttons(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://demoqa.com/radio-button")
        
        messages = ['yes', 'impressive', 'no']
        
        for message in messages:
            button = driver.find_element(By.XPATH, f"//label[@for='{message}Radio']")
            try:
                button.click()
                wait = WebDriverWait(driver, 3)
                result = wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'text-success')))
                assert result.text.lower() == message
                driver.refresh()
            except selenium.common.exceptions.TimeoutException:
                print("Button cannot be presed")
        
        driver.quit()