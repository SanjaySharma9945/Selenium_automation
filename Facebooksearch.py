from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class FacebookLogin:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2 })
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        self.driver.maximize_window()
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.get("https://www.facebook.com/login/")
        sleep(1)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.search_input()
        sleep(30)
        self.close_browser()

    def enter_username(self, username):
        username_field = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        username_field.send_keys(username)
        sleep(1)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        password_field.send_keys(password)
        sleep(1)

    def click_login_button(self):
        login_button = self.driver.find_element(By.NAME, 'login')
        login_button.click()
        
    def search_input(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='search']"))
        )
        search_input = self.driver.find_element(By.XPATH, "//input[@type='search']")
        search_input.send_keys("Sanjay Sharma" + Keys.ENTER)
        
    def close_browser(self):
        self.driver.close()
        print("Closing the browser")

# Usage
if __name__ == "__main__":
    username = "sanjay9448116@gmail.com"
    password = "Sanj944811@9"

    facebook_login = FacebookLogin()
    facebook_login.login(username, password)
