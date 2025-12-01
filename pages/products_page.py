from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductsPage (BasePage):
    product_title = (By.ID, 'item_4_title_link')
    add_to_cart_button = (By.ID, 'add-to-cart-sauce-labs-backpack')

    def getProductTitle(self):
        return self.get_text(*self.product_title)
    
    def addProduct(self):
        self.click(*self.add_to_cart_button)