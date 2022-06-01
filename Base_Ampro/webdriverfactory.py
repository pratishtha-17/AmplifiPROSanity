import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        #Test URL
        #baseURL="http://tscdelphp03:9090/amplifipro-test-july/login" 
        #UAT URL
        #baseURL="https://amplifipro2.tsclabs.in/" 
        #PROD url
        baseURL = "https://amplifipro.thesmartcube.com/" 
        if self.browser=="ieexplorer":
            driver=webdriver.Ie()
        elif self.browser=="firefox":
            driver=webdriver.Firefox()
        else:
            driver=webdriver.Chrome()
            driver.set_window_size(1366,768)
        
        driver.implicitly_wait(4)
        # Maximize the window
        driver.maximize_window()
        driver.get_window_size()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver                 