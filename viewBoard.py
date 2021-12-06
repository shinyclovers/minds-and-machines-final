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

Options().add_experimental_option("detach", True)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(60) # seconds  

if player == 1:
    driver.get('https://connect-4.org/en')
    driver.find_element(By.XPATH,'//button[@class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent ng-tns-c23-0"]').click()
    # element_present = EC.presence_of_element_located((By.XPATH,'//input[@id="invitionLinkInput2"]'))
    # WebDriverWait(driver, 10).until(element_present)
    name = driver.find_element(By.XPATH,'//input[@id="invitionLinkInput2"]')
    # print(EC.visibility_of(driver.find_element(By.XPATH,'//input[@id="invitionLinkInput2"]')))
    name.send_keys('Bram vs John')
    # print('name = ',name)
elif player == 2:
    website = input('enter code provided by opponent(?lb) => ')
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.implicitly_wait(60) # seconds
    driver.get('http://connect-4.org/?lb'+website.strip())
  
    EC.visibility_of_element_located(driver.find_element(By.XPATH,'//div[@class="ng-tns-c25-1"]'))
elif player == 0:
    # Options().add_experimental_option("detach", True)
    # driver = webdriver.Chrome(ChromeDriverManager().install())  
    # driver.implicitly_wait(60) # seconds  
    driver.get('https://connect-4.org/en')
    driver.find_element(By.XPATH,'//button[@class="mdl-button mdl-js-button mdl-js-ripple-effect mdl-button--raised mdl-button--accent ng-tns-c23-0"]').click()



    # element_present = EC.presence_of_element_located((By.XPATH,'//input[@id="invitionLinkInput2"]'))
    
    # WebDriverWait(driver, 10).until(element_present)


    # name = driver.find_element(By.XPATH,'//input[@id="invitionLinkInput2"]')
    # print(EC.visibility_of(driver.find_element(By.XPATH,'//input[@id="invitionLinkInput2"]')))
    # name.send_keys('Bram vs John')
    # print('name = ',name)
# print('gets here 59')

def checkGameState():
    endGameText=driver.find_element(By.XPATH,'//app-game-end//mat-card-content//p').get_attribute('class')
    if 'winnerText' in endGameText or 'loserText' in endGameText:
        gameOver = True
    else:
        gameOver = False
    if gameOver:
        driver.quit()
def getBoardState():
        table = driver.find_elements(By.XPATH,'//tr[@class="ng-star-inserted"]')
        columns = len(table)
        boardList = []
        for col in range(7):
            appendList = []
            for row in range(6):
                div = driver.find_element(By.XPATH,'//table/tr[{}]/td[{}]/div'.format(col+1,row+1))
                style = div.get_attribute('style')
                # print(style)
                red = 'red'
                blue = 'blue'
                # print(blue in style,red in style)
                if blue in str(style):
                    appendList.append('1')
                elif red in str(style):
                    appendList.append('2')
                else:
                    appendList.append('0')
            boardList.append(sorted(appendList,reverse=True))
        return boardList
def selectcol(num):
    driver.find_element(By.XPATH,'//table/tr[-1]/td[{}]'.format(num)).click()
def isBrowserAlive():
   try:
      driver.current_url
      # or driver.title
      return True
   except:
      return False


gameOver = False
while not gameOver:
    # print('still checking')
    print(getBoardState())
    checkGameState()
    selectcol(4)