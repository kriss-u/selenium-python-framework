from selenium.webdriver import Chrome, Firefox

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
    if browser_type == "gecko":
        return Firefox
