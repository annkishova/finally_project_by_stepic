from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    Login_email = (By.CSS_SELECTOR, "#id_login-username1")
    Login_password = (By.CSS_SELECTOR, "id_login-password1")
    Register_email = (By.CSS_SELECTOR, "[name='registration-email1']")
    Register_password = (By.CSS_SELECTOR, "id_registration-password11")
    Register_confirm_password = (By.CSS_SELECTOR, "id_registration-password21")

class ProductPageLocators():
    Product_price = (By.CSS_SELECTOR, ".product_main h1")
    Product_name = (By.CSS_SELECTOR, ".price_color")
    Basket = (By.CSS_SELECTOR, "#add_to_basket_form button")
    Message_adding = (By.CSS_SELECTOR, "div.alertinner")
    Basket_total = (By.CSS_SELECTOR, ".alert-info .alertinner strong")