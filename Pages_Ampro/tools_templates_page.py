from Base_Ampro.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
import Utilities_Ampro.custom_logger as cl
import logging, time
from selenium.webdriver import ActionChains
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class ToolsnTemplatesPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _ampro_logo="(//nav[@id='tsc_nav_1']/a/img)[1]"
    _tools_n_templates="//div[@id='navbarNavDropdown']/div/ul[2]/li[2]/a" 
    _tools_templates_breadcrumb="//div[@class='row']/div/ol//li[contains(@class,'breadcrumb-item active')]"
    _share_icon="//i[@id='shareTools']"
    _email="shareEmail"
    _comment="shareComment"
    _share_button="btnShareTools"
    _share_success_msg="errorMsgShare"
    _strategy_tool="//a[contains(text(),'Strategy tool')]"
    _create_strategy_modal_title="(//div[contains(@class,'modal-header')]/h5)[2]"
    _modal_dropdown="//span[@id='select2-_Report-container']"
    _close_button="//div[@id='shareToolsPopUp']//div/button/span"

    def navigateToHome(self):
        self.elementClick(locator=self._ampro_logo,locatorType="xpath")

    def navigateToToolsnTemplates(self):
        self.elementClick(locator=self._tools_n_templates,locatorType="xpath") 
        time.sleep(2)

    def strategyTool(self):
        self.elementClick(self._strategy_tool,locatorType="xpath")
        time.sleep(3)
      
      
    #this method randomly clicks on the available share icons on page
    def fileSharing(self,Email,Comment): 
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(2)
        links=[]
        #import pdb;pdb.set_trace()
        links = self.driver.find_elements_by_xpath(self._share_icon)
        l = links[randint(0, len(links) - 1)]
        l.click()
        time.sleep(2)
        self.sendKeys(Email,self._email)
        time.sleep(2)
        self.sendKeys(Comment,self._comment)
        time.sleep(2)
        self.elementClick(self._share_button)
        

    def verifyNavigationToToolsnTemplates(self):
        result=self.isElementPresent(self._tools_templates_breadcrumb,locatorType="xpath") 
        return result

    def verifyStrategyCreation(self):
        self.driver.switch_to.frame(0)
        time.sleep(2)
        result=self.isElementPresent(self._modal_dropdown,locatorType="xpath") 
        return result 
        self.driver.switch_to.default_content()   

    def verifyFileSharing(self):
        result=self.isElementPresent(self._share_success_msg)
        self.elementClick(self._close_button,locatorType="xpath")
        time.sleep(1)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
        time.sleep(2)
        return result    

    
