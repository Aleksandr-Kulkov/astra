from pages.astradisk_files_page import AstradiskFilesPage
from settings import *


def test_astradisk_files_delete_empty_folder(astradisk_auth, selenium):
    """Валидация подтверждения действий при удалении пустого каталога через раздел 'Действия'."""
    page = AstradiskFilesPage(selenium)
    page.all_files_click()
    page.checkbox_empty_folder_click()
    page.actions_click()
    page.actions_delete_click()
    assert page.delete_header() == delete_header_one_folder
    assert page.delete_notice() == delete_notice_one_folder
    page.delete_yes_btn_click()
    page.checkbox_empty_folder_invisibility()


def test_astradisk_files_cancel_delete_not_empty(astradisk_auth, selenium):
    """Валидация отмены удаления непустого каталога через раздел 'Действия'."""
    page = AstradiskFilesPage(selenium)
    page.all_files_click()
    page.checkbox_not_empty_click()
    page.actions_click()
    page.actions_delete_click()
    assert page.delete_header() == delete_header_one_folder
    assert page.delete_notice() == delete_notice_one_folder
    page.delete_no_btn_click()
    page.checkbox_not_empty_presence()


def test_astradisk_files_close_delete_two_files(astradisk_auth, selenium):
    """Валидация закрытия окна удаления двух файлов через раздел 'Действия'."""
    page = AstradiskFilesPage(selenium)
    page.all_files_click()
    page.checkbox_file_one_click()
    page.checkbox_file_two_click()
    page.actions_click()
    page.actions_delete_click()
    assert page.delete_header() == delete_header_two_files
    assert page.delete_notice() == delete_notice_two_files
    page.delete_close_click()
    page.delete_header_invisibility()
    page.checkbox_file_one_presence()
    page.checkbox_file_two_presence()


def test_astradisk_files_menu_delete_file(astradisk_auth, selenium):
    """Валидация подтверждения действий при удалении файла через меню."""
    page = AstradiskFilesPage(selenium)
    page.all_files_click()
    page.menu_file_three_click()
    page.menu_delete_click()
    assert page.delete_header() == delete_header_one_file
    assert page.delete_notice() == delete_notice_one_file
    page.delete_yes_btn_click()
    page.menu_file_three_invisibility()
