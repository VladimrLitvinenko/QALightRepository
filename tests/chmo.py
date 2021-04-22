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

    def test_chmo(self, setup):
        driver = setup

        driver.get("https://app.slack.com/client/T6RB05744/C6QP0A80Z")
        driver.find_element(by=By.XPATH, value="//input[@id='domain']").send_keys("geniusee")
        driver.find_element(by=By.XPATH, value="//button[contains(text(),'Continue')]").click()
        driver.find_element(by=By.XPATH, value="//input[@placeholder='name@work-email.com']").send_keys(
            "v.litvinenko@geniusee.com")
        driver.find_element(by=By.XPATH, value="//input[@placeholder='Your password']").send_keys("V00646000v")
        driver.find_element(by=By.XPATH, value="//button[@id='signin_btn']").click()
        pavel = driver.find_element(by=By.XPATH, value="//span[text()='Pavlo Burykh']")
        pavel.click()
        driver.find_element(by=By.XPATH, value="//div[@aria-label='Message Pavlo Burykh']").send_keys("чмо")
        driver.find_element(by=By.XPATH, value="//button[@aria-label='Send message']").click()
