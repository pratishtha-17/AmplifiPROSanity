from base_Ampro.basepage import BasePage
from selenium.webdriver import ActionChains
import utilities_Ampro.custom_logger as cl
import logging, time
from selenium.webdriver import ActionChains

class TopicalInsightsPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _all_intelligence="//div[@id='navbarNavDropdown']/div/ul[2]/li[2]/a"
    #_Topical_insights="//a[contains(text(),'Topical insights')]" 
    _Topical_insights="(//li[@class='nav-item']//a)[1]"
    #_Topical_insights="(//ul[@class='navbar-nav mt-3']//li)[1]"
    _Latest_topics="covidlatestTopics-tab"
    _Covid_19="covidcOVID19-tab"
    _All_topics="covidallTopics-tab"
    #_Topical_insights_breadcrumb="//li[contains(@class,'breadcrumb-item active') and contains(text(),'Topical insights')]"
    _Topical_insights_breadcrumb="//div[@class='col-sm-12 pageheading']//li[contains(@class,'breadcrumb-item active') and contains(text(),'Topical insights')]"
    _tab_tiles="//div[contains(@class,'blogimageSection')]"
    _No_records_found="//div[contains(text(),'No record found')]"
    
    
    def navigateToTopicalInsights(self):
        self.elementClick(locator=self._Topical_insights,locatorType="xpath") 
        time.sleep(2)

    def navigateToLatestTopics(self):
        self.webScroll(direction="down")
        self.elementClick(locator=self._Latest_topics)
        time.sleep(2)
        
    def navigateToCovid19(self):
        self.elementClick(locator=self._Covid_19)
        time.sleep(2)

    def navigateToAllTopics(self):
        self.elementClick(locator=self._All_topics)    
        time.sleep(2)

    def verifyNavigationToTopicalInsights(self):
        result=self.isElementPresent(self._Topical_insights_breadcrumb,locatorType="xpath")
        self.log.info("The result was returned as [%s]",result) 
        return result

    def verifyNavigationToLatestTopics(self):        
        temp_result1=self.elementPresenceCheck(self._tab_tiles,byType='xpath')
        if not temp_result1:
            temp_result2=self.isElementPresent(self._No_records_found,locatorType='xpath')
        #import pdb;pdb.set_trace()
        if temp_result1==True or temp_result2==True:
            return True
        else:                  
            return False        

    def verifyNavigationToCovid19(self):
        temp_result1=self.elementPresenceCheck(self._tab_tiles,byType='xpath')
        if not temp_result1:
            temp_result2=self.isElementPresent(self._No_records_found,locatorType='xpath')
        #import pdb;pdb.set_trace()
        if temp_result1==True or temp_result2==True:
            return True
        else:                  
            return False         

    def verifyNavigationToAllTopics(self):
        temp_result1=self.elementPresenceCheck(self._tab_tiles,byType='xpath')
        if not temp_result1:
            temp_result2=self.isElementPresent(self._No_records_found,locatorType='xpath')
        #import pdb;pdb.set_trace()
        if temp_result1==True or temp_result2==True:
            return True
        else:                  
            return False        

                                    



    


