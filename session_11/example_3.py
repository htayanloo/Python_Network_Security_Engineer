import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://divar.ir/s/tehran")
time.sleep(1)

search_bar = driver.find_element(By.CLASS_NAME, "kt-nav-text-field__input")

search_bar.send_keys('206')
search_bar.send_keys(Keys.RETURN)
time.sleep(15)

driver.quit()
