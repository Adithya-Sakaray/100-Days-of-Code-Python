from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/")

username_field = driver.find_element(By.NAME, value="session_key")
password_field = driver.find_element(By.NAME, value="session_password")
signin_button = driver.find_element(By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')

username_field.send_keys("adithyasakaray@gmail.com")
password_field.send_keys("Sopada123linkedin")
signin_button.click()

sleep(5)

job_tab = driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]/a')
job_tab.click()

sleep(3)

show_all_button = driver.find_element(By.CLASS_NAME, value="discovery-templates-vertical-list__footer")
show_all_button.click()

sleep(3)

list_of_jobs = driver.find_elements(By.CSS_SELECTOR, value=".scaffold-layout__list-container li")

number_of_jobs = len(list_of_jobs)
#
# for i in range(3):
#     list_of_jobs[i].click()
#     print(list_of_jobs[i].get_attribute("id"))
#     sleep(1)

for i in range(number_of_jobs):
    element_id = list_of_jobs[i].get_attribute("id")
    if "ember" in element_id:
        list_of_jobs[i].click()
        sleep(1)
        save_button = driver.find_element(By.CLASS_NAME, value="jobs-save-button")
        print(save_button.tag_name)
        save_button.click()
        sleep(1)


