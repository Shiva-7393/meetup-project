from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class WelcomePage:
    def __init__(self, driver):
        self.driver = driver

    def app_logo(self):
         return self.driver.find_element(By.XPATH, "//img[@alt='website logo']")
        
        
    def head_text(self):
        return self.driver.find_element(By.XPATH, "//h1[text()='Welcome to Meetup']").text
         
        
    def description_text(self):
        return self.driver.find_element(By.XPATH, "//p[text()='Please register for the topic']").text
        
    def meet_image(self):
        return self.driver.find_element(By.XPATH, "//img[@alt='meetup']")
    def register(self):
        self.driver.find_element(By.ID, "registerButton").click()
        url= self.driver.current_url
        return url
    

        