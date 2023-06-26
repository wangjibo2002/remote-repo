from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https:\\www.zte.com.cn")
element = browser.find_element(By.CSS_SELECTOR,'span')
print(element.get_attribute('class'))
frame = browser.find_elements(By.CSS_SELECTOR,'.text-input')
for i in frame:
    print(i.text)