from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from Inspect_Data import inspect_test_data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class Guvi:
    url="https://www.demoblaze.com/index.html"
    TIMEOUT=10
    @pytest.fixture(scope="module")
    def __init__(self,url):
        self.url=url
        #self.driver.implicitly_wait(5)
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.quit()
    #Test Case 1(Homepage Verification)
    def homepage_verify(self):
        self.driver.get(self.url)
        # Wait for the presence of a specific element on the page
        try:
            element_present=EC.presence_of_element_located(by=By.XPATH, value=Homepage.logo_xpath)
            WebDriverWait(driver, TIMEOUT).until(element_present)
            print("homepage loaded success")
        except TimeoutException:
            print("page not load")
        assert False

    #Test Case 2(Registration with valid data)
    def register(self):
        self.driver.get(self.url)
        self.driver.find_element(by=By.ID, value=Signup.signup_button).click()
        self.driver.find_element(by=By.ID, value=Signup.signup_username).send_keys("raj kumar")
        self.driver.find_element(by=By.ID, value=Signup.signup_password).send_keys("098765")
        self.driver.find_element(by=By.ID, value=Signup.signup_submit_button).click()
        # Wait for the confirmation  or element on the page
        try:
            confirmation= EC.text_to_be_present_in_element((by=By.ID, value=Signup.sign_submit_button)
            WebDriverWait(driver, TIMEOUT).until(confirmation)
            print("Registration successful!")
            assert True
        except TimeoutException:
            print("Timed out waiting for confirmation .")
            assert False
    #Test Case 3(User Login)
        def login(self):
            self.driver.get(self.url)
            self.driver.find_element(by=By.ID, value=Login.login_button).click()
            self.driver.find_element(by=By.ID, value=Login.login_usernam).send_keys("raj kumar")
            self.driver.find_element(by=By.ID, value=Login.login_password).send_keys("098765")
            self.driver.find_element(by=By.ID, value=Login.login_submit).click()
            # Wait for the  message or element on the page
            try:
                message = EC.text_to_be_present_in_element((by=By.ID, value=Login.login_submit)
                WebDriverWait(driver, TIMEOUT).until(message)
                print("Registration successful!")
                assert True
            except TimeoutException:
                print("Timed out waiting for  message.")
                assert False

        #Test Case 4(Product Selection and Cart Interaction)
        def product_selection(self):
            self.driver.get(self.url)
            self.driver.find_element(by=By.ID, value=category.select_phone).click()
            self.driver.find_element(by=By.XPATH, value=catgory.select_samsung).click()
            self.driver.find_element(by=By.XPATH, value=Category.select_add_cart).click()
            # Wait for the  message or element on the page
            try:
                verify = EC.text_to_be_present_in_element((by=By.XPATH, value=Category.select_add_cart)
                WebDriverWait(driver, TIMEOUT).until(verify)
                print("Registration successful!")
                assert True
            except TimeoutException:
                print("Timed out waiting for  verify.")
                assert False

        #Test Case 5(Placing an Order)
        def placing_order(self):
            self.driver.get(self.url)
            self.driver.find_element(by=By.XPATH, value=Cart.select_cart).click()
            self.driver.find_element(by=By.XPATH, value=Cart.select_plac_order).click()
            self.driver.find_element(by=By.ID, value=Cart.input_name).send_keys("raj kumar")
            self.driver.find_element(by=By.ID, value=Cart.input_country).send_keys("india")
            self.driver.find_element(by=By.ID, value=Cart.input_city).send_keys("goa")
            self.driver.find_element(by=By.ID, value=Cart.input_credit_card).send_keys("456781234509")
            self.driver.find_element(by=By.ID, value=Cart.input_month).send_keys("november")
            self.driver.find_element(by=By.ID, value=Cart.input_year).send_keys("2023")
            self.driver.find_element(by=By.XPATH, value=Cart.select_purchase).click()
            # Wait for the  message or element on the page
            try:
                verification = EC.text_to_be_present_in_element((by=By.XPATH, value=Cart.select_purchase)
                WebDriverWait(driver, TIMEOUT).until(verification)
                print("Registration successful!")
                assert True
            except TimeoutException:
                print("Timed out waiting for  verification.")
                assert False
        def Logout(self):
            self.driver.get(self.url)
            self.driver.find_element(by=By.ID, value=Logout.select_logout).click()
            # Wait for the presence of a specific element on the page
            try:
                element_present_homepage = EC.presence_of_element_located(by=By.XPATH, value=Homepage.logo_xpath)
                WebDriverWait(driver, TIMEOUT).until(element_present_homepage)
                print("homepage loaded success")
            except TimeoutException:
                print("page not load")
            assert False






