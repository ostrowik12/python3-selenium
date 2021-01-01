from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import numpy as np

driver = webdriver.Chrome()
driver.maximize_window()
data_path = 'csv/data.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    data = np.array(list(reader))
driver.get(data[0, 0])
# driver.implicitly_wait(15)
try:
    #    WebDriverWait(driver, 15).until(
    # EC.presence_of_element_located((driver.find_element_by_xpath('//*[@class="authorization-link"]')))
    #        EC.element_to_be_clickable('//*[@class="authorization-link"]')
    driver.implicitly_wait(15)

finally:

    driver.find_element_by_xpath('//*[@class="authorization-link"]').click()
login = driver.find_element_by_xpath('//*[@id="email"]')
login.send_keys(data[0, 1])
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys(data[0, 2])
driver.find_element_by_xpath('//*[@id="send2"]').click()
