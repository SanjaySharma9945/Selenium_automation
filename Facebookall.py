from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class FacebookLogin:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.get("https://www.facebook.com/login/")
        sleep(1)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.select_photo()
        self.write_post()
        self.click_on_post()
        self.click_on_profile()
        self.logout()
        sleep(30)
        self.close_browser()

    def enter_username(self, username):
        username_field = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.NAME, 'login')
        login_button.click()

    def select_photo(self):
        create_post_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]'))
        )
        create_post_button.click()

    def write_post(self):
        post_text_field = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]'))
        )
        post_text_field.send_keys("Hi, How are you??")

    def click_on_post(self):
        click_on_post = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div'))
        )
        click_on_post.submit()

    def click_on_profile(self):
        click_on_profile = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div/div[1]')))
        click_on_profile = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/span/div/div[1]')
        click_on_profile.click()
        sleep(10)

    def logout(self):
        logout = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[5]/div/div[1]/div[2]')))
        logout = self.driver.find_element(By.XPATH,
                                          '/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[5]/div/div[1]/div[2]')
        logout.click()

    def close_browser(self):
        self.driver.close()
        print("Closing the browser")


# Usage
if __name__ == "__main__":
    username = "sanjay9448116@gmail.com"
    password = "Sanj944811@9"

    facebook_login = FacebookLogin()
    facebook_login.login(username, password)
