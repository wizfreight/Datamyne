import csv
import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


s = Service(r'C:\Users\Bindu\PycharmProjects\big_schedules\chromedriver.exe')
driver = uc.Chrome(service=s)
driver.maximize_window()
url = 'https://threezero.datamyne.com/system/jsp/login.jsp'
url_2 = 'https://threezero.datamyne.com/frontend/loadSearchForm.thyme?appId=44&ticket=776e3b8f:185d616c981:-7a43'
driver.get(url)
username = driver.find_element(By.XPATH, '//*[@id="loginForm"]/fieldset/div[1]/input')
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/fieldset/div[2]/input')
username.send_keys("mrforw4")
password.send_keys("indiamr2022")
driver.find_element(By.XPATH, '//*[@id="loginForm"]/fieldset/a').click()
driver.implicitly_wait(5)
time.sleep(20)
row_group = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.ID, "containerResult")))
pagination = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.ID,'DataTables_Table_0_paginate')))
pagination_ul = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CLASS_NAME,'pagination')))
all_rows=[]
with open('', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile, delimiter=',', skipinitialspace=True)
    # wr.writerow(header)
for row in row_group.find_elements(By.CSS_SELECTOR, 'tr.odd, tr.even'):
        worksheet.write([d.text for d in row.find_elements(By.CSS_SELECTOR, 'td')])






