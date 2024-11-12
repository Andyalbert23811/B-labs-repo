from selenium.webdriver.common.by import By
from helpers.base_page import BasePage


class ProductPage(BasePage):
    Add_To_Cart_Button = (By.ID, 'product-addtocart-button')
    Navigate_to_Cart = (By.XPATH, '//*[@class="btn-common btn-regular medium super go-to-cart-btn"]')


    def click_add_to_cart(self):
        self.click_element(self.Add_To_Cart_Button)

    def navigate_to_cart(self):
        self.click_element(self.Navigate_to_Cart)