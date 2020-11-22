import HhRuPages


# Тест для проверки ввода:
def test_hh_search(browser):
    hh_main_page = HhRuPages.SearchHelper(browser)
    hh_main_page.goToSite()
    hh_main_page.clickSearchButton()
    # Набор ввода:
    symbols = [' ', '_', '@=', '""', '!"№%"!)(*?:;', '1230', 'Job', 'Работка', '       Раб  ']

    # Для главной страницы:
    for x in range(9):
        hh_main_page.goToSite()
        hh_main_page.enterWord(symbols[x])
        hh_main_page.clickSearchButton()

    # Для страницы вакансий:
    for x in range(9):
        hh_main_page.clearSearchField()
        hh_main_page.enterWord(symbols[x])
        hh_main_page.clickSearchButton()


# Тест для положительного ввода на главной странице:
def test_hh_search(browser):
    hh_main_page = HhRuPages.SearchHelper(browser)
    hh_main_page.goToSite()
    hh_main_page.enterWord("Тестировщик python")
    hh_main_page.clickSearchButton()


# Если текущая страница - это страница с выводом вакансий, -
# выполнить тест на применение фильтра по з/п. Если нет -
# перейти к странице с вакансиями:
def test_hh_filter(browser):
    hh_second_page = HhRuPages.FilterHelper(browser)
    if "https://spb.hh.ru/search/vacancy" in hh_second_page.getUrl():
        hh_second_page.chooseMoneyLimit("high")
    else:
        hh_second_page.goToPage('https://spb.hh.ru/vacancies/testirovshik')
        hh_second_page.chooseMoneyLimit("high")


