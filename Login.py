from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser
#from selenium.common.exceptions import TimeoutException

#read the url, username, password from settings.ini file
parser = ConfigParser()
parser.read('settings.ini')
url = parser.get('info', 'url')
id = parser.get('info', 'username')
pwd = parser.get('info', 'password')

#initialize chrome driver and open the required URL
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

#find elements or wait for 10 seconds if not found
username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "un"))
    )
username.send_keys(id)
password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pw"))
    )
password.send_keys(pwd)
signin_btn = driver.find_element(By.CLASS_NAME("btn primary"))

'''
username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "i0116"))
    )
next_btn = driver.find_element_by_id("idSIButton9")

username.send_keys(id)
next_btn.click()

password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwordInput"))
    )
signin_btn = driver.find_element_by_id("submitButton")

password.send_keys(pwd)
signin_btn.click()
'''
driver.implicitly_wait(5)

assert driver.title("")