from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time


# BIRTHDAY GREETINGS


# options=webdriver.ChromeOptions()
# options.add_argument(CHROME_PROFILE_PATH)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# webdriver.Chrome(options=options)

now = datetime.now()
currtime = now.strftime("%H:%M")
currdate=now.strftime("%d/%m")
birthdates={"vaibhav": "16/09",
    "sanchit": "16/08",
    "nikshat": "13/10",
    "shashank": "16/09",
    "bhuvan": "20/01",
    "sumit": "25/03"}
# if(currtime=="00:00"):
for key in birthdates:
        if(birthdates[key]==currdate):
            driver.get("https://web.whatsapp.com/")
            time.sleep(30)
            searchbar=driver.find_element("xpath","//*[@id='side']/div[1]/div/div/div[2]/div/div[2]")
            searchbar.click()
            searchbar.send_keys(key)
            searchbar.send_keys(Keys.ENTER)
            time.sleep(8)
            typing=driver.find_element("xpath","//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
            typing.click()
            typing.send_keys("Wish you a very happy birthday my dear friend"+key+"!!")
            typing.send_keys(Keys.ENTER)
            time.sleep(8)
            driver.close()



# AMAZON PRODUCT PRICE AUTOMATION


while(1):
    time.sleep(3600)
    driver.get("https://www.amazon.in/Atomic-Habits-James-Clear/dp/1847941834/ref=pd_bxgy_img_sccl_2/261-7757450-4225401?pd_rd_w=V4TU6&content-id=amzn1.sym.d68c4347-8b80-4998-9474-4671a1e32e96&pf_rd_p=d68c4347-8b80-4998-9474-4671a1e32e96&pf_rd_r=R2ZVN0CHWYS35GY04FFG&pd_rd_wg=eioSQ&pd_rd_r=c5d49501-b8de-4b21-8e3c-b67533270db0&pd_rd_i=1847941834&psc=1")
    time.sleep(5)
    price=driver.find_element("xpath","//*[@id='price']")
    if((int(price.text[1:3]))<300):
            print("The product is now in your budget!!")
            break
    else:
        print("Still not in your budget. Check back after one hour!!")
    break
driver.quit()
