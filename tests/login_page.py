"""Start Page tests"""
import logging

import pytest
import time

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
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        driver.implicitly_wait(time_to_wait=20)  # ждем пока найдет элемент
        yield driver
        driver.maximize_window()
        driver.close()

    def test_validation_on_registration_section(self, setup):
        """
        - Click on the sign_up button on the registration section
        - Assert text above 'username' field
        - Assert text above 'email' field
        - Assert text above 'password' field
        """
        driver = setup
        sign_up_button = driver.find_element(By.XPATH, value="//button[@type='submit']")
        sign_up_button.click()
        time.sleep(2.4)

        error_message_for_username = driver.find_element(By.XPATH,
                                                         value="//div[text() = 'Username must be at least 3 characters.']")
        error_message_for_email = driver.find_element(By.XPATH,
                                                      value="//div[text() = 'You must provide a valid email address.']")
        error_message_for_password = driver.find_element(By.XPATH,
                                                         value="//div[text() = 'Password must be at least 12 characters.']")

        assert error_message_for_username.text == "Username must be at least 3 characters."
        assert error_message_for_email.text == "You must provide a valid email address."
        assert error_message_for_password.text == "Password must be at least 12 characters."

    def test_user_is_registered(self, setup):
        """
        - Set variables for 'User Name', 'email', 'password'
        - Enter valid data into 'User Name' field
        - Enter valid data into 'Email' field
        - Enter valid data into 'Password' field
        - Click SIGN UP button
        - Assert that text of the success login is displyaed
        """
        user_name = f"UserName{self.variety}"
        email = f"validemail{self.variety}@gmail.com"
        password = f"Vv{self.variety}vv"
        driver = setup

        user_name_field_sign_up = driver.find_element(By.XPATH, value="//input[@placeholder='Pick a username']")
        user_name_field_sign_up.send_keys(user_name)

        valid_email_field_sign_up = driver.find_element(By.XPATH, value="//input[@placeholder='you@example.com']")
        valid_email_field_sign_up.send_keys(email)

        valid_password_field_sign_up = driver.find_element(By.XPATH, value="//input[@placeholder='Create a password']")
        valid_password_field_sign_up.send_keys(password)

        time.sleep(3)

        sign_up_button = driver.find_element(By.XPATH, value="//*[@type='submit']")
        sign_up_button.click()

        text_after_successfull_registration = driver.find_element(By.XPATH, value="//h2")
        assert text_after_successfull_registration.text == f"Hello {user_name.lower()}, your feed is empty."

    def test_user_is_logged_in(self, setup):
        """
        - Set variable for USER NAME with valid data
        -  Enter current variable into the USER NAME field
        - Enter Valid PASSWORD into the PASSWORD FIELD
        - Click SIGN IN button
        - Assert that USER MAME is displayed on the successful logged in page
        """
        user_name = "ValidUsername6"
        driver = setup

        user_name_field_login = driver.find_element(By.XPATH, value="//input[@placeholder='Username']")
        user_name_field_login.clear()
        user_name_field_login.send_keys(user_name)

        user_password_field_login = driver.find_element(By.XPATH, value="//input[@placeholder='Password']")
        user_password_field_login.clear()
        user_password_field_login.send_keys("V123412341234v")

        sign_in_button = driver.find_element(By.XPATH, value="//button[contains(text(),'Sign In')]")
        sign_in_button.click()

        text_after_successfull_registration = driver.find_element(By.XPATH, value="//h2")
        assert text_after_successfull_registration.text == f"Hello {user_name.lower()}, your feed is empty."

    def test_log_out(self, setup):
        """
        - Enter valid USER NAME into the USER NAME field
        - Enter Valid PASSWORD into the PASSWORD FIELD
        - Click SIGN IN button
        - Click LOG OUT button
        - Assert the SIGN IN button is displayed after user is logged out
        """
        user_name = "ValidUsername6"
        driver = setup

        user_name_field_login = driver.find_element(By.XPATH, value="//input[@placeholder='Username']")
        user_name_field_login.clear()
        user_name_field_login.send_keys(user_name)

        user_password_field_login = driver.find_element(By.XPATH, value="//input[@placeholder='Password']")
        user_password_field_login.clear()
        user_password_field_login.send_keys("V123412341234v")

        sign_in_button = driver.find_element(By.XPATH, value="//button[contains(text(),'Sign In')]")
        sign_in_button.click()

        log_out_button = driver.find_element(By.XPATH, value="//button[text()='Sign Out']")
        log_out_button.click()

        sign_in_button = driver.find_element(By.XPATH, value="//button[contains(text(),'Sign In')]")
        assert sign_in_button.text == "Sign In"

    def test_invalid_login(self, setup):
        """
        - Click SIGN IN button
        - Assert validation message for SIGN IN section
        """
        driver = setup
        sign_in_button = driver.find_element(By.XPATH, value="//button[contains(text(),'Sign In')]")
        sign_in_button.click()
        error_message_for_invalid_login = driver.find_element(By.XPATH,
                                                              value="//div[contains(text(),'Invalid username \ password')]")
        assert error_message_for_invalid_login.text == r"Invalid username \ password"
