from base_Ampro.basepage import BasePage
from selenium.webdriver import ActionChains
import utilities_Ampro.custom_logger as cl
import logging, time, traceback
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

class RequestCustomIntelligencePage(BasePage):

    allHandles = None

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    #_request_custom_intelligence = "//div[@id='navbarNavDropdown']/div/ul[2]/li[6]/a"
    _request_custom_intelligence = "//ul[@class='navbar-nav mt-3']//li[7]//a"        

    def navigateToRequestCustomIntelligence(self):
        global allHandles
        actions = ActionChains(self.driver)
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent handle for the current page identified [%s]",parentHandle)
        first_link = self.getElement(self._request_custom_intelligence, locatorType="xpath")
        actions.move_to_element(first_link).click().perform()
        self.log.info("Clicked on Request custom intelligence on top menu")
        time.sleep(2)        
        allHandles = self.driver.window_handles
        self.log.info("There are now 2 windows with different handles [%s]",len(allHandles))
        for handle in allHandles:
            self.log.info("At Handle [%s]", handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.driver.close()
                break
        self.driver.switch_to.window(parentHandle)

    def verifyNavigationToCustomIntelligence(self):             
        if len(allHandles) == 2:
            return True 
        else:
            return False

    