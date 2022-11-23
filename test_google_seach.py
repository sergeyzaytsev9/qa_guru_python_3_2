from selene.support.shared import browser
from selene import be, have



def test_search_positive(open_browser):
    search_query_positive = 'selene'
    search_result_positive = 'yashaka/selene: User-oriented Web UI browser tests in Python'

    browser.element('[name="q"]').should(be.blank).type(search_query_positive).press_enter()
    browser.element('[id="search"]').should(have.text(search_result_positive))


def test_search_negative(open_browser):
    search_query_negative = 'dasdaffgbdshbvsdnfkdsf'
    search_result_negative = f'Your search - {search_query_negative} - did not match any documents.'

    browser.element('[name="q"]').should(be.blank).type(search_query_negative).press_enter()
    browser.element('[id="rcnt"]').should(have.text(search_result_negative))