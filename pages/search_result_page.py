from selenium.webdriver.common.by import By
from helpers.base_page import BasePage


class ResultsPage(BasePage):
    First_item = (By.XPATH, "(//*[@class='listingWrapperSection'])[1]")
    Image = (By.XPATH, "(//*[@class='listingWrapperSection'])[1]//img")

    def click_first_item(self):
        self.click_element(self.First_item)

    def is_element_displayed(self):
        element = self.find_element(self.Image)
        return element.is_displayed()

