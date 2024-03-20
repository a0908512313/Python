from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("./chromedriver.exe")
driver.get(
    'https://www.facebook.com/pokes/?notif_id=1710471352752598&notif_t=poke&ref=notif')

WebDriverWait(driver, 60, 1).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[aria-label='戳回去']")
    ), "找不到指定的元素")

driver.find_element(
    By.CSS_SELECTOR, "[aria-label='戳回去']").click()
