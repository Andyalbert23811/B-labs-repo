from selenium.webdriver.common.by import By
from helpers.base_page import BasePage


class HomePage(BasePage):
    Search_field = (By.ID, "search")
    Search_button = (By.XPATH, '//*[@type="submit"]')

    def fill_search_bar(self, value):
        self.enter_text(self.Search_field, value)

    def click_search_button(self):
        self.click_element(self.Search_button)
