from pytest_selenium import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import AstradiskFilesLocators


class NextcloudFilesPage(BasePage):
    """Класс страницы 'Все файлы' nextcloud."""

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        # Создание нужных элементов
        self.all_files = driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_ALL_FILES)

    def all_files_click(self):
        self.all_files.click()

    def checkbox_empty_folder_click(self):
        self.checkbox_empty_folder = self.driver.find_element(
            *AstradiskFilesLocators.ASTRADISK_FILES_CHECKBOX_EMPTY_FOLDER)
        self.driver.execute_script("arguments[0].click();", self.checkbox_empty_folder)

    def checkbox_empty_folder_invisibility(self):
        WebDriverWait(self.driver, 3).until(
            EC.invisibility_of_element_located(AstradiskFilesLocators.ASTRADISK_FILES_CHECKBOX_EMPTY_FOLDER))

    def checkbox_not_empty_click(self):
        self.checkbox_not_empty = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_CHECKBOX_NOT_EMPTY)
        self.driver.execute_script("arguments[0].click();", self.checkbox_not_empty)

    def checkbox_not_empty_presence(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(AstradiskFilesLocators.ASTRADISK_FILES_CHECKBOX_NOT_EMPTY))

    def actions_click(self):
        self.actions = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_ACTIONS)
        self.actions.click()

    def actions_delete_click(self):
        self.actions_delete = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_ACTIONS_DELETE)
        self.actions_delete.click()

    def delete_header(self):
        self.delete_header = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_DELETE_HEADER).text
        return self.delete_header

    def delete_header_invisibility(self):
        WebDriverWait(self.driver, 3).until(
            EC.invisibility_of_element_located(AstradiskFilesLocators.ASTRADISK_FILES_DELETE_HEADER))

    def delete_notice(self):
        self.delete_notice = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_DELETE_NOTICE).text
        return self.delete_notice

    def delete_yes_btn_click(self):
        self.delete_yes_btn = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_DELETE_YES_BTN)
        self.delete_yes_btn.click()

    def delete_no_btn_click(self):
        self.delete_no_btn = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_DELETE_NO_BTN)
        self.delete_no_btn.click()

    def delete_close_click(self):
        self.delete_close = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_DELETE_CLOSE)
        self.delete_close.click()

    def checkbox_file_one_click(self):
        self.checkbox_file_one = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_CHECKBOX_FILE_ONE)
        self.driver.execute_script("arguments[0].click();", self.checkbox_file_one)

    def checkbox_file_one_presence(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(AstradiskFilesLocators.ASTRADISK_FILES_CHECKBOX_FILE_ONE))

    def checkbox_file_two_click(self):
        self.checkbox_file_two = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_CHECKBOX_FILE_TWO)
        self.driver.execute_script("arguments[0].click();", self.checkbox_file_two)

    def checkbox_file_two_presence(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(AstradiskFilesLocators.ASTRADISK_FILES_CHECKBOX_FILE_TWO))

    def menu_file_three_click(self):
        self.menu_file_three = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_MENU_FILE_THREE)
        self.driver.execute_script("arguments[0].click();", self.menu_file_three)

    def menu_file_three_invisibility(self):
        WebDriverWait(self.driver, 3).until(
            EC.invisibility_of_element_located(AstradiskFilesLocators.ASTRADISK_FILES_MENU_FILE_THREE))

    def menu_delete_click(self):
        self.menu_delete = self.driver.find_element(*AstradiskFilesLocators.ASTRADISK_FILES_MENU_DELETE)
        self.menu_delete.click()
