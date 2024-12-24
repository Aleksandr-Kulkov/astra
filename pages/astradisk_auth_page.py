from pytest_selenium import driver
from pages.base_page import BasePage
from pages.locators import AstradiskAuthLocators
from settings import astradisk_auth_page_url


class AstradiskAuthPage(BasePage):
    """Класс страницы авторизации astradisk."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = astradisk_auth_page_url
        driver.get(url)
        # Создание нужных элементов
        self.login = driver.find_element(*AstradiskAuthLocators.ASTRADISK_AUTH_LOGIN)
        self.password = driver.find_element(*AstradiskAuthLocators.ASTRADISK_AUTH_PASSWORD)
        self.enter_btn = driver.find_element(*AstradiskAuthLocators.ASTRADISK_AUTH_ENTER_BTN)

    def enter_login(self, value):
        self.login.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def enter_btn_click(self):
        self.enter_btn.click()
