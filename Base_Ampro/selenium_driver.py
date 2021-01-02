from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import Utilities_Ampro.custom_logger as cl
import logging
import time
import os,traceback,sys


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "tagname":
            return By.TAG_NAME    
        else:
            self.log.error("Locator type " + locatorType +
                          " not correct/supported")
            return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getElements(self,locator,locatorType):
        elements=None
        try:
            locatorType=locatorType.lower()
            byType=self.getbyType(locatorType)
            elements=self.driver.find_elements(byType,locator)
            self.log.info('element Found with locator '+ locator+ ' and locatorType '+locatorType)
        except:
            self.log.error('Element not found in getElement '+ locator+ ' and locatorType '+locatorType)  
        return elements    

    def elementClick(self,locator="", locatorType="id", element=None):
        
        try:
            if locator:
                element=self.getElement(locator, locatorType)
            element.click()
            self.log.info('Element found and clicked with locator: '+ locator+ ' and locatorType '+locatorType)
            
        except:
            self.log.error('Element could not be clicked with locator: '+ locator+ ' and locatorType '+locatorType)


    def sendKeys(self,data,locator="",locatorType="id", element=None):
        
        try:
            if locator:
                element=self.getElement(locator, locatorType)
            element.clear()
            element.send_keys(data)
            self.log.info('Data sent to element with locator '+locator+" and locatortype "+locatorType)
            
        except:
            self.log.error('Data could not be sent to element with locator '+locator+" and locatortype "+locatorType)  
    
    def sendKeysWhenReady(self, data, locatorType="id",locator="" ):
        
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(10) +
                          " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=10,
                                 poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("Element appeared on the web page")
            element.click()
            element.send_keys(data)

            if element.get_attribute("value") != data:
                self.log.debug("Text is not sent by xpath in field so try to send string char by char!")
                element.clear()
                for i in range(len(data)):
                    element.send_keys(data[i] + "")
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Element not appeared on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.error("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            self.log.error("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                self.log.error("Element not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            self.log.error("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     StaleElementReferenceException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def getText(self,locator="",locatorType="id",element="", info=""):
        try:
            if locator: # This means if locator is not empty
                element = self.getElement(locator, locatorType)
                text = element.text
            else:
                text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text  

    def webScroll(self,direction="up"):  
        if direction=="up":
            self.driver.execute_script("window.scrollBy(0,-1000);")
            time.sleep(3)
        elif direction=="down":
            self.driver.execute_script("window.scrollTo(0,250);")
            time.sleep(3)            
