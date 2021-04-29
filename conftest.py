import os.path
import traceback

import dotenv
import pytest

from config import load_driver
from config import setup_screenshots


def pytest_addoption(parser):
    parser.addoption("-U", "--base-url", help="the URL to test")
    parser.addoption("-E", "--env-file",
                     help="the file where environment variables are located (default: .env)")
    parser.addoption("-B", "--browser",
                     help="the browser to run tests on (must be on the drivers.config[platform][][type])")
    parser.addoption("-D", "--driver",
                     help="the path of the driver (should contain gecko, chrome, etc. in the filename)")
    parser.addoption("-S", "--screenshots-dir",
                     help="the directory path to store screenshots (default: screenshots)")


@pytest.fixture(scope="session")
def load_env(request):
    env_file = request.config.getoption("env_file")
    if env_file is None:
        dotenv.load_dotenv()
    else:
        dotenv.load_dotenv(os.path.abspath(os.path.join(request.config.rootdir, env_file)))


@pytest.fixture(scope="session", autouse=True)
def url(request, load_env):
    base_url = request.config.getoption("base_url") or os.environ.get("BASE_URL") or ""
    if base_url == "":
        pytest.exit("Please set a BASE_URL environment variable or pass one in -U/--base-url option")
    yield base_url


@pytest.fixture(scope="session")
def screenshots(request, load_env):
    yield setup_screenshots(request)


@pytest.fixture(scope="session")
def driver(request, load_env, screenshots):
    try:
        driver_instance = load_driver(request)
    except Exception:
        traceback.print_exc()
        pytest.exit("Cannot open browser")
    else:
        yield driver_instance
        driver_instance.quit()
