import pytest
from pages.astradisk_auth_page import AstradiskAuthPage
from pages.nextcloud_auth_page import NextcloudAuthPage
from settings import login, password


@pytest.fixture()
def astradisk_auth(selenium):
    """Фикстура авторизации в astradisk. После выполнения теста выходит из браузера."""
    page = AstradiskAuthPage(selenium)
    page.enter_login(login)
    page.enter_password(password)
    page.enter_btn_click()
    yield
    selenium.quit()


@pytest.fixture()
def nextcloud_auth(selenium):
    """Фикстура авторизации в nextcloud. После выполнения теста выходит из браузера."""
    page = NextcloudAuthPage(selenium)
    page.enter_login(login)
    page.enter_password(password)
    page.enter_btn_click()
    yield
    selenium.quit()
