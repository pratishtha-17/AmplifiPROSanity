from Base_Ampro.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
import Utilities_Ampro.custom_logger as cl
import logging, time, traceback
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from configfiles_ampro import config
from selenium.webdriver.common.keys import Keys

class AddToFavouritePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _categories_dropdown="//div[@id='navbarNavDropdown']/div/ul[2]/li[3]/a"
    _category="//section[@id='loadTopCategory']//aside"
    _category_breadcrumb="//div[contains(@class,'pageheading')]//a[@id='clickCategory']"
    _category_tiles="//div[@id='loadCategoryGroup']//div[contains(@class,'carousel-inner')]"
    _add_to_fav_link="(//i[contains(@sectionofpage,'{0}')])[1]"
    _OK_button="(//button[text()='OK'])[1]"
    _success_msg = "//div[contains(text(),'Added to your favourites.')]"
    
    def add_to_favouritefn(self):
        elements=[]     
        elements=self.driver.find_elements_by_xpath(self._category_tiles)
        try:            
            self.log.info("Inside loop")
            cat_hovered=elements[randint(0, len(elements) - 1)]
            self.log.info("Category idetified randomly %s",cat_hovered)
            text_cat_hovered=self.getText(element=cat_hovered)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});",cat_hovered)
            time.sleep(4)
            action = ActionChains(self.driver)
            action.move_to_element(cat_hovered).perform()
            self.log.info("Hovered to element [%s] ",cat_hovered)
            time.sleep(2)
            #import pdb; pdb.set_trace()
            fav_link = self._add_to_fav_link.format(text_cat_hovered)
            target = self.driver.find_element_by_xpath(fav_link)
            self.driver.execute_script("arguments[0].click();",target)
            time.sleep(2) 
            self.log.info("Clicked on the favourites icon")         
                                      
        except Exception as e:
                self.log.error("Could not click on hovered tile link [%s]",e) 
                self.log.error("Exception Caught: {}".format(traceback.format_exc()))
                self.log.error("".join(traceback.format_stack()))  

    def verifyAddToFavourite(self):
        #self.driver.switch_to.frame("0") 
        time.sleep(2)
        element = self.getElement(self._success_msg,locatorType="xpath")
        self.log.info("Added to favourites success message encountered [%s]",element)
        result = self.isElementPresent(self._success_msg,locatorType="xpath")
        #import pdb; pdb.set_trace()
        if result == True:
            self.elementClick(self._OK_button,locatorType="xpath")
            return result
        else:
            return False    



            
               

    
    
