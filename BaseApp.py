from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://spb.hh.ru/"

    def findElement(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"!Элемент не найден: '{locator}'.")

    def findElements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"!Элемент не найден: '{locator}'.")

    def goToSite(self):
        return self.driver.get(self.base_url)

    def goToPage(self, page):
        return self.driver.get(page)

    def getUrl(self):
        return self.driver.current_url
