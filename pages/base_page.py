from pytest_selenium import driver


class BasePage(object):
    """Класс базовой стрницы. Конструктор класса принимает на вход объект веб-драйвера,
    адрес страницы и время ожидания элементов"""

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)
