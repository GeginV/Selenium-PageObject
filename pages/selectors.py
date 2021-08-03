from selenium.webdriver.common.by import By

class AuthSelectors:
    AUTH_EMAIL = (By.ID, "email")
    AUTH_PASS = (By.ID, 'pass')
    AUTH_BTN = (By.CLASS_NAME, 'btn-success')
    