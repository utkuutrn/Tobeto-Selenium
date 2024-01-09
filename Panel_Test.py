from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from constants import globalConstants as c

class Test_tobetoPlatformLogin():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_visibility_of_login_page(self):
    
        #1- "Giriş Yap" butonu, "Şifremi Unuttum" bağlantısı, "Henüz Üye Değil misin? Kayıt Ol" bağlantısı alanlarını kontrol et.
        tobeto_img = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, c.Tobeto_Logo_XPATH)))
        email_input = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, c.EMAIL_XPATH)))
        password_input = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, c.PASSWORD_XPATH)))
        login_button = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, c.LOGIN_BUTTON_XPATH)))
        forgot_password_link = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, c.FORGOT_PASSWORD_XPATH)))
        sign_up_link = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, c.REGISTER_XPATH)))

        
        assert tobeto_img.is_displayed()
        assert email_input.is_displayed()
        assert password_input.is_displayed()
        assert login_button.is_displayed()
        assert forgot_password_link.is_displayed()
        assert sign_up_link.is_displayed()
        assert sign_up_link.text == "Kayıt Ol"
    def teardown_method(self):
        self.driver.quit()
     #2-Başarılı giriş.
    def test_successful_login(self):
        
        email_input = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, c.EMAIL_XPATH)))
        email_input.send_keys("johiked454@telvetto.com")

        password_input = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, c.PASSWORD_XPATH)))
        password_input.send_keys("basariligiris")

        login_button = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.XPATH, c.LOGIN_BUTTON_XPATH)))
        login_button.click()

        dashboard_title = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.XPATH, c.SYSTEM_MESSAGE_XPATH)))
        assert dashboard_title.is_displayed()
    
    def teardown_method(self):
        self.driver.quit()
     #3-Boş bırakıp test et.
    @pytest.mark.parametrize("email_input, password_input", [ ("test@test.com", ""), ("", "sifretest"), ("", "") ])
    def test_empty_input_login(self, email_input, password_input):
        
        email_input_box = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, c.EMAIL_XPATH)))
        email_input_box.send_keys(email_input)

        password_input_box = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, c.PASSWORD_XPATH)))
        password_input_box.send_keys(password_input)

        login_button = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, c.LOGIN_BUTTON_XPATH)))
        login_button.click()

        error_message = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, c.MESSAGE_Error_XPATH)))
        assert error_message.text == "Doldurulması zorunlu alan*"