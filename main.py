import csv
import time

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
driver.implicitly_wait(5)
time.sleep(200)
while True:
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
    from_record = input('enter the record range : ')
    start_range = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="dd_startRangeE"]')))
    start_range.send_keys(from_record)
    to_record = input('enter the record range : ')
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
    driver.refresh()
    time.sleep(50)

