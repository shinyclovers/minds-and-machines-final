import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time





player = input('are you player 1 or player 2 => ').strip()
player = int(player)



if player == 1:
    Options().add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install())    
    driver.get('https://connect-4.org/en')
    driver.find_element(By.XPATH,'//button[@class=\'mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent ng-tns-c23-0\']').click()



    element_present = EC.presence_of_element_located((By.XPATH,'//input[@id=\'invitionLinkInput2\']'))
    
    # WebDriverWait(driver, 10).until(element_present)


    name = driver.find_element(By.XPATH,'//input[@id=\'invitionLinkInput2\']')
    # print(EC.visibility_of(driver.find_element(By.XPATH,'//input[@id=\'invitionLinkInput2\']')))
    name.send_keys('playerOne')
    # print('name = ',name)
if player == 2:
    website = input('enter code provided by opponent(?lb) => ')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10) # seconds
    driver.get('http://connect-4.org/?lb'+website.strip())
  
    EC.visibility_of_element_located(driver.find_element(By.XPATH,'//div[@class=\'ng-tns-c25-1\']'))

finalBox = driver.find_element(By.XPATH,'//div[@class="ng-tns-c25-1"]')
while True:
    pass