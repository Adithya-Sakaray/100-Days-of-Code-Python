import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class TwitterManager():

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self, username, password, email):
        self.driver.get("https://twitter.com/")

        time.sleep(3)

        sign_in_button = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a")
        sign_in_button.click()

        time.sleep(3)
        username_field = self.driver.find_element(by=By.NAME, value="text")
        username_field.send_keys(email)

        next_button = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        next_button.click()

        time.sleep(2)
        name_field = self.driver.find_element(by=By.NAME, value="text")
        name_field.send_keys(username)

        next_button_1 = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div")
        next_button_1.click()


        time.sleep(1)
        password_field = self.driver.find_element(by=By.NAME, value="password")
        password_field.send_keys(password)

        login_button = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div")
        login_button.click()

        print("Done")

    def tweet(self, message):
        time.sleep(8)

        tweet_field = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet_field.click()

        tweet_field_active = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet_field_active.send_keys(message)

        post_button = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span")
        post_button.click()

        print("Posted")




