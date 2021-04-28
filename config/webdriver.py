import os
import platform
import sys

from selenium import webdriver

from config import platform_exec


def get_driver_instance(request, driver_type, driver):
    system = platform.system().lower()
    driver_path_arg = request.config.getoption("driver")
    driver_name_project = platform_exec[system][driver_type]
    driver_path_project = os.path.join('drivers', driver_name_project)
    driver_path_project = (os.path.exists(
        os.path.join(request.config.rootdir, driver_path_project)) and driver_path_project) or None
    driver_path_default = os.environ.get(f"DRIVER_{driver_type.upper()}") or driver_path_project
    driver_path = (driver_path_arg and os.path.join(os.getcwd(), driver_path_arg)) or (
            driver_path_default and os.path.join(request.config.rootdir, driver_path_default)) or ""

    sys.path.append(os.path.abspath(os.path.join(driver_path_default, os.pardir)))

    if driver_path == "":
        return driver()
    return driver(executable_path=os.path.abspath(driver_path))


def load_driver(request):
    browser = request.config.getoption("browser") or ""
    # if browser == "firefox":
    #     return get_driver_instance(request, "gecko", webdriver.Firefox)
    if browser == "chrome":
        return get_driver_instance(request, "chrome", webdriver.Chrome)

    return get_driver_instance(request, "gecko", webdriver.Firefox)
