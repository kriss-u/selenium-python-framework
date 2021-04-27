import os

import selenium
from selenium.webdriver import Chrome, Firefox

from selenium.common.exceptions import WebDriverException

config = {
    "windows": {
        0: {
            "type": "chrome",
            "exec": "chromedriver.exe"
        },
        1: {
            "type": "gecko",
            "exec": "geckodriver.exe"
        }
    },
    "linux": {
    },
    "mac": {
    }
}


def select_driver(browser_type="chrome"):
    if browser_type == "chrome":
        return Chrome
    if browser_type in ["gecko", "firefox"]:
        return Firefox


def load_driver_from_path_or_env(selected_driver, driver_type, driver_path=None, env_variable=None):
    if env_variable in os.environ:
        driver_path_env = os.environ[env_variable]
        if driver_path_env != "":
            return selected_driver(executable_path=os.path.abspath(driver_path_env))
    if os.path.exists(driver_path):
        return selected_driver(executable_path=driver_path)

    try:
        return selected_driver()
    except WebDriverException:
        print(f"{driver_type} driver not found.")
