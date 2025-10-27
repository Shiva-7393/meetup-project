from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.error_msg_class = "error"

    def website_logo(self):
        return self.driver.find_element(By.XPATH, "//img[@alt='website logo']")
    
    def is_logo_displayed(self):
        try:
            return self.driver.find_element(By.XPATH, "//img[@alt='website logo']").is_displayed()
        except:
            return False
    
    def website_register_image(self):
        return self.driver.find_element(By.XPATH, "//img[@alt='website register']")
    
    def is_register_image_present(self):
        try:
            element = self.driver.find_element(By.XPATH, "//img[@alt='website register']")
            src = element.get_attribute('src')
            return element is not None and src is not None and src != ""
        except:
            return False

    def get_heading_text(self):
        try:
            return self.driver.find_element(By.XPATH, "//h1[text()='Let us join']").text
        except:
            try:
                return self.driver.find_element(By.TAG_NAME, "h1").text
            except:
                return ""

    def get_name_label(self):
        try:
            return self.driver.find_element(By.XPATH, "//label[text()='NAME']").text
        except:
            try:
                labels = self.driver.find_elements(By.TAG_NAME, "label")
                for label in labels:
                    if "name" in label.text.upper():
                        return label.text
                return ""
            except:
                return ""

    def get_topic_label(self):
        try:
            return self.driver.find_element(By.XPATH, "//label[text()='TOPICS']").text
        except:
            try:
                labels = self.driver.find_elements(By.TAG_NAME, "label")
                for label in labels:
                    if "topic" in label.text.upper():
                        return label.text
                return ""
            except:
                return ""

    def enter_name(self, name):
        element = self.driver.find_element(By.ID, "name")
        element.clear()
        element.send_keys(name)

    def select_topic(self, value):
        dropdown = self.driver.find_element(By.ID, "topic")
        select = Select(dropdown)
        select.select_by_value(value)

    def click_register(self):
        button = self.driver.find_element(By.XPATH, "//button[text()='Register Now']")
        button.click()

    def get_error_text(self):
        element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Please enter your name')]")
        return element.text

    def register_image(self):
        """Find register image element"""
        return self.driver.find_element(By.XPATH, "//img[@alt='website register']")

