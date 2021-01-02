from Base_Ampro.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
import Utilities_Ampro.custom_logger as cl
import logging, time, traceback
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

class ResourcesPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _resources="//div[@id='navbarNavDropdown']/div/ul[2]/li[5]/a"
    _blogs="(//a[contains(text(),'Blogs')])[1]"
    _breadcrumb="//div[contains(@class,'pageheading')]//ol//li[3]"
    _attribute="//input[@id='timeInSeconds']"
    _case_studies="(//a[contains(text(),'Case studies')])[1]"
    _podcasts_n_videos="(//a[contains(text(),'Podcasts and videos')])[1]"
    _spend_matters_insights="(//a[contains(text(),'Spend matters insights')])[1]"
    _thought_leadership="(//a[contains(text(),'Thought leadership')])[1]"
    _CASME_resource_centre="(//a[contains(text(),'CASME resource centre')])[1]"
    _CASME_logo="//a[contains(@class,'logo pull-left site-logo')]/img"
    
    def navigateToResources(self):
        self.elementClick(self._resources,locatorType="xpath")
        self.log.info("Clicked on Resources top menu")

    def navigateToBlogs(self):
        action=ActionChains(self.driver)
        first_link=self.getElement(self._blogs,locatorType="xpath")
        action.move_to_element(first_link).click().perform()
        self.log.info("Clicked on Blogs under All Intelligence top menu")
        time.sleep(3)

    def verifyNavigationToBlogs(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        attribute=self.getElement(self._attribute,locatorType="xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Blogs [%s]",breadcrumb)
        attribute_value=attribute.get_attribute("pagename")
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Blogs" and attribute_value=="Resources- Blogs":
            return True 
        else:
            return False

    def navigateToCaseStudies(self):
        action=ActionChains(self.driver)
        second_link=self.getElement(self._case_studies,locatorType="xpath")
        action.move_to_element(second_link).click().perform()
        self.log.info("Clicked on Case studies under All Intelligence top menu")
        time.sleep(3)

    def verifyNavigationToCaseStudies(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        attribute=self.getElement(self._attribute,locatorType="xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Case studies [%s]",breadcrumb)
        attribute_value=attribute.get_attribute("pagename")
        #import pdb;pdb.set_trace()
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Case studies" and attribute_value=="Resources- Case studies":
            return True 
        else:
            return False  

    def navigateToPodcastsnVideos(self):
        action=ActionChains(self.driver)
        third_link=self.getElement(self._podcasts_n_videos,locatorType="xpath")
        action.move_to_element(third_link).click().perform()
        self.log.info("Clicked on Podcasts and videos under All Intelligence top menu")
        time.sleep(3)

    def verifyNavigationToPodcastsnVideos(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        attribute=self.getElement(self._attribute,locatorType="xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Podcasts and videos [%s]",breadcrumb)
        attribute_value=attribute.get_attribute("pagename")
        #import pdb;pdb.set_trace()
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Podcasts and videos" and attribute_value=="Resources- Podcasts and videos":
            return True 
        else:
            return False   

    def navigateToSpendMattersInsights(self):
        action=ActionChains(self.driver)
        fourth_link=self.getElement(self._spend_matters_insights,locatorType="xpath")
        action.move_to_element(fourth_link).click().perform()
        self.log.info("Clicked on Spend Matters Insights under All Intelligence top menu")
        time.sleep(3)

    def verifyNavigationToSpendMattersInsights(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        attribute=self.getElement(self._attribute,locatorType="xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Spend matters insights [%s]",breadcrumb)
        attribute_value=attribute.get_attribute("pagename")
        #import pdb;pdb.set_trace()
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Spend matters insights" and attribute_value=="Resources- Spend matters insights":
            return True 
        else:
            return False          

    def navigateToThoughtLeadership(self):
        action=ActionChains(self.driver)
        fifth_link=self.getElement(self._thought_leadership,locatorType="xpath")
        action.move_to_element(fifth_link).click().perform()
        self.log.info("Clicked on Thought leadership under All Intelligence top menu")
        time.sleep(3)

    def verifyNavigationToThoughtLeadership(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        attribute=self.getElement(self._attribute,locatorType="xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Thought leadership [%s]",breadcrumb)
        attribute_value=attribute.get_attribute("pagename")
        #import pdb;pdb.set_trace()
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Thought leadership" and attribute_value=="Resources- Thought leadership":
            return True 
        else:
            return False 

    def navigateToCASMEResourceCentre(self):
        action=ActionChains(self.driver)
        sixth_link = self.getElement(self._CASME_resource_centre,locatorType="xpath")
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent Handle identified [%s]", parentHandle)
        action.move_to_element(sixth_link).click().perform()
        self.log.info("Clicked on CASME resource centre under All Intelligence top menu")
        time.sleep(3)
        #Finding all handles
        handles=self.driver.window_handles
        for handle in handles:
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                break
                
    def verifyNavigationToCASMEResourceCentre(self):
        result=self.isElementPresent(self._CASME_logo,locatorType="xpath")
        if result==True:
            return result 
        else:
            return False                         

    