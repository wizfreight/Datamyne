import csv
import time

import pandas as pd
import undetected_chromedriver as uc
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

s = Service(r'C:\Users\Bindu\PycharmProjects\big_schedules\chromedriver.exe')
driver = uc.Chrome(service=s)
driver.maximize_window()
url = 'https://threezero.datamyne.com/system/jsp/login.jsp'
driver.get(url)
driver.implicitly_wait(5)
username = driver.find_element(By.XPATH, '//*[@id="UserName"]')
username.send_keys("mrforw4")
next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="UsernameNext"]')))
next.click()
password = driver.find_element(By.XPATH, '//*[@id="Password"]')
password.send_keys("indiamr2022")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="Login"]'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH,
     '//*[@id="skipNow"]'))).click()
driver.implicitly_wait(20)
leftpanel = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="leftNavBar"]')))
sidemenu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="side-menu"]/ul[1]/li[8]')))
seemore = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="side-menu"]/ul[1]/li[8]/ul/li[6]/a'))).click()
modal_box_countries = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="htmlPageBody"]/div[7]')))
# list_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
#             (By.XPATH,'//*[@id="htmlPageBody"]/div[7]/div[2]/div/div[2]/div/div/div/div[1]/ul')))
countries_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterTag"]')))
countries_name.send_keys(input('enter country name '))
countries_name.click()
# drop_down =WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,' //*[@id="htmlPageBody"]/div[7]/div[2]/div/div[2]/div/span/span')))
selection = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="htmlPageBody"]/div[7]/div[2]/div/div[2]/div/span/span/div')))
selection.click()
# action = ActionChains(driver)
# # double click operation and perform
# action.double_click(drop_down).perform()
Add = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="htmlPageBody"]/div[7]/div[2]/div/div[3]/button[2]')))
Add.click()
date_selection = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="page-wrapper"]/div[1]/div/div[2]/div[1]/div/div')))
calendar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="page-wrapper"]/div[1]/div/div[2]/div[1]/div/div/span[1]'))).click()
date_range = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="htmlPageBody"]/div[6]/div[3]')))
select = Select(driver.find_element(By.CLASS_NAME, 'yearsRange'))
select.select_by_value('2022')
apply = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="htmlPageBody"]/div[6]/div[3]/div/button[1]')))
apply.click()

time.sleep(50)
print('loaded')
row_group = driver.find_elements(By.XPATH, '//*[@id="resultTable"]/div[1]/table/tbody')
# header = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
#     (By.XPATH, '//*[@id="resultTable"]/div[1]/table/thead/tr')))
pagination = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="DataTables_Table_0_paginate"]/ul')))
time.sleep(0.2)
pageSize = int(driver.find_element(By.XPATH,
                                   "//ul[@class='pagination']//following-sibling::li[7]").text);

with open('mango.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, delimiter=',', skipinitialspace=True)

    for row in row_group.find_elements(By.CSS_SELECTOR, 'tr'):
        wr.writerow([d.text for d in row.find_elements(By.CSS_SELECTOR, 'td')])
        print(f"Processing page ..")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Next"))).click()
    print('clicked')



