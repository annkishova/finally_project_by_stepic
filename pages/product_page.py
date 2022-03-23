from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators



class ProductPage(BasePage):
    #def should_be_can_add_product_to_basket(self):
        #self.should_be_promo_url()
     #   self.add_to_basket()
      #  self.should_be_product_on_page()
       # self.should_be_checked_order()
      

    #def should_be_promo_url(self):
        #current_url = self.browser.current_url
        #assert "?promo=newYear" in current_url , "Нет промо"
        # реализуйте проверку на корректный url адрес
    
    #Добавляем в корзину
    def add_to_basket(self):
        #assert self.is_element_present(*ProductPageLocators.Product_price), "Нет стоимости"
        addToBasket = self.browser.find_element(*ProductPageLocators.Basket)
        addToBasket.click()    

    #Проверка что товар добавлен в корзину
    def should_be_product_on_page(self):
        #assert self.is_element_present(*ProductPageLocators.Product_price), "Нет стоимости"
        assert self.is_element_present(*ProductPageLocators.Product_name), "Нет названия"
        assert self.is_element_present(*ProductPageLocators.Message_adding), "Сообщения нет"
        #получаем текст элементов проверки
        product_name = self.browser.find_element(*ProductPageLocators.Product_name)
        product_name_text = product_name.text
        message = self.browser.find_element(*ProductPageLocators.Message_adding)
        message_text = message.text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert product_name_text == message_text, "No no no product name in the message"
        # реализуйте проверку, что есть товар и цена
        
        #Проверка цены товара в корзине
    def should_be_checked_order_price(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.Basket_total), "Message basket total is not presented"
        assert self.is_element_present(*ProductPageLocators.Product_price), "Product price is not presented"
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.Basket_total).text
        product_price = self.browser.find_element(*ProductPageLocators.Product_price).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price == message_basket_total, "No product price in the message"
       
        
    