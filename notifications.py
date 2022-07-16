from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver=webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)
driver.get("https://www.nitj.ac.in/")
driver.maximize_window()
driver.find_element("xpath","/html/body/div[1]/div/div[3]/div[1]/div[1]/div[3]/div/div/div/div/div/ul/li[2]/a/b").click()
# driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[1]/div[3]/div/div/div/div/div/ul/li[2]/a/b").click()
time.sleep(3)
b=(driver.find_element("xpath","//*[@id='section-2']/ul/li[1]/a"))
# b=(driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/ul/li[1]/a/b[1]").is_displayed())
time.sleep(3)
c=b.text
driver.quit()

# Below script checks for a new notification on our college website after every one hour

while(1):
    time.sleep(3600)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.nitj.ac.in/")
    driver.maximize_window()
    driver.find_element("xpath","/html/body/div[1]/div/div[3]/div[1]/div[1]/div[3]/div/div/div/div/div/ul/li[2]/a/b").click()
    # driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[1]/div[3]/div/div/div/div/div/ul/li[2]/a/b").click()
    time.sleep(3)
    b=(driver.find_element("xpath","//*[@id='section-2']/ul/li[1]/a"))
    # b=(driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/ul/li[1]/a/b[1]").is_displayed())
    time.sleep(3)
    if(b.text==c):
        print("No new notification is there!!")
    else:
        c=b.text
        print("You got a new notification!!"+c)
        time.sleep(5)
    driver.quit()

    
