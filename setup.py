import argparse
import platform

from drivers import config, select_driver, load_driver_from_path_or_env
import dotenv
import os
import collections


def load_env(file_path):
    """
    Load the environment variables from a file

    :param file_path: The file path of the environment variables
    :return: None
    """
    file_path_local = file_path
    if file_path is None:
        file_path_local = os.path.join(os.path.dirname(__file__), '.env')

    if not os.path.isfile(file_path_local):
        raise FileNotFoundError

    try:
        dotenv.load_dotenv(os.path.abspath(file_path_local))
    except TypeError:
        dotenv.load_dotenv()


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


def parse_arguments():
    """
    Parses the arguments supplied by user using CLI

    :return: The namespace which contains the arguments and their values
    """
    parser = argparse.ArgumentParser(description="Run the selenium tests")
    parser.add_argument("-u", "--url", help="the URL to test", default=None)
    parser.add_argument("-e", "--env-file",
                        help="the file where environment variables are located (default: .env)")
    parser.add_argument("-b", "--browser",
                        help="the browser to run tests on (must be on the drivers.config[platform][][type])")
    parser.add_argument("-d", "--driver",
                        help="the path of the driver (should contain gecko, chrome, etc. in the filename)")
    parser.add_argument("-s", "--screenshots-dir",
                        help="the directory path to store screenshots (default: screenshots)")
    return parser.parse_args()
