from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url , "Нет ссылки на логин"        

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.Login_email), "Нет поля email login"
        assert self.is_element_present(*LoginPageLocators.Login_password), "Нет поля пароль login"
              

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.Register_email), "Нет поля email регистрация"
        assert self.is_element_present(*LoginPageLocators.Register_password), "Нет поля пароль регистрация"
        assert self.is_element_present(*LoginPageLocators.Register_confirm_password), "Нет поля подтверди пароль"
    
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.Register_email).send_keys(email)
        self.browser.find_element(*LoginPageLocators.Register_password).send_keys(password)
        self.browser.find_element(*LoginPageLocators.Register_confirm_password).send_keys(password)
        self.browser.find_element(*LoginPageLocators.Confirm_button).click()
        