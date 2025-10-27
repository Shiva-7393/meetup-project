import pytest 
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)    
    driver.get("https://qameetup.ccbp.tech/")
    yield driver
    time.sleep(2)
    
    driver.quit()

@pytest.fixture()
def register_page_setup(setup):
    """Fixture that navigates to the register page and returns the driver"""
    driver = setup
    
    from pages.welcome_page import WelcomePage
    wp = WelcomePage(driver)
    wp.register()
    
    # Wait for register page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='website logo']"))
    )
    
    return driver


