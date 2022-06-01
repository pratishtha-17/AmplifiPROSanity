from base_Ampro.basepage import BasePage
from selenium.webdriver import ActionChains
import utilities_Ampro.custom_logger as cl
import logging, time, traceback
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from configfiles_ampro import config
from selenium.webdriver.common.keys import Keys
from pages_Ampro.navigation_page import NavigationPage
from configfiles_ampro import config
from traceback import print_stack
#new comment added for git tutorial
class AddToFavouritePage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #Locators
    # _categories_dropdown = "//div[@id='navbarNavDropdown']/div/ul[2]/li[3]/a"
    # _category = "//section[@id='loadTopCategory']//aside"
    # _category_breadcrumb = "//div[contains(@class,'pageheading')]//a[@id='clickCategory']"
    _category_tiles = "//div[@id='loadCategoryGroup']//div[contains(@class,'carousel-inner')]"
    _individual_category_tile = "(//div[@id='loadCategoryGroup']//div[contains(@class,'carousel-inner')]//div[@class='imageSection']//following-sibling::p)[{0}]"
    _add_to_fav_link = "(//i[contains(@sectionofpage,'{0}')])[1]"
    # _OK_button = "(//button[text()='OK'])[1]"
    # _success_msg = "//div[contains(text(),'Added to your favourites.')]"
    _favourite_items = "//ul[@id='lightSlider2a']//li//div[@class='carousel-inner']//div[@class='descriptionSection']//p"    
    _user_icon = "(//a[@id='navbarDropdownMenuLinka'])[1]"
    _my_favourites_link = "//div[contains(@class,'dropdown-menu-right show')]//a[text()='My favourites']"
    _remove_icon = "(//ul[@id='lightSlider2a']//li//i)[{0}]"    
    _delete_confirmation = "delete"
    _delete_alert = "//input[@id='checkLastElement']//following-sibling::button"
    _max_5_fav_msg = "favouriteModalIdDashboard"
    _OK_added_to_favourites = "//button[@class='btn btn-primary btn-sm']"
    
    def count_of_favourites(self):        
        self.elementClick(self._user_icon, locatorType='xpath')
        favourites_link = self.getElement(self._my_favourites_link, locatorType='xpath')
        actions = ActionChains(self.driver)
        actions.move_to_element(favourites_link).click().perform()
        config.count = self.driver.find_elements_by_xpath(self._favourite_items)
        for c in config.count:
            c_text = c.get_attribute("innerText")
            config.text_on_fav_items.append(c_text)
            self.log.info("Item appended to Favourites list [%s]", c_text)
        return len(config.count)            

    def remove_from_favourites(self):        
        item_to_be_deleted = self.getElement(self._remove_icon.format(randint(1,len(config.count))), locatorType='xpath')   
        self.driver.execute_script("arguments[0].scrollIntoView(true);", item_to_be_deleted)            
        self.driver.execute_script("arguments[0].click();", item_to_be_deleted)  
        time.sleep(2)          
        confirmation_button = self.getElement(self._delete_confirmation)            
        self.driver.execute_script("arguments[0].scrollIntoView(true);", confirmation_button)
        self.driver.execute_script("arguments[0].click();", confirmation_button) 
        self.log.info("Clicked OK on Confirmation")                
        time.sleep(2)       
        alert_button = self.getElement(self._delete_alert, locatorType='xpath')            
        self.driver.execute_script("arguments[0].scrollIntoView(true);", alert_button)
        self.driver.execute_script("arguments[0].click();", alert_button)
        self.log.info("Clicked OK on Alert")            

    def add_to_favouritefn(self):        
        elements=[]   
        try:            
            #self.log.info("Inside add_to_favourite()")
            #import pdb; pdb.set_trace()
            if self.count_of_favourites() == 5:                
                self.remove_from_favourites()
                self.nav.navigateToHomePage()
                elements=self.driver.find_elements_by_xpath(self._category_tiles)
                for e in range(1, len(elements)):
                    # cat_hovered = elements[randint(0, len(elements) - 1)]
                    # self.log.info("Category idetified randomly %s", cat_hovered)
                    # text_cat_hovered = cat_hovered.text
                    tile = self.getElement(self._individual_category_tile.format(e), locatorType='xpath')
                    tile_text = tile.get_attribute("innerText")
                    if tile_text not in config.text_on_fav_items:
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", elements[e-1])
                        time.sleep(2)
                        actions = ActionChains(self.driver)
                        actions.move_to_element(elements[e-1]).perform()
                        self.log.info("Hovered to element [%s]", tile_text)
                        time.sleep(2)
                        #import pdb; pdb.set_trace()
                        fav_link = self._add_to_fav_link.format(tile_text)
                        target = self.driver.find_element_by_xpath(fav_link)
                        self.driver.execute_script("arguments[0].click();", target)
                        time.sleep(2) 
                        self.log.info("Clicked on the add to favourites icon")
                        if "Maximum of five can be added as favourite." in self.getElement(self._max_5_fav_msg).text:
                            break 
                        else:
                            OK_button = self.getElement(self._OK_added_to_favourites, locatorType='xpath')
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", OK_button)
                            self.driver.execute_script("arguments[0].click();", OK_button)                      
            else:
                self.nav.navigateToHomePage()                
                elements=self.driver.find_elements_by_xpath(self._category_tiles)
                for e in range(1, len(elements)):
                    tile = self.getElement(self._individual_category_tile.format(e), locatorType='xpath')
                    tile_text = tile.get_attribute("innerText")
                    if tile_text not in config.text_on_fav_items:
                        #import pdb; pdb.set_trace()
                        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", elements[e-1])
                        time.sleep(2)
                        actions = ActionChains(self.driver)
                        actions.move_to_element(elements[e-1]).perform()
                        self.log.info("Hovered to element [%s] ", tile_text)
                        time.sleep(2)
                        #import pdb; pdb.set_trace()
                        fav_link = self._add_to_fav_link.format(tile_text)
                        target = self.driver.find_element_by_xpath(fav_link)
                        self.driver.execute_script("arguments[0].click();",target)
                        time.sleep(2) 
                        self.log.info("Clicked on the add to favourites icon")
                        #import pdb; pdb.set_trace()                        
                        if "Maximum of five can be added as favourite." in self.getElement(self._max_5_fav_msg).text:
                            break 
                        else:
                            OK_button = self.getElement(self._OK_added_to_favourites, locatorType='xpath')
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", OK_button)
                            self.driver.execute_script("arguments[0].click();", OK_button)                      

        except Exception as e:
            self.log.error("Could not click on hovered tile link [%s]",e) 
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))  

    def verifyAddToFavourite(self):        
        if "Maximum of five can be added as favourite." in self.getElement(self._max_5_fav_msg).text:            
            return True
        else:
            return False    



            
               

    
    
