import os.path

import dotenv
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("-U", "--url", help="the URL to test")
    parser.addoption("-E", "--env-file",
                     help="the file where environment variables are located (default: .env)")
    parser.addoption("-B", "--browser",
                     help="the browser to run tests on (must be on the drivers.config[platform][][type])")
    parser.addoption("-D", "--driver",
                     help="the path of the driver (should contain gecko, chrome, etc. in the filename)")
    parser.addoption("-S", "--screenshots-dir",
                     help="the directory path to store screenshots (default: screenshots)")


@pytest.fixture(scope="session", autouse=True)
def load_env(request, driver):
    env_file = request.config.getoption("env_file")
    if env_file is None:
        dotenv.load_dotenv()
    else:
        dotenv.load_dotenv(os.path.abspath(os.path.join(request.config.rootdir, env_file)))
    yield driver


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("browser") or ""

    if browser == "firefox":
        driver = request.config.getoption("driver") or os.environ.get("DRIVER_GECKO") or ""
        if driver == "":
            driver_instance = webdriver.Firefox()
            yield driver_instance
        else:
            driver_instance = webdriver.Firefox(executable_path=os.path.abspath(os.path.join(os.getcwd(), driver)))
            yield driver_instance

    if browser == "chrome":
        driver = request.config.getoption("driver") or os.environ.get("DRIVER_CHROME") or ""
        if driver == "":
            driver_instance = webdriver.Chrome()
            yield driver_instance
        else:
            driver_instance = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), driver)))
            yield driver_instance

    try:
        driver_instance = webdriver.Firefox()
        yield driver_instance
    except Exception:
        pytest.exit("Cannot open browser")
    else:
        driver_instance.quit()
