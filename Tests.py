# Выполнение тестов

import pytest
from Pages import MainPage
from Pages import ResultPage


# Тест для проверки ввода:
def test_hh_search(browser):
    hh_main_page = MainPage.SearchHelper(browser)
    hh_main_page.goToSite()
    hh_main_page.clickSearchButton()
    # Набор ввода:
    symbols = [' ', '_', '@=', '""', '!"№%"!)(*?:;', '1230', 'Job', 'Работка', '       Раб  ']

    # Негатив для главной страницы:
    for x in range(len(symbols)):
        hh_main_page.goToSite()
        hh_main_page.enterWord(symbols[x])
        hh_main_page.clickSearchButton()

    # Положительный ввод:
    hh_main_page.enterWord("Тестировщик python")

    # Негатив для страницы вакансий:
    for x in range(len(symbols)):
        hh_main_page.clearSearchField()
        hh_main_page.enterWord(symbols[x])
        hh_main_page.clickSearchButton()

    # Положительный ввод:
    hh_main_page.enterWord("Тестировщик python")


# Если текущая страница - это страница с выводом вакансий, -
# выполнить тест на применение фильтра по з/п. Если нет -
# перейти к странице с вакансиями и применить фильтр:
def test_hh_filter(browser):
    hh_second_page = ResultPage.FilterHelper(browser)
    if "https://spb.hh.ru/search/vacancy" in hh_second_page.getUrl():

        # Задание нижнего/верхнего предела доступного по фильтру з/п:
        hh_second_page.chooseMoneyLimit("high")
    else:
        hh_second_page.goToPage('https://spb.hh.ru/vacancies/testirovshik')
        hh_second_page.chooseMoneyLimit("high")