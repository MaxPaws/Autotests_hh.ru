# Главная страница

from selenium.webdriver.common.by import By
from BaseApp import BasePage

# Локаторы для поля ввода на главной странице:
class HhSearchLocators:
    LOCATOR_HH_SEARCH_FIELD = (By.XPATH, "//input[@data-qa='search-input']")
    LOCATOR_HH_SEARCH_BUTTON = (By.XPATH, "//button[@data-qa='search-button']")

# Класс с определением методов для поискового поля главной страницы:
class SearchHelper(BasePage):

    # Ввод пользовательского текста в поле для поиска:
    def enterWord(self, word):
        search_field = self.findElement(HhSearchLocators.LOCATOR_HH_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    # Нажатие на кнопку поиска:
    def clickSearchButton(self):
        return self.findElement(HhSearchLocators.LOCATOR_HH_SEARCH_BUTTON).click()

    # Очистка поискового поля:
    def clearSearchField(self):
        search_field = self.findElement(HhSearchLocators.LOCATOR_HH_SEARCH_FIELD)
        search_field.clear()
        return search_field