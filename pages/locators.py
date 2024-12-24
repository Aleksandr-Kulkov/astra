from selenium.webdriver.common.by import By


class AstradiskAuthLocators:
    ASTRADISK_AUTH_LOGIN = (By.ID, 'user')
    ASTRADISK_AUTH_PASSWORD = (By.ID, 'password')
    ASTRADISK_AUTH_ENTER_BTN = (By.XPATH, '//button//span[text()="Войти"]')


class AstradiskFilesLocators:
    ASTRADISK_FILES_ALL_FILES = (By.XPATH, '//span[contains(text(),"Все файлы")]')
    ASTRADISK_FILES_CHECKBOX_EMPTY_FOLDER = (By.XPATH, '//label//span[contains(text(),"Empty Folder")]')
    ASTRADISK_FILES_CHECKBOX_NOT_EMPTY = (By.XPATH, '//label//span[contains(text(),"Not Empty")]')
    ASTRADISK_FILES_CHECKBOX_FILE_ONE = (By.XPATH, '//label//span[contains(text(),"file 1")]')
    ASTRADISK_FILES_CHECKBOX_FILE_TWO = (By.XPATH, '//label//span[contains(text(),"file 2")]')
    ASTRADISK_FILES_MENU_FILE_THREE = (
    By.XPATH, '//tr[contains(@data-file,"file 3")]//a[@data-action="menu"]//span[@class="icon icon-more"]')
    ASTRADISK_FILES_MENU_DELETE = (By.XPATH, '//span[text()="Удалить файл"]')
    ASTRADISK_FILES_ACTIONS = (By.XPATH, '//span[@class="selectedActions"]//span[text()="Действия"]')
    ASTRADISK_FILES_ACTIONS_DELETE = (
    By.XPATH, '//span[@class="selectedActions"]//span[@class="label" and text()="Удалить"]')
    ASTRADISK_FILES_DELETE_YES_BTN = (By.XPATH, '//*[@role="dialog"]//button[text()="Да"]')
    ASTRADISK_FILES_DELETE_NO_BTN = (By.XPATH, '//*[@role="dialog"]//button[text()="Нет"]')
    ASTRADISK_FILES_DELETE_CLOSE = (By.XPATH, '//*[@role="dialog"]//button[contains(@aria-label,"Закрыть")]')
    ASTRADISK_FILES_DELETE_HEADER = (By.XPATH, '//*[@role="dialog"]//h2')
    ASTRADISK_FILES_DELETE_NOTICE = (By.XPATH, '//*[@role="dialog"]//p')


class NextcloudAuthLocators:
    NEXTCLOUD_AUTH_LOGIN = (By.ID, 'user')
    NEXTCLOUD_AUTH_PASSWORD = (By.ID, 'password')
    NEXTCLOUD_AUTH_ENTER_BTN = (By.XPATH, '//button//span[text()="Войти"]')
