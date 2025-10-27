from pages.welcome_page import WelcomePage
import pytest 
def test_welcome_page(setup):
    driver= setup
    wp=WelcomePage(driver)
    assert wp.app_logo().is_displayed()
    assert wp.head_text()=="Welcome to Meetup"
    assert wp.description_text()=="Please register for the topic"
    assert wp.meet_image().is_displayed()
    assert wp.register()=="https://qameetup.ccbp.tech/register"
