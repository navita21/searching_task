import pytest
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="class")
def launch_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com/")
        yield page
        browser.close()