from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils import wait


class Homepage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = wait(driver)

    def open(self):
        self.driver.get(f"{self.base_url}")

    def type_search(self, term):
        driver = self.driver
        search_input = driver.find_element(By.XPATH, "//input[@name='q']")
        search_input.send_keys(term)
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, "//ul[@role='listbox']//li[1]"), term))
        return driver.find_elements(By.XPATH, "//ul[@role='listbox']//li")

    def clear_search(self):
        driver = self.driver
        search_input = driver.find_element(By.XPATH, "//input[@name='q']")
        search_input.clear()
