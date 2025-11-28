from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    username = (By.ID, 'user-name')
    password = (By.ID, 'password')
    login_button = (By.ID, 'login-button')

    def login(self, username, password):
        self.type(*self.username, text=username)
        self.type(*self.password, text=password)
        self.click(*self.login_button)