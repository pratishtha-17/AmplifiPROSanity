from Base_Ampro.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
import Utilities_Ampro.custom_logger as cl
import logging, time, traceback
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

class SolutionsPage(SeleniumDriver):

    allHandles = None

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _solutions="//div[@id='navbarNavDropdown']/div/ul[2]/li[6]/a"
    _my_solutions="//div[@id='navbarNavDropdown']/div/ul[2]/li[6]/div/ul[1]"
    #_my_solutions="(//a[contains(text(),'My solutions')])[1]"
    _first_item_my_solutions="(//ul[contains(@class,'navbar-nav mt-3')]//li[6]//div//div/a)[1]"
    _my_request="//div[@id='navbarNavDropdown']/div/ul[2]/li[6]/div/ul[2]"
    _attribute="//input[@id='timeInSeconds']"
    _my_deliverables="//div[@id='navbarNavDropdown']/div/ul[2]/li[6]/div/ul[3]"
    _more_offerings="//div[@id='navbarNavDropdown']/div/ul[2]/li[6]/div/ul[4]"
    
    def navigateToSolutions(self):
        self.elementClick(self._solutions,locatorType="xpath")
        self.log.info("Clicked on Solutions top menu")

    def navigateToMysolutions(self):
        global allHandles
        action = ActionChains(self.driver)
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent handle for the current page identified [%s]",parentHandle)
        first_link = self.getElement(self._my_solutions,locatorType="xpath")
        action.move_to_element(first_link).click().perform()
        self.log.info("Clicked on My solutions under Solutions top menu")
        time.sleep(2)
        second_link = self.getElement(self._first_item_my_solutions,locatorType="xpath")
        action.move_to_element(second_link).click().perform()
        time.sleep(2)
        self.log.info("Clicked on first link under My solutions")
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

    def verifyNavigationToSolutions(self):             
        if len(allHandles) == 2:
            return True 
        else:
            return False

    def navigateToMyrequest(self):
        global allHandles
        action = ActionChains(self.driver)
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent handle for the current page identified [%s]",parentHandle)
        first_link = self.getElement(self._my_request,locatorType="xpath")
        action.move_to_element(first_link).click().perform()
        time.sleep(2)
        self.log.info("Clicked on My request under Solutions")
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

    def verifyNavigationToMyrequest(self):             
        if len(allHandles) == 2:
            return True 
        else:
            return False 

    def navigateToMydeliverables(self):
        global allHandles
        action = ActionChains(self.driver)
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent handle for the current page identified [%s]",parentHandle)
        first_link = self.getElement(self._my_deliverables,locatorType="xpath")
        action.move_to_element(first_link).click().perform()
        time.sleep(2)
        self.log.info("Clicked on My request under Solutions")
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

    def verifyNavigationToMydeliverables(self):             
        if len(allHandles) == 2:
            return True 
        else:
            return False               

    