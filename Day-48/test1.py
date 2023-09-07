from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# no_of_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

search = driver.find_element(By.NAME, value="search")

search.send_keys("Python")
search.send_keys(Keys.ENTER)
search.send_keys(Keys.ENTER)
