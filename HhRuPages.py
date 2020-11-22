from BaseApp import BasePage
from selenium.webdriver.common.by import By


# Локаторы для поля ввода на главной странице:
class HhSearchLocators:
    LOCATOR_HH_SEARCH_FIELD = (By.XPATH, "//input[@data-qa='search-input']")
    LOCATOR_HH_SEARCH_BUTTON = (By.XPATH, "//button[@data-qa='search-button']")


# Локаторы для фильтра на странице с вакансиями:
class HhFilterLocators:
    LOCATOR_HH_FILTER_BUTTON = (By.LINK_TEXT, "Фильтры (1)")

    # Локатор для элементов выбора граничного значения з/п (элементы с текстом '... руб.'):
    LOCATOR_HH_FILTER_MONEY_ELEMENTS = (By.XPATH, "//span[@data-qa='serp__cluster-item-title' and contains(text(), "
                                                 "'руб.')]")


# Класс для поискового поля главной страницы:
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

    # Ояистка поискового поля:
    def clearSearchField(self):
        search_field = self.findElement(HhSearchLocators.LOCATOR_HH_SEARCH_FIELD)
        search_field.clear()
        return search_field


# Класс для элементов фильтраа а странице с вакансиями:
class FilterHelper(BasePage):

    # Нахождение всех элементов фильтрации з/п и применение необходимого, в зависимости от указания
    # верхнего/нижнего предела по з/п:
    def chooseMoneyLimit(self, limit):
        global fElement
        filters = self.findElements(HhFilterLocators.LOCATOR_HH_FILTER_MONEY_ELEMENTS)

        # Если в тесте указан верхний предел -
        # берем последний элемент найденного списка (максимальный предел)
        if limit == "high":
            fElement = filters[-1]

        # Если в тесте указан нижний предел -
        # берем первый элемент найденного списка (минимальный предел)
        elif limit == "low":
            fElement = filters[0]
        fElement.click()
