from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import random
from time import sleep

driver = webdriver.Edge("auto_fill_form\driver\msedgedriver.exe")

url = "https://forms.office.com/pages/responsepage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAO__VIr16pUOFE5SzVWS0hCUUc3RkpZUFBLM09VQUcwTy4u&fbclid=IwAR36fJU59hCiBOJknN3_Odr3gCsHwCqcXyLRew8XVTKCQTxYuAswVHi5LA8"

driver.get(url)
sleep(8)

# start_now = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-main-content1"]/div/div[4]/button')))
# start_now.click()

script = "document.querySelector('#form-main-content1 .css-119 button').click();"
driver.execute_script(script)

def fill_form(name, email):
    pass

    # another_response = driver.find_element_by_xpath('//*[@id="form-main-content1"]/div/div/div[2]/div[2]/div[2]/a')

fill_form("Phan Dinh Son", "phandinhsonntgb@gmail.com")