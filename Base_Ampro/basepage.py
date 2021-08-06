"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
from base_Ampro.selenium_driver import SeleniumDriver
from utilities_Ampro.util import Util
from selenium.webdriver.common.keys import Keys
import time, os.path
import traceback
import utilities_Ampro.custom_logger as cl
import logging

class BasePage(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super().__init__(driver)
        self.driver = driver
        self.util = Util(self.driver)

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            traceback.print_stack()
            return False

    def verifyFileSharing(self, _share_icons_all, _email, _comment, Email, Comment, _share_button, _success_msg, _close_button):
        try:
            self.util.fileSharingIcon(_share_icons_all,_email,_comment,Email,Comment,_share_button)
            actualText = self.getElement(_success_msg)                                  
            result = self.util.verifyTextMatch(actualText.get_attribute("innerText"), "Shared successfully")
            self.elementClick(_close_button,locatorType="xpath")
            time.sleep(2)
            self.driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
            time.sleep(2)
            return result
        except:
            self.log.error("Failed insde base class - could not close share pop")
            traceback.print_stack()
            return False


    def verifyTextOnModal(self, _modal_text, textToVerify):
        """
        Verify the text on Modal 

        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualText = self.getElement(_modal_text).text
            return self.util.verifyTextContains(actualText, textToVerify)
        except:
            self.log.error("Failed to get modal text")
            traceback.print_stack()
            return False    

    def verifyCaraouselItems(self,expected_list, actual_list):
        return self.util.verifyListMatch(expected_list, actual_list)

    def verifyDownload(self, first, last, ext):
        #import pdb;pdb.set_trace()
        path=self.util.dynamic_file_path(first, last, ext)
        self.log.info("Dynamic file path [%s]",path)
        result=os.path.isfile(path)
        self.log.info("File download complete [%s]", result)
        return result    

