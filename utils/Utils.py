import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utils:
    @staticmethod
    def wait_for_element(get_element_function, attempts=5, interval=1):
        """
        Tenta encontrar um elemento repetidamente até atingir o número de tentativas.

        :param get_element_function: função sem argumentos que retorna o WebElement (ex: lambda: page.element)
        :param attempts: número máximo de tentativas
        :param interval: tempo (em segundos) entre cada tentativa
        :return: WebElement encontrado
        :raises NoSuchElementException: se o elemento não for encontrado após todas as tentativas
        """
        for i in range(attempts):
            try:
                element = get_element_function()
                if element:
                    return element
            except NoSuchElementException:
                time.sleep(interval)
        raise NoSuchElementException(f"Elemento não encontrado após {attempts} tentativas.")

    @staticmethod
    def wait_for_text(driver, text, timeout=10):
        """
        Espera até que um elemento com o texto especificado esteja visível na tela.

        :param driver: Instância do WebDriver
        :param text: Texto a ser procurado
        :param timeout: Tempo máximo de espera em segundos
        :return: O WebElement encontrado ou None se não encontrado
        """
        try:
            xpath = f"//*[contains(text(), '{text}')]"
            return WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
        except TimeoutException:
            print(f"[WARNING] Texto '{text}' não encontrado após {timeout} segundos.")
            return None