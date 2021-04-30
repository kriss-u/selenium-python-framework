class element_contains_text(object):
    """ An expectation for checking if the given text is present in the
    specified element.
    locator, text
    """

    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.text in element.text:
            return element


class all_elements_contain_text(object):
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        is_text_present = True
        for element in elements:
            is_text_present = is_text_present and (self.text in element.text)
            if not is_text_present:
                return []
        return elements
