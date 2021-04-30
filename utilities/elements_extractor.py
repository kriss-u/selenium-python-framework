from selenium.common import exceptions as e
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.expected_conditions import element_contains_text, all_elements_contain_text
from utilities.webdriver import wait


def find_visibility(condition, driver, locator, locator_type, exception=Exception, wait_duration=10):
    w = wait(driver, wait_duration)
    presence = condition
    if locator_type == "xpath":
        return w.until(presence((By.XPATH, locator)))
    if locator_type == "id":
        return w.until(presence((By.ID, locator)))
    if locator_type == "class":
        return w.until(presence((By.CLASS_NAME, locator)))
    if locator_type == "css":
        return w.until(presence((By.CSS_SELECTOR, locator)))
    if locator_type == "name":
        return w.until(presence((By.NAME, locator)))
    if locator_type == "tag":
        return w.until(presence((By.TAG_NAME, locator)))
    if locator_type == "exact_link_text":
        return w.until(presence((By.LINK_TEXT, locator)))
    if locator_type == "link_text":
        return w.until(presence((By.PARTIAL_LINK_TEXT, locator)))

    raise exception(f"{locator_type}: {locator} not found!")


def find_contains(condition, driver, locator, locator_type, text, exception=Exception, wait_duration=10):
    w = wait(driver, wait_duration)
    presence = condition
    if locator_type == "xpath":
        return w.until(presence((By.XPATH, locator), text))
    if locator_type == "id":
        return w.until(presence((By.ID, locator), text))
    if locator_type == "class":
        return w.until(presence((By.CLASS_NAME, locator), text))
    if locator_type == "css":
        return w.until(presence((By.CSS_SELECTOR, locator), text))
    if locator_type == "name":
        return w.until(presence((By.NAME, locator), text))
    if locator_type == "tag":
        return w.until(presence((By.TAG_NAME, locator), text))
    if locator_type == "exact_link_text":
        return w.until(presence((By.LINK_TEXT, locator), text))
    if locator_type == "link_text":
        return w.until(presence((By.PARTIAL_LINK_TEXT, locator), text))

    raise exception(f"{locator_type}: {locator} doesn't contain text {text}!")


def find_one_present(driver, locator, locator_type="xpath", timeout=10):
    return find_visibility(EC.presence_of_element_located, driver, locator, locator_type,
                           e.NoSuchElementException, timeout)


def find_one_visible(driver, locator, locator_type="xpath", timeout=10):
    return find_visibility(EC.visibility_of_element_located, driver, locator, locator_type,
                           e.ElementNotVisibleException, timeout)


def find_one_contains_text(text, driver, locator, locator_type="xpath", timeout=10):
    return find_contains(element_contains_text, driver, locator, locator_type, text,
                         e.NoSuchElementException, timeout)


def find_all_present(driver, locator, locator_type="xpath", timeout=10):
    return find_visibility(EC.presence_of_all_elements_located, driver, locator, locator_type,
                           e.NoSuchElementException, timeout)


def find_all_contains_text(text, driver, locator, locator_type="xpath", timeout=10):
    return find_contains(all_elements_contain_text, driver, locator, locator_type, text,
                         e.NoSuchElementException, timeout)
