from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://connect-4.org/en')

driver.find_elements_by_xpath('//button[@class=\'mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent ng-tns-c23-0\']')[0].click()
# getFriendButton.click()

driver.find_elements_by_xpath('//input[@id=\'invitionLinkInput2\']').sendKeys('playerOne')
while True:
    pass