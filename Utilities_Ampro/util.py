"""
@package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import time
import traceback
import random, string
import utilities_Ampro.custom_logger as cl
import logging
from selenium.webdriver.common.keys import Keys
from random import randint
from base_Ampro.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
from configfiles_ampro import config

class Util(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def getAlphaNumeric(self, length, type='letters'):
        """
        Get random string of characters

        Parameters:
            length: Length of string, number of characters string should have
            type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        Get a list of valid email ids

        Parameters:
            listSize: Number of names. Default is 5 names in a list
            itemLength: It should be a list containing number of items equal to the listSize
                        This determines the length of the each item in the list -> [1, 2, 3, 4, 5]
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyTextContains(self, actualText, expectedText):
        """
        Verify actual text contains expected text string

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self, actualText, expectedText):
        """
        Verify text match

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if actualText.lower() == expectedText.lower():
            self.log.info("### TEXT MATCHED !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches

        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        Parameters:
            expectedList: Expected List
            actualList: Actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True

    def fileSharingbutton(self,Email,Comment): 
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(2)
        links=[]
        #import pdb;pdb.set_trace()
        links = self.driver.find_elements_by_css_selector(self._share_icon)
        l = links[randint(0, len(links) - 1)]
        l.click()
        time.sleep(2)
        self.sendKeys(Email,self._email)
        time.sleep(2)
        self.sendKeys(Comment,self._comment)
        time.sleep(2)
        self.elementClick(self._share_button) 

    def fileSharingIcon(self,_share_icons_all,_email,_comment,Email,Comment,_share_button): 
        try: 
            all_icons = self.driver.find_elements_by_id(_share_icons_all)
            for all in range(len(all_icons)):
                share = all_icons[(randint(0, len(all_icons)-1))] 
                self.log.info("Share icon selected as [%s]",share.text) 
                if share.is_displayed():                
                    self.driver.execute_script("arguments[0].scrollIntoView({behaviour: 'smooth', block: 'end', inline: 'end'});", share)
                    time.sleep(4)
                    self.driver.execute_script("arguments[0].click();", share)  
                    self.sendKeys(Email,_email)
                    time.sleep(2)
                    self.sendKeys(Comment,_comment)
                    time.sleep(2)
                    self.elementClick(_share_button)
                    time.sleep(2)
                    break
                else:
                    continue
        except:
            self.log.error("Failed inside util-could not click on share button on pop up")
            traceback.print_stack()  

    def dynamic_file_path(self, first, last, ext):           
        sys_download = "C:/Users/pratishtha.bhadula/Downloads/"        
        final_first = ''.join(e for e in first.strip() if e.isalnum())
        final_last = ''.join(e for e in last.strip() if e.isalnum())
        result = sys_download + final_first + "-" + final_last + ext 
        return result            


    # def count_of_favourites(self, _user_icon, _my_favourites_link, _fav_tab_sd, _favourite_items):        
    #     self.elementClick(_user_icon, locatorType='xpath')
    #     favourites_link = self.getElement(_my_favourites_link, locatorType='xpath')
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(favourites_link).click().perform()
    #     if self.isElementPresent(_fav_tab_sd, locatorType='xpath'):
    #         config.count = self.driver.find_elements_by_xpath(_favourite_items)
    #         for c in config.count:
    #             c_text = c.get_attribute("innerText")
    #             config.text_on_fav_items.append(c_text)
    #             self.log.info("Item appended to Favourites list [%s]", c_text)
    #         return len(config.count) 
    #     else:
    #         return 0               

    # def remove_from_favourites(self,_remove_icon,_delete_confirmation,_delete_alert):        
    #     item_to_be_deleted = self.getElement(_remove_icon.format(randint(1,len(config.count))), locatorType='xpath')   
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", item_to_be_deleted)            
    #     self.driver.execute_script("arguments[0].click();", item_to_be_deleted)  
    #     time.sleep(2)          
    #     confirmation_button = self.getElement(_delete_confirmation)            
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", confirmation_button)
    #     self.driver.execute_script("arguments[0].click();", confirmation_button) 
    #     self.log.info("Clicked OK on Confirmation")                
    #     time.sleep(2)       
    #     alert_button = self.getElement(_delete_alert, locatorType='xpath')            
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", alert_button)
    #     self.driver.execute_script("arguments[0].click();", alert_button)
    #     self.log.info("Clicked OK on Alert")            

    # def add_to_favouritefn(self,_user_icon, _my_favourites_link, _fav_tab_sd, _favourite_items,_remove_icon,_delete_confirmation,_delete_alert):        
    #     elements=[]   
    #     try:            
    #         #self.log.info("Inside add_to_favourite()")
    #         #import pdb; pdb.set_trace()
    #         if self.count_of_favourites(_user_icon, _my_favourites_link, _fav_tab_sd, _favourite_items) == 5:                
    #             self.remove_from_favourites(_remove_icon,_delete_confirmation,_delete_alert)
    #             self.nav.navigateToHomePage()
    #             elements=self.driver.find_elements_by_xpath(self._category_tiles)
    #             for e in range(1, len(elements)):
    #                 # cat_hovered = elements[randint(0, len(elements) - 1)]
    #                 # self.log.info("Category idetified randomly %s", cat_hovered)
    #                 # text_cat_hovered = cat_hovered.text
    #                 tile = self.getElement(self._individual_category_tile.format(e), locatorType='xpath')
    #                 tile_text = tile.get_attribute("innerText")
    #                 if tile_text not in config.text_on_fav_items:
    #                     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", elements[e-1])
    #                     time.sleep(2)
    #                     actions = ActionChains(self.driver)
    #                     actions.move_to_element(elements[e-1]).perform()
    #                     self.log.info("Hovered to element [%s]", tile_text)
    #                     time.sleep(2)
    #                     #import pdb; pdb.set_trace()
    #                     fav_link = self._add_to_fav_link.format(tile_text)
    #                     target = self.driver.find_element_by_xpath(fav_link)
    #                     self.driver.execute_script("arguments[0].click();", target)
    #                     time.sleep(2) 
    #                     self.log.info("Clicked on the add to favourites icon")
    #                     if "Maximum of five can be added as favourite." in self.getElement(self._max_5_fav_msg).text:
    #                         break 
    #                     else:
    #                         OK_button = self.getElement(self._OK_added_to_favourites, locatorType='xpath')
    #                         self.driver.execute_script("arguments[0].scrollIntoView(true);", OK_button)
    #                         self.driver.execute_script("arguments[0].click();", OK_button)                      
    #         else:
    #             self.nav.navigateToHomePage()                
    #             elements=self.driver.find_elements_by_xpath(self._category_tiles)
    #             for e in range(1, len(elements)):
    #                 tile = self.getElement(self._individual_category_tile.format(e), locatorType='xpath')
    #                 tile_text = tile.get_attribute("innerText")
    #                 if tile_text not in config.text_on_fav_items:
    #                     #import pdb; pdb.set_trace()
    #                     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", elements[e-1])
    #                     time.sleep(2)
    #                     actions = ActionChains(self.driver)
    #                     actions.move_to_element(elements[e-1]).perform()
    #                     self.log.info("Hovered to element [%s] ", tile_text)
    #                     time.sleep(2)
    #                     #import pdb; pdb.set_trace()
    #                     fav_link = self._add_to_fav_link.format(tile_text)
    #                     target = self.driver.find_element_by_xpath(fav_link)
    #                     self.driver.execute_script("arguments[0].click();",target)
    #                     time.sleep(2) 
    #                     self.log.info("Clicked on the add to favourites icon")
    #                     #import pdb; pdb.set_trace()                        
    #                     if "Maximum of five can be added as favourite." in self.getElement(self._max_5_fav_msg).text:
    #                         break 
    #                     else:
    #                         OK_button = self.getElement(self._OK_added_to_favourites, locatorType='xpath')
    #                         self.driver.execute_script("arguments[0].scrollIntoView(true);", OK_button)
    #                         self.driver.execute_script("arguments[0].click();", OK_button)                      

    #     except Exception as e:
    #         self.log.error("Could not click on hovered tile link [%s]",e) 
    #         self.log.error("Exception Caught: {}".format(traceback.format_exc()))
    #         self.log.error("".join(traceback.format_stack()))  
        
