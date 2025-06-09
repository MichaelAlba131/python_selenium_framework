import shutil
import tempfile
import uuid

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
import allure

TEMP_DIRS = []

def before_scenario(context, scenario):
    browser = os.getenv("BROWSER", "chrome").lower()
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        context.driver = webdriver.Firefox(service=service, options=options)

    else:
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

        # Diretório único usando UUID
        user_data_dir = os.path.join(tempfile.gettempdir(), f"chrome-profile-{uuid.uuid4()}")
        os.makedirs(user_data_dir, exist_ok=True)
        TEMP_DIRS.append(user_data_dir)
        options.add_argument(f"--user-data-dir={user_data_dir}")

        service = ChromeService(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=options)

    context.driver.maximize_window()


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        try:
            screenshot = context.driver.get_screenshot_as_png()
            allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            context.driver.quit()
        except Exception as e:
            print(f"[WARN] Não foi possível capturar screenshot: {e}")

    # Limpa perfis temporários criados
    for temp_dir in TEMP_DIRS:
        shutil.rmtree(temp_dir, ignore_errors=True)
    TEMP_DIRS.clear()