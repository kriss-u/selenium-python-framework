import collections
import platform
import os
from config.platform_drivers import config
from selenium.webdriver import Chrome, Firefox

from selenium.common.exceptions import WebDriverException


def select_driver(browser_type="chrome"):
    if browser_type == "chrome":
        return Chrome
    if browser_type in ["gecko", "firefox"]:
        return Firefox


def load():
    pass


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


def load_driver(driver_path, browser=None):
    """
    Load the driver for testing as per the argument provided
    :param browser: The browser supplied from the argument
    :param driver_path: The path supplied by user for the driver
    :return: The webdriver instance of the browser
    """
    platform_system = platform.system().lower()
    drivers = config[platform_system]
    drivers_sorted = collections.OrderedDict(sorted(drivers.items()))

    if browser is not None and browser != "":
        browser = browser.lower()
        if driver_path is not None and driver_path != "":
            selected_driver = select_driver(browser)
            return selected_driver(executable_path=os.path.abspath(driver_path))
        else:
            if browser == "firefox":
                browser = "gecko"

            driver_exec = list(filter(lambda x: x["type"] == browser, drivers.values()))[0]["exec"]
            print(driver_exec)
            env_variable = f"DRIVER_{browser.upper()}"
            selected_driver = select_driver(browser)
            driver_path_local = f"drivers/{platform_system}/{driver_exec}"

            return load_driver_from_path_or_env(selected_driver, browser, driver_path_local, env_variable)

    if driver_path is not None and driver_path != "":
        for k in drivers_sorted:
            if drivers[k]["type"] in driver_path.lower():
                selected_driver = select_driver(drivers[k]["type"])
                return selected_driver(executable_path=os.path.join(os.path.dirname(__file__), driver_path))
    else:
        for k in drivers_sorted:
            env_variable = f"DRIVER_{drivers[k]['type'].upper()}"
            selected_driver = select_driver(drivers[k]["type"])

            driver_path_local = f"drivers/{platform_system}/{drivers[k]['exec']}"
            return load_driver_from_path_or_env(selected_driver, drivers[k]["type"], driver_path_local, env_variable)
        else:
            raise Exception("Drivers not found.")
