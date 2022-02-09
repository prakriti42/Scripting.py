'''
    Written By : Prakriti Regmi 
    Written On : 9th Feb, 2022
    Description : This is a python script to log into my personal messenger profile and send a message.
'''


#Necessary Libraries 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

#Indicating the location for my chrome driver path
driverpath = "C:/Users/Prakriti/Downloads/chromedriver_win32/chromedriver.exe"


#Setting Up The WebDriver for my browser 
s = Service(driverpath)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=driverpath)
driver.maximize_window()


#Opening the Messenger page
driver.get("https://www.messenger.com/")

#Scrolling down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)



#Fetching and writing on the target Fields for logging in
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
username.clear()
username.send_keys("regmi.prakriti24@gmail.com")


#Fetching and writing on the target Fields for logging in
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
password.clear()
password.send_keys("YourPassword")


#fetching the login button and clicking it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()



##Searching the Contact I want to message
search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='Search Messenger']")))
search.clear()
search.send_keys("Prakriti Regmi")
time.sleep(5)

#fetching the top most search result and clicking it
try : 
    first_result = driver.find_element(By.XPATH,"//ul[@role=\"listbox\"]/li[1]/ul/li[2]").click()
except NoSuchElementException:
    print("Element Not Found")

#fetching the message box for the selected conversation and writing the message
messageBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label=\"Message\"]")))
messageBox.send_keys("Hello, This was a message sent through a script")

#Sending the message
messageBox.send_keys(Keys.ENTER)


'''
    VOILA! Message sent successfully :)
'''
