from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_field = driver.find_element(By.NAME, value="fName")
last_name_field = driver.find_element(By.NAME, value="lName")
email_field = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.TAG_NAME, value="button")

first_name_field.send_keys("Adi")
last_name_field.send_keys("Sak")
email_field.send_keys("email@gmail.com")
button.click()

