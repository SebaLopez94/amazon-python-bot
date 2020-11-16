from selenium import webdriver
from time import sleep

class PS5Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.amazon.es/')
        sleep(50)

    def checkAndBuyPS5(self):
        self.driver.get('https://www.amazon.es/dp/B08KKJ37F7?tag=infolinkin-21th=1&psc=1')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
            buyNow.click()
            sleep(2)
            buyNow2 = self.driver.find_element_by_xpath('//*[@id="submitOrderButtonId"]/span/input')  
            buyNow2.click()
            sleep(1)
            self.driver.close()
        except Exception as e:
            print(e)
            sleep(3)
            self.checkAndBuyPS5()
bot = PS5Bot()
bot.login()
bot.checkAndBuyPS5()
