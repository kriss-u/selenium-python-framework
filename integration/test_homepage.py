class TestHomepage:
    def test_one(self, driver):
        driver.get("https://www.google.com")
        assert False

    def test_two(self, driver):
        driver.get("https://www.facebook.com")
        assert True
