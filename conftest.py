import pytest
from selene.support.shared import browser

@pytest.fixture()
def set_window_size():
    browser.config.window_width = 1080
    browser.config.window_width = 920

@pytest.fixture()
def open_browser(set_window_size):
    base_url = 'https://google.com/ncr'
    browser.open(base_url)