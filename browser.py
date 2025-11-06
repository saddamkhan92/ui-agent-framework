from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserWrapper:
    def __init__(self):
        chrome_options = Options()
       # chrome_options.add_argument("--headless")  # optional
        service = Service()
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def go(self, url: str):
        self.driver.get(url)

    def click(self, selector: str):
        elem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        )
        elem.click()

    def type(self, selector: str, text: str):
        import time
        time.sleep(2)
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
        )
        elem.clear()
        elem.send_keys(text)

    def get_text(self, selector: str) -> str:
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
        )
        return elem.text

    def screenshot(self, path: str):
        self.driver.save_screenshot(path)

    def close(self):
        self.driver.quit()
