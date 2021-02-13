# import selenium,time & urllib modules
# import time
# import urllib.request
# import os
# import wget
from instaclient import InstaClient
from instaclient.errors.common import *

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# launch Chrome and navigate to Instagram page
driver = webdriver.Chrome("C:/webdrivers/chromedriver_win32/chromedriver.exe")
driver.get("https://www.instagram.com")

username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

username.send_keys("larm_bee")
password.send_keys("Brandonkanute1@")

log_in = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']"))).click()
not_now = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Not Now')]"))).click()

searchbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
keyword = "larm_bee"
searchbox.send_keys(keyword)
searchbox.send_keys(Keys.ENTER)

first_result = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, '-qQT3')))
first_result.click()

# followers = driver.find_element_by_class_name('g47SY')
no_of_posts = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'g47SY')))
print('Posts: ' + no_of_posts.text)

followers = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span"
    )))

print('Followers: ' + followers.text)

following = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.XPATH,
        "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span"
    )))

print('Following: ' + following.text)

driver.quit()