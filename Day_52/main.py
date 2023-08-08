from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH=""
INSTA_USERNAME="My username"
INSTA_PASSWORD="My password"
SIMILAR_ACCOUNT="Name of an account"

class InstaFollower:
    def __init(self,driver_path):
        self.driver=webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        email=self.driver.find_element_by_name("username")
        email.send_keys(INSTA_USERNAME)
        password=self.driver.find_element_by_name("password")
        password.send_keys(INSTA_PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        time.sleep(5)
        follow_button=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follow_button.click()

        time.sleep(5)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot=InstaFollower(CHROME_DRIVER_PATH)

bot.login()
bot.find_followers()
bot.follow()

