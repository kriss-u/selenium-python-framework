from selenium.webdriver.common.by import By

from utilities import find_all_contains_text
from utilities import find_one_present
from utilities import wait


class Homepage:
    def __init__(self, driver, base_url, timeout=10):
        self.driver = driver
        self.base_url = base_url
        self.wait = wait(driver, timeout)

    def open(self):
        self.driver.get(f"{self.base_url}")

    def type_search(self, term):
        driver = self.driver
        search_input = find_one_present(driver, "//input[@name='q']", "xpath")
        search_input.send_keys(term)
        return find_all_contains_text(term, driver, "//ul[@role='listbox']//li", "xpath")

    def clear_search(self):
        driver = self.driver
        search_input = driver.find_element(By.XPATH, "//input[@name='q']")
        search_input.clear()
