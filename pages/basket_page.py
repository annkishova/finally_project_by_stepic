from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators
from .locators import BasketPageLocators



class BasketPage(BasePage):

    def should_be_empty_basket(self):      
        assert self.is_element_present(*BasketPageLocators.Busket_empty_text), "Нет текста о пустой корзине"
        assert self.is_not_element_present(*BasketPageLocators.Not_product), "В корзине есть товары"
        
        