from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('./chromedriver')
driver.get('https://kktix.com/')


driver.find_element(
    by=By.XPATH, value="//*[@id='navbar']/ul[2]/li[2]/a").click()

account = driver.find_element(
    by=By.XPATH, value="//*[@id='user_login']").click()
account.clear()
account.send_keys('account')

password = driver.find_element(
    by=By.XPATH, value="//*[@id='user_password']").click()
password.clear()
password.send_keys('password')

loginBtn = driver.find_element(
    by=By.XPATH, value="//*[@id='new_user']/input[3]").click()
loginBtn.click()

searchInput = driver.find_element(
    by=By.XPATH, value="//*[@id='navbar']/ul[1]/li[3]/form/input")
searchInput.clear()
searchInput.send_keys('超級圓頂')

driver.find_element(by=By.XPATH, value="//*[@id='new_user']/input[3]").click()
