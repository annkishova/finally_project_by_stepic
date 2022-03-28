from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") 
    Basket_button = (By.CSS_SELECTOR, ".btn-group a.btn-default")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    Login_email = (By.CSS_SELECTOR, "#id_login-username")
    Login_password = (By.CSS_SELECTOR, "#id_login-password")
    Register_email = (By.CSS_SELECTOR, "[name='registration-email']")
    Register_password = (By.CSS_SELECTOR, "#id_registration-password1")
    Register_confirm_password = (By.CSS_SELECTOR, "#id_registration-password2")

class ProductPageLocators():
    Product_price = (By.CSS_SELECTOR, ".product_main .price_color")
    Product_name = (By.CSS_SELECTOR, ".product_main h1")
    Basket = (By.CSS_SELECTOR, "#add_to_basket_form button")
    Message_adding = (By.CSS_SELECTOR, ".alertinner strong")
    Basket_total = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class BasketPageLocators():
    Busket_empty_text = (By.CSS_SELECTOR, "#content_inner [href='/en-gb/']")
    Not_product = (By.CSS_SELECTOR, "#basket_formset") 
    