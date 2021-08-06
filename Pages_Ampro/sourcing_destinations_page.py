from inspect import stack
from pdb import set_trace
from base_Ampro.basepage import BasePage
from pages_Ampro.navigation_page import NavigationPage
import utilities_Ampro.custom_logger as cl
import logging, time, os.path
import random, traceback
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from configfiles_ampro import config
from traceback import print_stack
import pdb

class SourcingDestinationsPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #Locators
    _sourcing_destinations = "//div[@class='dropdown-menu show']//a[10]"    
    _share_icons_all = "shareSDChart"
    _share_button = "btnShareTools"
    _commodity_group_sd="(//div[@class='btn-group']//button//span)[1]"
    _commodity_sd = "(//div[@class='btn-group']//button//span)[2]"
    _destination_country_sd = "(//div[@class='btn-group']//button//span)[3]" 
    _first_c_g = "(//label[@title='--Select commodity group--'])[1]//ancestor::li//following-sibling::li[1]//label"
    _first_r_c = "(//label[@title='-- Select country --'])[1]//ancestor::li//following-sibling::li[1]//label"
    #_first_commodity="(//label[@title='-- Select commodity --'])[1]//ancestor::li//following-sibling::li[1]//label"
    _apply_button = "//div[@id='collapseFilter']//button[contains(text(),'Apply')]"
    _apply_button2 = "applyFilter"
    _key_insights = "overAllSummary"
    _first_c_g_sd = "(//label[@title='-- Select --'])[1]//ancestor::li//following-sibling::li//label[contains(text(),'{0}')]"
    _first_commodity_sd = "(//label[@title='-- Select --'])[2]//ancestor::li//following-sibling::li//label[contains(text(),'{0}')]"
    _first_dest_country_sd = "(//label[@title='-- Select --'])[3]//ancestor::li//following-sibling::li//label[contains(text(),'{0}')]"
    _key_insights = "overAllSummary" 
    _close_button = "//button[@comment='PopUp closed']//span"
    _email = "shareEmail"
    _comment = "shareComment"  
    _success_msg = "errorMsgShare"   
    _fav_tabs = "//div[@id='navbarSupportedContent']//a"
    _fav_tab_sd = "//div[@id='navbarSupportedContent']//a[@sectionofpage='Sourcing destinations']"
    _favourite_items = "//div[contains(@class,'row')]//a[@data-original-title='Remove from favourite']" 
    _favourite_icons = "//a[@data-original-title='Copy link' and contains(@class,'last-element') and not(contains(@style,'display: none'))]//preceding-sibling::a[@data-original-title='Add to favourite']"  
    _favourite_icon = "(//div[contains(@class,'row')]//a[@data-original-title='Add to favourite'])[{0}]"       
    _remove_icon = "//a[@sectionofpage='Chart - Remove from favourite']"    
    _delete_confirmation = "delete"
    _delete_alert = "//input[@id='checkLastElement']//following-sibling::button"
    _modal_text = "favouriteModalId"
    _OK_on_modal = "//div[@id='favouriteModal']//button[contains(text(),'OK')]"
    _chart_title = "//*[name()='svg']//*[name()='g' and @font-weight='bold']//*[name()='tspan']"
    _copy_icon = "//a[@data-original-title='Copy link' and contains(@class,'last-element') and not(contains(@style,'display: none'))]"
    _copy_link = "(//a[@data-original-title='Copy link' and contains(@class,'last-element') and not(contains(@style,'display: none'))]//following-sibling::div//a[@id='btnCopy'])[{0}]"
    _copy_modal = "copyLinkModalId"
    _OK_on_copy_modal = "//div[@id='copyLinkModal']//div[@class='modal-footer']//button[contains(text(),'OK')]"
    _text_on_copy_modal = "//div[@id='copyLinkModalId' and contains(text(),'Successfully copied at your clipboard')]"
    _additional_intelligence = "//a[@sectionofpage='Additional intelligence - View report'][1]"
    _header_on_reportdashboard = "//h1[@class='d-inline']"
    _carousel = "//div[@id='main-carousel']"
    _carousel_items = "//div[@id='main-carousel']//div[contains(@class,'carousel-item')]//img"
    _next_on_carousel = "//ol[@class='carousel-indicators ']//li"
    _close_cost_calculator = "//button[@actionname='Cost Calculator']//span"
    _close_strategy = "//button[@actionname='Strategy']//span"
    _header_strategy = "//h5[@id='exampleModalLabel' and contains(text(),'Create strategy')]"
    _header_cost_calculator = "//h5[@id='exampleModalLabel' and contains(text(),'Cost calculator')]"

    def FilterSelectionSourcingDestinations(self, CommodityGroup, Commodity, DestinationCountry):        
        try:
            self.elementClick(self._commodity_group_sd,locatorType="xpath")
            self.log.info("Select Commodity group dropdown clicked")
            time.sleep(2)                        
            element1 = self.getElement(self._first_c_g_sd.format(CommodityGroup),locatorType="xpath")            
            self.driver.execute_script("arguments[0].click();",element1)
            self.log.info("First Commodity Group selected from dropdown") 
            time.sleep(2)           
            self.elementClick(self._commodity_sd,locatorType="xpath")
            self.log.info("Select Commodity dropdown clicked")
            time.sleep(2)            
            element2 = self.getElement(self._first_commodity_sd.format(Commodity),locatorType='xpath')            
            self.driver.execute_script("arguments[0].click();",element2)            
            self.log.info("Text on Commodity selection [%s]",config.text_commodity)
            time.sleep(2)
            self.elementClick(self._destination_country_sd,locatorType="xpath")
            self.log.info("Select Destination Country dropdown clicked")
            time.sleep(2)            
            element3 = self.getElement(self._first_dest_country_sd.format(DestinationCountry),locatorType="xpath")                        
            self.driver.execute_script("arguments[0].click();",element3)            
            self.log.info("Text on Destination Country selection [%s]",config.text_country)            
            time.sleep(2)
            self.elementClick(self._apply_button2)
            self.log.info("Filter applied")
            time.sleep(2)      
                 
        except:
            self.log.error("Could not select value from dropdown ") 
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack())) 

    def verifyNavigationToSourcingDestinations(self):
        return self.isElementPresent(self._key_insights)        

    def downloadData(self): 
        self.elementClick("downloadDataSD")  
        time.sleep(4) 
    
    def verifyDownloadCompleted(self, Commodity, DestinationCountry, ext):
        #import pdb;pdb.set_trace()
        return self.verifyDownload(Commodity, DestinationCountry, ext)        

    def fileSharing(self,Email,Comment):
        try:                 
            return self.verifyFileSharing(self._share_icons_all, self._email, self._comment, Email, Comment, self._share_button,self._success_msg, self._close_button)
        except:  
            self.log.error("Could not call verifyFileSharing") 
            traceback.print_stack() 

    def count_of_favourites(self):  
        self.nav.navigateToMyFavourites()         
        if self.isElementPresent(self._fav_tab_sd, locatorType='xpath'):
            self.elementClick(self._fav_tab_sd, locatorType='xpath')
            time.sleep(4)
            favs = self.driver.find_elements_by_xpath(self._favourite_items)
            for c in favs:
                c_text = c.get_attribute("comment")                
                config.text_on_fav_items.append(c_text)
                self.log.info("Item appended to Favourites list [%s]", c_text)
            return len(config.text_on_fav_items)  
        else:
            return 0              

    def remove_from_favourites(self):        
        items_in_favs = self.driver.find_elements_by_xpath(self._remove_icon) 
        for item in items_in_favs:
            if item.is_displayed():  
                self.driver.execute_script("arguments[0].scrollIntoView(true);", item)            
                self.driver.execute_script("arguments[0].click();", item)  
                time.sleep(2)          
                confirmation_button = self.getElement(self._delete_confirmation)            
                self.driver.execute_script("arguments[0].scrollIntoView(true);", confirmation_button)
                self.driver.execute_script("arguments[0].click();", confirmation_button) 
                self.log.info("Clicked OK on Delete Confirmation")                
                time.sleep(2)       
                alert_button = self.getElement(self._delete_alert, locatorType='xpath')            
                self.driver.execute_script("arguments[0].scrollIntoView(true);", alert_button)
                self.driver.execute_script("arguments[0].click();", alert_button)
                self.log.info("Clicked OK on Deleted item Alert") 
                break           

    def addToFavourites(self,CommodityGroup, Commodity, DestinationCountry):                
        try:            
            #import pdb; pdb.set_trace()
            if self.count_of_favourites() >= 5: 
                self.log.info("since count of fav items is 5 hence entered if part of loop")                               
                self.remove_from_favourites()
                self.nav.navigateToSourcingDestinations()
                self.FilterSelectionSourcingDestinations(CommodityGroup, Commodity, DestinationCountry)
                elements = self.driver.find_elements_by_xpath(self._favourite_icons)                
                for el in elements:
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'end', inline: 'end'});", el)
                    time.sleep(4)
                    self.driver.execute_script("arguments[0].click();", el)
                    self.log.info("Clicked on Add to favourites icon")
                    time.sleep(2) 
                    OK_button = self.getElement(self._OK_on_modal, locatorType='xpath')                    
                    if self.verifyTextOnModal(self._modal_text, "Cannot be added to favourites as chart data is not available"):                            
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", OK_button)
                        self.driver.execute_script("arguments[0].click();", OK_button) 
                        continue  
                    elif self.verifyTextOnModal(self._modal_text, "Already added as favourite. Kindly access under My Favourites section."):
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", OK_button)
                        self.driver.execute_script("arguments[0].click();", OK_button) 
                        continue                                          
                    elif self.verifyTextOnModal(self._modal_text, "Maximum of five can be added as favourite."):                            
                        break                     
                    else: 
                        config.count += 1                           
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", OK_button)
                        self.driver.execute_script("arguments[0].click();", OK_button) 
                                                    
            else:
                self.log.info("since count of fav items is less than 5 hence entered else part of loop") 
                self.nav.navigateToSourcingDestinations()
                self.FilterSelectionSourcingDestinations(CommodityGroup, Commodity, DestinationCountry)             
                elements = self.driver.find_elements_by_xpath(self._favourite_icons)
                for el in elements:
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'end', inline: 'end'});", el)
                    time.sleep(4)
                    self.driver.execute_script("arguments[0].click();", el)
                    self.log.info("Clicked on Add to favourites icon")
                    time.sleep(2) 
                    OK_button = self.getElement(self._OK_on_modal, locatorType='xpath')                    
                    if self.verifyTextOnModal(self._modal_text, "Cannot be added to favourites as chart data is not available"):                            
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", OK_button)
                        self.driver.execute_script("arguments[0].click();", OK_button) 
                        continue  
                    elif self.verifyTextOnModal(self._modal_text, "Already added as favourite. Kindly access under My Favourites section."):
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", OK_button)
                        self.driver.execute_script("arguments[0].click();", OK_button) 
                        continue                                          
                    elif self.verifyTextOnModal(self._modal_text, "Maximum of five can be added as favourite."):                            
                        break                     
                    else: 
                        config.count += 1                           
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", OK_button)
                        self.driver.execute_script("arguments[0].click();", OK_button)              
        except Exception as e:
            self.log.error("Could not click on Add to Favourites icon [%s]",e) 
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))         
    
    def verifyAddToFavourites(self):
        return self.verifyTextOnModal(self._modal_text, "Maximum of five can be added as favourite.") 

    def copyLink(self):
        elements = self.driver.find_elements_by_xpath(self._copy_icon)               
        for ele in range(0,len(elements)):
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'end', inline: 'end'});", elements[ele])            
            self.driver.execute_script("arguments[0].click();", elements[ele]) 
            time.sleep(1)                       
            self.elementClick(self._copy_link.format(ele+1),locatorType='xpath')            
            self.waitForElement(self._copy_modal,locatorType='xpath')
            config.text_on_copy = self.getText(self._text_on_copy_modal, locatorType='xpath')
            OK_button = self.getElement(self._OK_on_copy_modal, locatorType='xpath')
            self.driver.execute_script("arguments[0].click();", OK_button)            
            time.sleep(1)
            
    def verifyLinkCopied(self):
        if "Successfully copied at your clipboard" in config.text_on_copy:
            return True
        else:
            return False   

    def clickOnAdditionalIntelligence(self):        
        global allHandles
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent handle for the current page identified [%s]", parentHandle)
        #config.text_on_addtional_intel = self.getText(self._additional_intelligence, locatorType='xpath')
        self.elementClick(self._additional_intelligence, locatorType='xpath')
        self.log.info("Clicked on reports under Additional Intelligence")
        time.sleep(2)        
        allHandles = self.driver.window_handles
        self.log.info("There are now 2 windows with different handles [%s]", len(allHandles))
        for handle in allHandles:
            self.log.info("At Handle [%s]", handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.driver.close()
                break
        self.driver.switch_to.window(parentHandle)

    def verifyNavigationToAdditionalIntelligence(self):             
        if len(allHandles) == 2:
            return True 
        else:
            return False 

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
            carousel_block = self.getElement(self._carousel, locatorType='xpath')
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'end', inline: 'end'});", carousel_block)
            self.log.info("Carousel scrolled into view")
            time.sleep(2) 
            #import pdb; pdb.set_trace()       
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
        


            









