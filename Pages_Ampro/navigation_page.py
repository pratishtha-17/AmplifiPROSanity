from base_Ampro.basepage import BasePage
from selenium.webdriver import ActionChains
import utilities_Ampro.custom_logger as cl
import logging, time, traceback
from selenium.webdriver import ActionChains
from random import randint
from configfiles_ampro import config
from selenium.webdriver.common.keys import Keys

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _ampro_logo = "navbar-brand-header"
    _recently_viewed = "loadRecentView"
    _sourcing_destinations="(//a[contains(text(),'Sourcing destinations')])[1]"
    _commodity_group_c="(//div[@class='btn-group']//button//span)[1]"
    _all_intelligence="//ul[@class='navbar-nav mt-3']//li[3]"
    _user_icon = "(//a[@id='navbarDropdownMenuLinka'])[1]"
    _my_favourites_link = "//div[contains(@class,'dropdown-menu-right show')]//a[text()='My favourites']"    

    def navigateToHomePage(self):
        self.elementClick(self._ampro_logo)
        self.waitForElement(self._recently_viewed)

    def navigateToAllIntelligence(self):
        self.elementClick(self._all_intelligence,locatorType="xpath")
        self.log.info("Clicked on All Intelligence top menu")     

    def navigateToSourcingDestinations(self):
        self.elementClick(self._all_intelligence,locatorType="xpath")
        self.log.info("Clicked on All Intelligence top menu")
        actions = ActionChains(self.driver)
        link = self.getElement(self._sourcing_destinations,locatorType="xpath")
        actions.move_to_element(link).click().perform()
        time.sleep(2)
        self.log.info("Landed on Sourcing destinations from All intelligence top menu") 

    def navigateToMyFavourites(self):
        self.elementClick(self._user_icon, locatorType='xpath')        
        favourites_link = self.getElement(self._my_favourites_link, locatorType='xpath')
        actions = ActionChains(self.driver)
        actions.move_to_element(favourites_link).click().perform() 
        time.sleep(4)  

      

               

