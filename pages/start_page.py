"""Encapsulate actions related to start page"""
import logging
import time

from selenium.webdriver.common.by import By

from constants import start_page_locators


class StartPage:
    """class stores actions and virefications related to start page"""

    def __init__(self, driver):
        self.driver = driver
        # self.logger = logging.getLogger(__name__)

    # Создали метод который заполняет поля SIGN IN секции
    def fill_sign_in_field(self, username, password):
        """
        Fill specified variables
        """

        user_name_field_login = self.driver.find_element(By.XPATH, value=start_page_locators.SIGN_IN_USER_NAME_XPATH)
        user_name_field_login.clear()
        user_name_field_login.send_keys(username)
        # self.logger.info("Set login value: ", username)

        user_password_field_login = self.driver.find_element(By.XPATH, value=start_page_locators.SIGN_IN_PASSWORD_XPATH)
        user_password_field_login.clear()
        user_password_field_login.send_keys(password)
        # self.logger.info("Set login value: ", password)

        sign_in_button = self.driver.find_element(By.XPATH, value=start_page_locators.SIGN_IN_BUTTON_XPATH)
        sign_in_button.click()
        # self.logger.info("Click SIGN IN button")

    def verify_invalid_credentials(self):
        """Check error message on invalid credentials"""
        error_message_for_invalid_login = self.driver.find_element(By.XPATH, value=start_page_locators.SIGN_IN_ERROR)
        assert error_message_for_invalid_login.text == r"Invalid username \ password"
        # self.logger.debug("Error message is verified")

    def log_out(self):
        log_out_button = self.driver.find_element(By.XPATH, value=start_page_locators.SIGN_OUT_BUTTON)
        log_out_button.click()

        sign_in_button = self.driver.find_element(By.XPATH, value=start_page_locators.SIGN_IN_BUTTON_XPATH)
        assert sign_in_button.text == "Sign In"

    def fill_sign_up_username(self, username):
        user_name_field_sign_up = self.driver.find_element(By.XPATH,
                                                           value=start_page_locators.SIGN_UP_USERNAME_FIELD_XPATH)
        user_name_field_sign_up.send_keys(username)

    def fill_sign_up_email(self, email):
        valid_email_field_sign_up = self.driver.find_element(By.XPATH,
                                                             value=start_page_locators.SIGN_UP_EMAIL_FIELD_XPATH)
        valid_email_field_sign_up.send_keys(email)

    def fill_sign_up_password(self, password):
        valid_password_field_sign_up = self.driver.find_element(By.XPATH,
                                                                value=start_page_locators.SIGN_UP_PASSWORD_FIELD_XPATH)
        valid_password_field_sign_up.send_keys(password)

    def sign_up_user(self, username, email, password):
        self.fill_sign_up_username(username)
        self.fill_sign_up_email(email)
        self.fill_sign_up_password(password)
        time.sleep(5)
        sign_up_button = self.driver.find_element(By.XPATH, value=start_page_locators.SIGN_UP_BUTTON_XPATH)
        sign_up_button.click()

    def verify_user_is_signed_up(self, username):
        text_after_successfull_registration = self.driver.find_element(By.XPATH,
                                                                       value=start_page_locators.SIGN_UP_SUCCESSFUL_MESSAGE_FIELD_XPATH)
        assert text_after_successfull_registration.text == f"Hello {username.lower()}, your feed is empty."

    def click_sign_up_button(self):
        sign_up_button = self.driver.find_element(By.XPATH, value=start_page_locators.SIGN_UP_BUTTON_XPATH)
        sign_up_button.click()

    def verify_error_for_username_field_on_SIGN_UP(self):
        error_message_for_username = self.driver.find_element(By.XPATH,
                                                              value=start_page_locators.SIGN_UP_ERROR_FOR_USERNAME_XPATH)
        assert error_message_for_username.text == "Username must be at least 3 characters."

    def verify_error_for_email_field_on_SIGN_UP(self):
        error_message_for_email = self.driver.find_element(By.XPATH,
                                                           value=start_page_locators.SIGN_UP_ERROR_FOR_EMAIL_XPATH)
        assert error_message_for_email.text == "You must provide a valid email address."

    def verify_error_for_password_field_on_SIGN_UP(self):
        error_message_for_password = self.driver.find_element(By.XPATH,
                                                              value=start_page_locators.SIGN_UP_ERROR_FOR_PASSWORD_XPATH)
        assert error_message_for_password.text == "Password must be at least 12 characters."