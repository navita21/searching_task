import pytest
from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def search(self):
        search_bar = self.page.locator('//*[@id="APjFqb"]')
        
        if search_bar.is_visible():
            # Fill the search bar with the query
            search_bar.fill("keyboard")
            
            # Click the first "Google Search" button
            google_search = self.page.get_by_label("Google Search").first
            google_search.click()
            
            # Wait for the search results to load
            self.page.wait_for_load_state('networkidle')
            self.page.wait_for_selector('h3')
            
            # Get the first 10 search results
            results = self.page.locator('h3').all_text_contents()[:10]
            
            # Print and write the results
            self._print_and_write_results(results)
            return True
        
        return False

    def _print_and_write_results(self, results: list):
        """Prints and writes the search results to a text file."""
        
        with open("search_results.txt", "w") as file:
            for idx, result in enumerate(results, start=1):
                output = f"{idx}. {result}"
                print(output)
                file.write(output + "\n")
