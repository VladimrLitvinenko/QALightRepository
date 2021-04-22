"""Start Page tests"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import BaseTest


class TestStartPage(BaseTest):
    """Test for start page"""

    @pytest.fixture(scope="function")
    def setup(self):
        driver = webdriver.Chrome(
            executable_path="/home/ihor/PycharmProjects/pythonQALightSelenium/drivers/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(time_to_wait=20)  # ждем пока найдет элемент
        yield driver
        driver.maximize_window()
        driver.close()

    def test_empty_fields_login(self, setup):
        driver = setup

        # Open start page
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        # Clear password and login fields
        username_input_field = driver.find_element(by=By.XPATH, value="//input[@placeholder='Username']")
        username_input_field.clear()

        password_input_field = driver.find_element(by=By.XPATH, value="//input[@placeholder='Password']")
        password_input_field.clear()
        # Click on Sign in
        sign_in_button = driver.find_element(by=By.XPATH, value="//*[@class='btn btn-primary btn-sm']")
        sign_in_button.click()

        # Verify the error message
        error_message = driver.find_element(by=By.XPATH, value="//div[@class='alert alert-danger text-center']")
        assert error_message.text == r"Invalid username \ password"

# """1) Verify, the error messanges will be displayed if the [Sign up for OurApp] button is clicked"""
# """
#  - Click the SUBMIT button
#  - get the error message for 'Pick a username' field
#  - get the error message for 'email' field
#  - get the error message for 'password' field
#  """
# driver.find_element_by_xpath("//button[@type='submit']").click()
# print(driver.find_element_by_xpath("//div[text() = 'Username must be at least 3 characters.']").text)
# print(driver.find_element_by_xpath("//div[text() = 'You must provide a valid email address.']").text)
# print(driver.find_element_by_xpath("//div[text() = 'Password must be at least 12 characters.']").text)
#
# """2) Verify the error message will be displayed if invalid login and password are entered into 'Sign in' section"""
# """
#  - Enter invalid username
#  - enter invalid password
#  - click 'Sign In' button
#  - Verify validation message
#  """
# driver.find_element_by_xpath("//input[@name='username' and @placeholder= 'Username']").send_keys("any")
# driver.find_element_by_xpath("//input[@name = 'password' and @placeholder='Password']").send_keys("54555")
# driver.find_element_by_xpath("//button[text()='Sign In']").click()
# print(driver.find_element_by_xpath("//div[contains(text(),'Invalid username \ password')]").text)
#
#
# """3) Verify the user is signed up if the valid data is entered"""
# """
#  - Enter valid unique username
#  - Enter valid unique email
#  - Enter valid password
#  - Click 'Sign up' button
# """
# driver.find_element_by_xpath("//input[@placeholder='Pick a username']").send_keys("anyuser" + iniq_value)
# driver.find_element_by_xpath("//input[@name='email' and @placeholder= 'you@example.com']").send_keys("uniqemail" + iniq_value + "@gmail.com")
# driver.find_element_by_xpath("//input[@placeholder='Create a password']").send_keys("^jUPfbD9LkY6")
# driver.find_element_by_xpath("//button[contains(text(),'Sign up for OurApp')]").click()
#
# """4) Verify the user is logged out"""
# """
#  - Click log out button
#  - Verify the Start page is displayed
# """
# driver.find_element_by_xpath("//button[text()='Sign Out']").click()
# print(driver.find_element_by_xpath("//h4/a[@href ='/']").text)
#
# """5) Verify the user will be logged in if the valid data is entered"""
# """
#  - Enter valid username into Username field of 'Sign in' section
#  - Enter valid password into password field of 'Sign in' section
#  - Click valid 'Sign In' button
#  - Verify Text center section is displayed
# """
# driver.find_element_by_xpath("//input[@name='username' and @placeholder= 'Username']").send_keys("any")
# driver.find_element_by_xpath("//input[@name = 'password' and @placeholder='Password']").send_keys("^jUPfbD9LkY6")
# driver.find_element_by_xpath("//button[text()='Sign In']").click()
# print("MESSAGE AFTER SIGN IN:", driver.find_element_by_xpath("//div[@class='text-center']").text)
