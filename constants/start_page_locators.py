"""Store locators and useful constants"""

START_PAGE_URLS = "https://qa-complex-app-for-testing.herokuapp.com/"

# SIGN UP locators
SIGN_UP_BUTTON_XPATH = "//button[@type='submit']"
SIGN_UP_ERROR_FOR_USERNAME_XPATH = "//div[text() = 'Username must be at least 3 characters.']"
SIGN_UP_ERROR_FOR_EMAIL_XPATH = "//div[text() = 'You must provide a valid email address.']"
SIGN_UP_ERROR_FOR_PASSWORD_XPATH = "//div[text() = 'Password must be at least 12 characters.']"
SIGN_UP_USERNAME_FIELD_XPATH = "//input[@placeholder='Pick a username']"
SIGN_UP_EMAIL_FIELD_XPATH = "//input[@placeholder='you@example.com']"
SIGN_UP_PASSWORD_FIELD_XPATH = "//input[@placeholder='Create a password']"
SIGN_UP_SUCCESSFUL_MESSAGE_FIELD_XPATH = "//h2"

# SigN IN locators
SIGN_IN_USER_NAME_XPATH = "//input[@placeholder='Username']"
SIGN_IN_PASSWORD_XPATH = "//input[@placeholder='Password']"
SIGN_IN_BUTTON_XPATH = "//button[contains(text(),'Sign In')]"
SIGN_IN_SUCCESS_MESSAGE_XPATH = "//h2"
SIGN_IN_ERROR = "//div[contains(text(),'Invalid username \ password')]"

SIGN_OUT_BUTTON = "//button[text()='Sign Out']"
