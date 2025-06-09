import time

from pages.login_page import LoginPage
from utils.Utils import Utils

class LoginInteractions:
    def __init__(self, login_page: LoginPage):
        self.login_page = login_page

    def login(self, username, password):
        Utils.wait_for_element(lambda: self.login_page.username_input).send_keys(username)
        Utils.wait_for_element(lambda: self.login_page.password_input).send_keys(password)
        time.sleep(1)
        Utils.wait_for_element(lambda: self.login_page.login_button).click()

    def valido_a_mensagem_na_tela(self, mensagem):
        return Utils.wait_for_text(self.login_page.driver, mensagem, 10) is not None