# Страница с результатами поиска

from selenium.webdriver.common.by import By
from BaseApp import BasePage

# Локаторы для фильтра:
class HhFilterLocators:
    LOCATOR_HH_FILTER_BUTTON = (By.LINK_TEXT, "Фильтры (1)")

    # Локатор для элементов выбора граничного значения з/п (элементы с текстом '... руб.'):
    LOCATOR_HH_FILTER_MONEY_ELEMENTS = (By.XPATH, "//span[@data-qa='serp__cluster-item-title' and contains(text(), "
                                                 "'руб.')]")

# Класс с элементами фильтра:
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