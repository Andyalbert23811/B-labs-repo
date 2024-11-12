import pytest
import allure
from selenium import webdriver
from pages import home_page, search_result_page, product_page

@allure.feature('Add to Cart')
class TestAddToCart:
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://btech.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('Search and Add to Cart')
    def test_search_valid_keyword(self):
        with allure.step('Fill search bar and click search button'):
            homePages = home_page.HomePage(self.driver)
            homePages.fill_search_bar("iphone15")
            homePages.click_search_button()

        with allure.step('Locate image and click first item'):
            searchResult = search_result_page.ResultsPage(self.driver)
            assert searchResult.is_element_displayed(), "Element is not displayed"
            searchResult.click_first_item()

        with allure.step('Add to cart and navigate to cart'):
            productPage = product_page.ProductPage(self.driver)
            productPage.click_add_to_cart()
            productPage.navigate_to_cart()

    def teardown_method(self, method):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main()