from selenium import webdriver
from selenium.webdriver.common.by import By
from driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class WebTables(Driver):

    def click_add(self):
        button_xpath = "//button[text() = 'Add']"
        button = self.driver.find_element(By.XPATH, button_xpath)
        button.click()

    def get_labels(self):
        list_of_labels = []
        xpath_labels = "//div[@class = 'modal-body']//form//label"
        labels = self.driver.find_elements(By.XPATH, xpath_labels)
        for label in labels:
            list_of_labels.append(label.text)
        return list_of_labels

    def complete_form(self, input_dict):
        list_of_labels = self.get_labels()
        input_xpath = "//div[div[label[text() = '{}']]]//input"
        submit_xpath = "//div//button[text()='Submit']"
        for label in list_of_labels:
            input_text = self.driver.find_element(By.XPATH, input_xpath.format(label))
            input_text.send_keys(input_dict[label])
        submit = self.driver.find_element(By.XPATH, submit_xpath)
        submit.click()

    def verify_the_table(self, input_dict):
        output_dict = {}
        member_xpath = "//div[@class='web-tables-wrapper']//div[div[contains(text(), '{}')]]//div"
        members = self.driver.find_elements(By.XPATH, member_xpath.format(input_dict['First Name']))
        tags = ['First Name', 'Last Name', 'Age', 'Email', 'Salary', 'Department']
        for tag, member in zip(tags, members):
            output_dict[tag] = member.text
        for value_input, value_output in zip(input_dict.values(), output_dict.values()):
            assert value_input == value_input