import tempfile

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
import allure


def before_scenario(context, scenario):
    browser = os.getenv("BROWSER", "chrome").lower()
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(service=service, options=options)

    else:  # Chrome
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")  # Chrome 109+
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        # Garante que cada execução usa um diretório de perfil isolado
        temp_profile = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={temp_profile}")

        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=options)

    context.driver.maximize_window()


def after_scenario(context, scenario):
    screenshot = context.driver.get_screenshot_as_png()
    # Anexa no relatório Allure
    allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
    context.driver.quit()