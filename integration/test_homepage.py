import pytest
from selenium.webdriver.common.by import By

from pages import Homepage
from utilities import assert_in_all


class TestHomepage:
    # FIXME: Add proper fixture
    @pytest.fixture(scope="class", autouse=True)
    def homepage(self, driver, url):
        yield Homepage(driver, url)

    # @pytest.fixture(scope="class", autouse=True)
    # def wait(self, driver):
    #     yield WebDriverWait(driver, 10)

    def test_valid_search_suggestion(self, homepage):
        homepage.open()
        results = homepage.type_search("google")
        assert_in_all("google", results)
        homepage.clear_search()
        results = homepage.type_search("facebook")
        assert_in_all("facebook", results)

    def test_i_am_feeling_lucky_btn(self, homepage, driver):
        homepage.open()
        # FIXME: Move the code below to Homepage class
        elem = driver.find_element(By.XPATH, "//div[@class='FPdoLc tfB0Bf']//input[@name='btnI']")
        elem.click()
        assert '/doodles' in driver.current_url
