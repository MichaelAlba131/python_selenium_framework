from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://login.dafiti.com.br/")

    # Locators (apenas como propriedades)
    @property
    def username_input(self):
        return self.driver.find_element(By.XPATH, "//input[@name='email']")

    @property
    def password_input(self):
        return self.driver.find_element(By.XPATH, "//input[@name='password']")

    @property
    def login_button(self):
        return self.driver.find_element(By.XPATH, "//button/div[text()='Entrar']//ancestor::button")

    @property
    def page_title(self):
        return self.driver.title