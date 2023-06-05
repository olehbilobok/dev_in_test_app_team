from selenium.common.exceptions import NoSuchElementException


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(15)

    def find_element(self, find_by, selector):

        if find_by == 'xpath':
            try:
                return self.driver.find_element_by_xpath(selector)
            except NoSuchElementException:
                pass

        elif find_by == 'id':
            try:
                return self.driver.find_element_by_id(selector)
            except NoSuchElementException:
                pass

        elif find_by == 'class_name':
            try:
                return self.driver.find_element_by_class_name(selector)
            except NoSuchElementException:
                pass

        elif find_by == 'accessibility_id':
            try:
                return self.driver.find_element_by_accessibility_id(selector)
            except NoSuchElementException:
                pass

    @staticmethod
    def click_element(element):
        return element.click()
