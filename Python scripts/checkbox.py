from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def complete_checkboxes(input_dict, driver):
    click_xpath = "//div[contains(@class, 'check-box-tree')]//span[text()='{}']"
    is_selected_xpath = "//label[span[text()='{}']]//input"
    driver.execute_script("window.scrollBy(0,200)")

    for key, value in input_dict.items():
        time.sleep(0.2)
        button = driver.find_element(By.XPATH, click_xpath.format(key))
        if value == 'checked':
            check_button = driver.find_element(By.XPATH, is_selected_xpath.format(key))
            if check_button.is_selected():
                pass
            else:
                button.click()



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/checkbox")

input_dict = {'Home': 'unchecked', 'Desktop': 'unchecked', 'Notes': 'checked',
              'Commands': 'unchecked', 'Documents': 'unchecked', 'WorkSpace': 'unchecked',
              'React': 'unchecked', 'Angular': 'checked', 'Veu': 'checked',
              'Office': 'unchecked', 'Public': 'unchecked', 'Private': 'checked',
              'Classified': 'unchecked', 'General': 'unchecked', 'Downloads': 'checked',
              'Word File.doc': 'checked', 'Excel File.doc': 'unchecked'}

expand_button = driver.find_element(By.XPATH, "//button[@aria-label= \"Expand all\"]")
expand_button.click()

complete_checkboxes(input_dict, driver)


driver.quit()