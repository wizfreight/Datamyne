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
time.sleep(20)
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
time.sleep(10)
date_selection = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="page-wrapper"]/div[1]/div/div[2]/div[1]/div/div')))
calendar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="page-wrapper"]/div[1]/div/div[2]/div[1]/div/div/span[1]'))).click()
date_range = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="htmlPageBody"]/div[6]/div[3]')))
last_year = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="htmlPageBody"]/div[6]/div[3]/ul[1]/li[3]'))).click()
apply = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="page-wrapper"]/div[1]/div/div[2]/div[1]/div/div/span[2]/button')))
apply.click()
time.sleep(30)
inputFile = 'number_range_inputs.xlsx'
inputs = pd.read_excel(inputFile)
from_record = inputs.From_Record.dropna()
print(from_record)
to_record = inputs.To_Record.dropna()
print(to_record)

i=1
while True:
    data = zip(from_record, to_record)
    for f, t in data:
        from_record = f
        to_record = t
        row_group = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.ID, "containerResult")))
        row_ = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "box-btn-actions")))
        walkthrough = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "walkthrough_step_8")))
        btnexcel = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="btnExcel"]/button[1]'))).click()
        modal_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="htmlPageBody"]/div[8]')))
        record_range = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="excelDialog"]/div[3]/div[3]')))
        # from_record = input('enter the record range : ')
        start_range = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="dd_startRangeE"]')))
        start_range.send_keys(from_record)
        # to_record = input('enter the record range : ')
        end_range = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="dd_endRangeE"]')))
        end_range.send_keys(to_record)
        on_screen = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="excelDialog"]/div[3]/div[2]')))
        reocrd_range_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="radioToExportRange"]'))).click()
        der = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="htmlPageBody"]/div[7]/div[3]/div')))
        download = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="htmlPageBody"]/div[7]/div[3]/div/button[2]')))
        download.click()
        time.sleep(80)
        i = i + 1






