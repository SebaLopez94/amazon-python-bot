from selenium import webdriver
from time import sleep

class PS5Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.amazon.es/')
        sleep(50)

    def buyPS5(self):
        self.driver.get('https://www.amazon.es/dp/8441539901/?coliid=I3DE9591VF4NM3&colid=2AWUCLX2YRNRY&psc=1')
        sleep(1)   
        try:
            buyNow = self.driver.find_element_by_xpath('//*[@id="buy-now-button"]')
            buyNow.click()
            sleep(1)
            buyNow2 = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/div/div[3]/div/form/div/span/span/span/input')  
            buyNow2.click()
            sleep(2)
            self.driver.close()
        except Exception as e:
            print(e)
            sleep(2)
            self.buyPS5()
bot = PS5Bot()
bot.login()
bot.buyPS5()