from base_Ampro.basepage import BasePage
import utilities_Ampro.custom_logger as cl
import logging,time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from pages_Ampro.navigation_page import NavigationPage
from configfiles_ampro import config
import traceback

class HomePage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        
    #Locators
    _FAQ_link = "//div[@class='footer']//a[contains(text(),'FAQ')]"
    _questions_FAQ = "//div[@class='faqSection']//h3"
    _first_question_FAQ = "(//div[@class='faqSection']//h3)[1]"
    _user_icon = "(//a[@id='navbarDropdownMenuLinka'])[1]"
    _profile_link = "(//div[contains(@class,'dropdown-menu')]//ul//following::a[text()='Profile'])[1]"
    _My_profile_header = "//div[contains(@class,'col-sm-8 pageheading')]//h1[contains(text(),'My profile')]"    
    _sign_out = "//div[contains(@class,'dropdown-menu dropdown-menu-right show')]//a[@sectionofpage='Sign out']"
    _tier_name = "//a[@id='navbar-brand-header']//span"
    _tier_pop_up = "(//div[@class='modal-content']//span[text()='tiers'])[1]"
    _close_pop_up ="//button[@sectionofpage='Close']//span"
    _terms_n_conditions = "//div[@class='footer']//a[contains(text(),' Terms & conditions')]"
    _terms_n_conditions_header = "//header[@class='py-2']/h1"
    _login_button="//button[contains(text(),'Sign in')]"

    #to check in
    def navigationToFAQ(self):
        self.nav.navigateToHomePage()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END) 
        self.waitForVisibilityOfElement(self._FAQ_link, locatorType='xpath')
        self.elementClick(self._FAQ_link, locatorType='xpath')
        self.waitForElement(self._first_question_FAQ, locatorType='xpath')
        
    #to checkin to TFS comment 2
    def verifyNavigationToFAQ(self):
        return self.isElementPresent(self._first_question_FAQ, locatorType='xpath')

    def navigationToTermsnConditions(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)         
        self.waitForVisibilityOfElement(self._terms_n_conditions, locatorType='xpath')
        time.sleep(2)
        self.elementClick(self._terms_n_conditions,locatorType='xpath')
        self.waitForElement(self._terms_n_conditions_header, locatorType='xpath')

    def verifyNavigationToTermsnConditions(self):
        return self.isElementPresent(self._terms_n_conditions_header, locatorType='xpath')  

    def navigateToProfile(self):
        self.elementClick(self._user_icon, locatorType='xpath')        
        profile_link = self.getElement(self._profile_link, locatorType='xpath')
        actions = ActionChains(self.driver)
        actions.move_to_element(profile_link).click().perform() 
        self.waitForElement(self._My_profile_header, locatorType='xpath')     

    def verifyNavigationToProfile(self):
        return self.isElementPresent(self._My_profile_header, locatorType='xpath')

    def clickTierName(self):
        self.elementClick(self._tier_name, locatorType='xpath')        
        self.waitForElement(self._tier_pop_up, locatorType= 'xpath')
        #time.sleep(4)

    def verifyTierPopUp(self):
        result = self.isElementPresent(self._tier_pop_up, locatorType='xpath') 
        self.elementClick(self._close_pop_up, locatorType='xpath')        
        return result 

    def signOut(self):
        self.elementClick(self._user_icon, locatorType='xpath')        
        sign_out_link = self.getElement(self._sign_out, locatorType='xpath')
        actions = ActionChains(self.driver)
        actions.move_to_element(sign_out_link).click().perform() 
        self.waitForElement(self._login_button, locatorType='xpath')  

    def verifySignOut(self):
        return self.isElementPresent(self._login_button, locatorType='xpath')    

    def carouselNewWindow(self):        
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent handle for the current page identified [%s]", parentHandle)                   
        allHandles = self.driver.window_handles
        self.log.info("There are now 2 windows with different handles [%s]", len(allHandles))
        for handle in allHandles:
            self.log.info("At Handle [%s]", handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                config.carousel_item_titles.append(self.getTitle())
                #import pdb; pdb.set_trace()
                self.driver.close()
                break
        self.driver.switch_to.window(parentHandle)

    def carouselCostCalculatorPopUp(self):
        x = self.getElement(self._header_cost_calculator, locatorType='xpath')
        text = x.get_attribute("innerText")
        config.carousel_item_titles.append(text.strip())
        self.elementClick(self._close_cost_calculator, locatorType='xpath')

    def carouselStrategyPopUp(self):
        x = self.getElement(self._header_strategy, locatorType='xpath')
        config.carousel_item_titles.append(x.get_attribute("innerText"))
        self.elementClick(self._close_strategy, locatorType='xpath')

    def clickOnCarousel(self):
        try:                   
            elements = self.driver.find_elements_by_xpath(self._carousel_items)
            indicators = self.driver.find_elements_by_xpath(self._next_on_carousel)           
            for ele in range(len(elements)):            
                if indicators[ele].get_attribute("data-slide-to") in ['0','2','4']:
                    self.elementClick(element=indicators[ele])
                    self.log.info("Indicator clicked on carousel [%s]", ele)
                    time.sleep(1)
                    self.elementClick(element=elements[ele]) 
                    self.log.info("Tile clicked on carousel [%s]", ele)
                    time.sleep(4)           
                    self.carouselNewWindow()     
                elif indicators[ele].get_attribute("data-slide-to") == '1':
                    self.elementClick(element=indicators[ele])
                    self.log.info("Indicator clicked on carousel [%s]", ele)
                    time.sleep(1)
                    self.elementClick(element=elements[ele]) 
                    self.log.info("Tile clicked on carousel [%s]", ele)
                    time.sleep(4)           
                    self.carouselCostCalculatorPopUp()
                elif indicators[ele].get_attribute("data-slide-to") == '3':
                    self.elementClick(element=indicators[ele])
                    self.log.info("Indicator clicked on carousel [%s]", ele)
                    time.sleep(1)
                    self.elementClick(element=elements[ele]) 
                    self.log.info("Tile clicked on carousel [%s]", ele)
                    time.sleep(4)           
                    self.carouselStrategyPopUp()
        except Exception as e:
            self.log.error("Could not click on carousel items")  
            self.log.error("Could not click on Add to Favourites icon [%s]",e) 
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))   
            
    def verifyClickOnCarouselItems(self):  
        #import pdb; pdb.set_trace() 
        return self.verifyCaraouselItems(['Work flow', 'Cost calculator', 'Work flow', 'Create strategy', 'Work flow'],config.carousel_item_titles)      
                  

          
        
