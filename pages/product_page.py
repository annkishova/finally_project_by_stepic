from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
  
    #Добавляем в корзину
    def add_to_basket(self):
        addToBasket = self.browser.find_element(*ProductPageLocators.Basket)
        addToBasket.click()    

    #Проверка что товар добавлен в корзину
    def should_be_product_on_page(self):
        assert self.is_element_present(*ProductPageLocators.Product_name), "Нет названия"
        assert self.is_element_present(*ProductPageLocators.Message_adding), "Сообщения нет"
        #получаем текст элементов проверки
        product_name = self.browser.find_element(*ProductPageLocators.Product_name)
        product_name_text = product_name.text
        message = self.browser.find_element(*ProductPageLocators.Message_adding)
        message_text = message.text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        assert product_name_text == message_text, "No no no product name in the message"
        
        
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

    def should_is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
       
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        
    