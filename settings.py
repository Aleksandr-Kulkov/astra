import os
from dotenv import load_dotenv

# Auth
load_dotenv()

login = os.getenv('login')
password = os.getenv('password')

# URL
astradisk_auth_page_url = 'https://test-disk.promo.astradisk.ru/login'
nextcloud_auth_page_url = 'https://test-vanilla.promo.astradisk.ru/login'

# Text
delete_header_one_folder = 'Удалить 1 каталог?'
delete_notice_one_folder = 'Вы уверены, что хотите удалить 1 каталог?'
delete_header_two_files = 'Удалить 2 файла?'
delete_notice_two_files = 'Вы уверены, что хотите удалить 2 файла?'
delete_header_one_file = 'Удалить файл?'
delete_notice_one_file = 'Вы уверены, что хотите удалить "file 3.docx"?'
