from Base_Ampro.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
import Utilities_Ampro.custom_logger as cl
import logging, time
from selenium.webdriver import ActionChains

class Covid19ResourceCentrePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _Ampro_logo="(//nav[@id='tsc_nav_1']/a/img)[1]"
    _Covid19_resource_centre="//div[@id='navbarNavDropdown']/div/ul[2]/li[1]/a" 
    _Sector_deep_dive="covidsectorDeepDive-tab"
    _Category_snapshot="covidcategorySnapshot-tab"
    _100_day_framework="covid100DayFramework-tab"
    _Covid19_video_series="covidcovid19VideoSeries-tab"
    _Covid19_breadcrumb="//div[@class='row']/div/ol//li[contains(@class,'breadcrumb-item active')]"
    _No_record_message="//div[contains(text(),'No record found')]"
    _tab1_img="//div[@id='sectioncovidsectorDeepDive']/div[1]/div[1]/img"
    _tab2_img="//div[@id='sectioncovidcategorySnapshot']/div[1]/div[1]/img"
    _tab3_img="//div[@id='sectioncovid100DayFramework']/div[1]/div[1]/img"
    _tab4_vdo="//div[@id='sectioncovidvideoSeries']/div[1]/iframe"
    
    def navigateToHome(self):
        self.elementClick(locator=self._Ampro_logo,locatorType="xpath")

    def navigateToCovid19ResourceCentre(self):
        self.elementClick(locator=self._Covid19_resource_centre,locatorType="xpath") 
        time.sleep(2)

    def navigateToSectorDeepDive(self):
        self.webScroll(direction="down")
        self.elementClick(locator=self._Sector_deep_dive)
        time.sleep(2)
        
    def navigateToCategorySnapshot(self):
        self.elementClick(locator=self._Category_snapshot)
        time.sleep(2)

    def navigateTo100DayFramework(self):
        self.elementClick(locator=self._100_day_framework)    
        time.sleep(2)

    def navigateToCovid19VideoSeries(self):
        self.elementClick(locator=self._Covid19_video_series)
        time.sleep(2)
        self.webScroll(direction="up")  

    def verifyNavigationToCovid19Tab(self):
        result=self.isElementPresent(self._Covid19_breadcrumb,locatorType="xpath") 
        return result

    def verifyNavigationToSectorDeepDive(self):
        tab1Message=self.getElement(self._No_record_message,locatorType="xpath")
        r1=self.isElementPresent(self._tab1_img,locatorType="xpath")
        r2=tab1Message.is_displayed()
        if r1==True or r2==True:
            #import pdb;pdb.set_trace()
            return True
        else:
            return False 

    def verifyNavigationToCategorySnapshot(self):
        tab2Message=self.getElement(self._No_record_message,locatorType="xpath")
        r1=self.isElementPresent(self._tab2_img,locatorType="xpath")
        r2=tab2Message.is_displayed()
        if r1==True or r2==True:
            #import pdb;pdb.set_trace()
            return True
        else:
            return False 

    def verifyNavigationTo100DayFramework(self):
        tab3Message=self.getElement(self._No_record_message,locatorType="xpath")
        r1=self.isElementPresent(self._tab3_img,locatorType="xpath")
        r2=tab3Message.is_displayed()
        if r1==True or r2==True:
            #import pdb;pdb.set_trace()
            return True
        else:
            return False  

    def verifyNavigationToCovid19VideoSeries(self):
        tab4Message=self.getElement(self._No_record_message,locatorType="xpath")
        r1=self.isElementPresent(self._tab4_vdo,locatorType="xpath")
        r2=tab4Message.is_displayed()
        if r1==True or r2==True:
            #import pdb;pdb.set_trace()
            return True
        else:
            return False                               



    


