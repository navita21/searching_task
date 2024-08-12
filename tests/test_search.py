from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
import pytest
from search import MainPage

class TestGoogle:
    def test_launch(self, launch_google):
        page=launch_google
        main_page = MainPage(page)
        assert main_page.search()