class TestHomepage:
    def test_one(self, driver):
        driver.get("https://www.google.com")

    def test_two(self, driver):
        driver.get("https://www.facebook.com")
