from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep



class InstaManager:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/")

        sleep(3)

        username_field = self.driver.find_element(By.NAME, value="username")
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.NAME, value="password")
        password_field.send_keys(password)

        password_field.send_keys(Keys.ENTER)

        sleep(5)
        not_now = self.driver.find_element(By.CLASS_NAME, 'x1yc6y37')
        not_now.click()

        not_now2 = self.driver.find_element(By.CLASS_NAME, '_a9_1')
        not_now2.click()

    def find_followers(self, query):
        sleep(3)
        search = self.driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]')
        search.click()
        sleep(2)
        search_input = self.driver.find_element(By.CLASS_NAME, 'x7xwk5j')
        search_input.send_keys('chefsteps')
        search_input.send_keys(Keys.ENTER)
        sleep(3)
        chef = self.driver.find_element(By.XPATH,
                                        '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div')
        chef.click()
        sleep(5)
        followers = self.driver.find_elements(By.TAG_NAME, "li")
        followers[1].click()
        sleep(3)
        click_follow = self.driver.find_elements(By.CLASS_NAME, '_acas')
        count = 1
        for i in range(3):
            sleep(3)
            click_follow[count].send_keys(Keys.ENTER)
            count += 1


