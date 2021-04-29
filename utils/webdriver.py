from selenium.webdriver.support.ui import WebDriverWait


def wait(driver, time=10):
    return WebDriverWait(driver, time)
