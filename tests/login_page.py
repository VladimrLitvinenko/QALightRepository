"""Start Page tests"""
import logging

import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from conftest import BaseTest
from constants import start_page_locators
from pages.start_page import StartPage


class TestStartPage(BaseTest):
    """Test for start page"""

    @pytest.fixture(scope="function")
    def setup(self):
        driver = webdriver.Chrome(
            executable_path="/home/ihor/PycharmProjects/pythonQALightSelenium/drivers/chromedriver")
        driver.maximize_window()
        driver.get(start_page_locators.START_PAGE_URLS)
        driver.implicitly_wait(time_to_wait=20)  # ждем пока найдет элемент
        start_page_obj = StartPage(driver)
        yield start_page_obj
        driver.maximize_window()
        driver.close()

    def test_validation_on_registration_section(self, setup):
        """
        - Click on the sign_up button on the registration section
        - Assert text above 'username' field
        - Assert text above 'email' field
        - Assert text above 'password' field
        """
        start_page_obj = setup
        start_page_obj.click_sign_up_button()
        start_page_obj.verify_error_for_username_field_on_SIGN_UP()
        start_page_obj.verify_error_for_email_field_on_SIGN_UP()
        start_page_obj.verify_error_for_password_field_on_SIGN_UP()
        self.logger.info("all error messages for username, email and password fields are displayed for SIGN UP section")

    def test_user_is_registered(self, setup):
        """
        - Set variables for 'User Name', 'email', 'password'
        - Enter valid data into 'User Name' field
        - Enter valid data into 'Email' field
        - Enter valid data into 'Password' field
        - Click SIGN UP button
        - Assert that text of the success login is displyaed
        """

        start_page_obj = setup
        username = f"UserName{self.variety}"

        # Set valid login, email, password
        start_page_obj.sign_up_user(username=username, email=f"validemail{self.variety}@gmail.com",
                                    password=f"Vv{self.variety}vv")
        self.logger.info(f"Entered unique username = {username}, email and password into SIGN UP section")

        # Verify user is signed up successfully
        start_page_obj.verify_user_is_signed_up(username=username)
        self.logger.info(
            f"Verify  unique username = {username.lower()}, username is displayed after successful SIGN UP")

    def test_user_is_logged_in(self, setup):
        """
        - Set variable for USER NAME with valid data
        -  Enter current variable into the USER NAME field
        - Enter Valid PASSWORD into the PASSWORD FIELD
        - Click SIGN IN button
        - Assert that USER MAME is displayed on the successful logged in page
        """
        start_page_obj = setup
        username = "ValidUsername6"
        start_page_obj.fill_sign_in_field(username=username, password="V123412341234v")
        start_page_obj.verify_user_is_signed_up(username=username.lower())
        self.logger.info(
            f"Verify  unique username = {username.lower()}, username is displayed after successful SIGN IN")

    def test_log_out(self, setup):
        """
        - Enter valid USER NAME into the USER NAME field
        - Enter Valid PASSWORD into the PASSWORD FIELD
        - Click SIGN IN button
        - Click LOG OUT button
        - Assert the SIGN IN button is displayed after user is logged out
        """
        start_page_obj = setup
        start_page_obj.fill_sign_in_field(username="ValidUsername6", password="V123412341234v")
        start_page_obj.log_out()
        self.logger.info("Valid user is successfully login, THEN logged out")

    def test_invalid_login(self, setup):
        """
        - Click SIGN IN button
        - Assert validation message for SIGN IN section
        """
        start_page_obj = setup
        # передаем пустые строки в username и в password дабы вызвать эрор
        start_page_obj.fill_sign_in_field(username="", password="")
        # verify error message
        start_page_obj.verify_invalid_credentials()
        self.logger.info("error message is verified for SIGN IN section")
