# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        print(f'Bot is navigating toward: twitter index page')
        wait = WebDriverWait(bot, 20)
        try:
            # Sign in button finder by Class_Name & click
            loginpage = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'StaticLoggedOutHomePage-buttonLogin'))).click()
            print('Made it to login page')
            time.sleep(6)
            # Email & username input field finder by XPATH
            email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')))
            # Password input field finder by XPATH
            password = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')))
            email.clear()
            password.clear()
            email.send_keys(self.username)
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(3)
        except Exception as error:
            print('Error: Something was not succesfull')
            time.sleep(3)
            print(f'Error {error}')
            bot.quit()

    def like_tweets(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        wait = WebDriverWait(bot, 6)
        time.sleep(3)
        try:
            for i in range(1,10):
                bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                time.sleep(2)
                tweets = wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'tweet')))
                links = [elem.get_attribute('data-permalink-path') for elem in tweets]
                # print(links)
                for link in links:
                    bot.get('https://twitter.com' + link)
                    try:
                        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'HeartAnimation'))).click()
                        print('Liked a tweet')
                        time.sleep(10)
                    except Exception as error:
                        time.sleep(60)
                        print(error)
        except Exception as error:
            print('Error: Like tweets has encountered an error')
            time.sleep(2)
            print(error)
            bot.quit()


car = TwitterBot('Username', 'Password') #TwitterBot takes the username and password ('username', 'password')
car.login()
car.like_tweets('Hashtag') # like_tweets takes the hashtag ('hashtag')