import pytest
from pages.register_page import RegisterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_register_page_ui(register_page_setup):
    rp = RegisterPage(register_page_setup)
    
    assert rp.is_logo_displayed(), "App logo is not displayed"
    assert rp.get_heading_text() == "Let us join", f"Expected 'Let us join', got '{rp.get_heading_text()}'"
    assert rp.get_name_label() == "NAME", f"Expected 'NAME', got '{rp.get_name_label()}'"
    assert rp.get_topic_label() == "TOPICS", f"Expected 'TOPICS', got '{rp.get_topic_label()}'"

def test_register_page_error_message(register_page_setup):
    rp = RegisterPage(register_page_setup)
    
    rp.click_register()
    
    WebDriverWait(register_page_setup, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Please enter')]"))
    )
    
    error_text = rp.get_error_text()
    assert "Please enter" in error_text, f"Expected error message containing 'Please enter', got '{error_text}'"

@pytest.mark.parametrize("name,option_value,option_text", [
    ("Jack", "ARTS_AND_CULTURE", "Arts and Culture"),
    ("Jerry", "CAREER_AND_BUSINESS", "Career and Business"),
    ("John", "EDUCATION_AND_LEARNING", "Education and Learning"),
    ("Jim", "FASHION_AND_BEAUTY", "Fashion and Learning"),
    ("Jane", "GAMES", "Games")
])
def test_register_page_functionality_with_valid_inputs(register_page_setup, name, option_value, option_text):
    rp = RegisterPage(register_page_setup)
    
    rp.enter_name(name)
    rp.select_topic(option_value)
    rp.click_register()
    
    WebDriverWait(register_page_setup, 10).until(EC.url_to_be("https://qameetup.ccbp.tech/"))
    
    assert register_page_setup.current_url == "https://qameetup.ccbp.tech/"
    assert f"Hello {name}" in register_page_setup.page_source
    
    # Handle the Fashion and Beauty vs Fashion and Learning exception
    expected_text = "Fashion and Learning" if "Beauty" in option_text else option_text
    assert f"Welcome to {expected_text}" in register_page_setup.page_source
