from Base_Ampro.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
import Utilities_Ampro.custom_logger as cl
import logging, time, traceback
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from configfiles_ampro import config

class CategoriesPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _categories_dropdown="//div[@id='navbarNavDropdown']/div/ul[2]/li[3]/a"
    _category="//section[@id='loadTopCategory']//aside"
    _category_breadcrumb="//div[contains(@class,'pageheading')]//a[@id='clickCategory']"
    _category_tiles="//div[@id='loadCategoryGroup']//div[contains(@class,'carousel-inner')]"
    _category_tile_link="(//a[contains(@sectionofpage,'{0}')])[1]"
    
    def navigateToHome(self):
        self.elementClick(locator=self._ampro_logo,locatorType="xpath")

    def navigateToCategoryViaTopMenu(self):
        self.elementClick(locator=self._categories_dropdown,locatorType="xpath") 
        time.sleep(2)
        links=[]
        #import pdb;pdb.set_trace()
        links = self.driver.find_elements_by_xpath(self._category)
        link_selected = links[randint(0, len(links) - 1)]
        config.text_on_dropdown_item = self.getText(element=link_selected)
        link_selected.click()
        time.sleep(2)

    def navigateToCategoryViaHomepg(self):
        elements=[]     
        try:
            elements = self.driver.find_elements_by_xpath(self._category_tiles)
            config.cat_hovered=elements[randint(0, len(elements) - 1)]
            config.text_cat_hovered=self.getText(element=config.cat_hovered)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});",config.cat_hovered)
            time.sleep(4)
            action = ActionChains(self.driver)
            action.move_to_element(config.cat_hovered).perform()
            self.log.info("Hovered to element [%s] on location [%s] with size [%s]",config.cat_hovered,config.cat_hovered.location,config.cat_hovered.size)
            time.sleep(2)
            report_link = self._category_tile_link.format(config.text_cat_hovered)
            config.target = self.driver.find_element_by_xpath(report_link)
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();",config.target)
            #action.move_to_element(config.target).click().perform()
            time.sleep(4)                               
        except Exception as e:
            self.log.error("Could not click on hovered tile link [%s]",e) 
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))  
         
    def verifyNavigationToCategoryViaTopMenu(self):
        config.text_on_breadcrumb=self.getText(locator=self._category_breadcrumb,locatorType="xpath")
        if config.text_on_dropdown_item==config.text_on_breadcrumb:
            return True
        else:
            return False

    def verifyNavigationToCategoryViaHomepg(self):
        config.textafterclick=self.getText(locator=self._category_breadcrumb,locatorType="xpath")
        #import pdb;pdb.set_trace()
        if config.text_cat_hovered==config.textafterclick:
            return True
        else:
            return False  

                     

    
    
