from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

 
def test_guest_can_add_product_to_basket(browser):
    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    #запоминаем цену
    Product_page = ProductPage(browser, browser.current_url)
    Product_page.should_be_promo_url()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_on_page() 
    page.should_be_checked_order()
    #проверка цены корзины с ценой товара
    