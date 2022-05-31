from base_Ampro.basepage import BasePage
from selenium.webdriver import ActionChains
import utilities_Ampro.custom_logger as cl
import logging, time, traceback
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from configfiles_ampro import config

class CategoriesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _categories_dropdown="//ul[@class='navbar-nav mt-3']//li[2]"
    _category_links="//ul[@class='navbar-nav mt-3']//li[2]//aside//a"
    _category_breadcrumb="//div[contains(@class,'pageheading')]//a[@id='clickCategory']"
    _category_tiles="//div[@id='loadCategoryGroup']//div[contains(@class,'carousel-inner')]"
    _category_tile_link="(//a[contains(@sectionofpage,'{0}')])[1]"
    _tabs_categories_view = "//ul[@id='reportTabsId']//li//a"
    _breadcrumb = "//div[contains(@class,'pageheading')]//li[contains(@class,'breadcrumb-item active')]"
    _category_News = "(//div[@class='News'])[1]//a"   
    

    def navigateToCategoryViaTopMenu(self):
        self.elementClick(locator=self._categories_dropdown,locatorType="xpath") 
        time.sleep(2)
        #import pdb;pdb.set_trace()
        links = self.driver.find_elements_by_xpath(self._category_links)
        link_selected = links[randint(0, len(links) - 1)]
        config.text_on_dropdown_item = self.getText(element=link_selected)
        self.driver.execute_script("arguments[0].click();", link_selected)
        time.sleep(2)

    def clickOnEachTabOnCategoryView(self):
        elements = self.driver.find_elements_by_xpath(self._tabs_categories_view)  
        for ele in elements:
            self.driver.execute_script("arguments[0].click();", ele)
            time.sleep(2)
            config.text_cat_hovered = ele.get_attribute("innerText") 
            config.text_on_breadcrumb = self.getText(self._breadcrumb,locatorType='xpath')
            config.final_result.append(self.util.verifyTextMatch(config.text_cat_hovered, config.text_on_breadcrumb))

    def verifyClickOnEachTab(Self):
        if False in config.final_result:
            return False
        else:
            return True  

    def clickCategoryNews(self):
        global allHandles
        elements = self.driver.find_elements_by_xpath(self._category_News)
        news_item_selected = elements[randint(0,len(elements)-1)]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", news_item_selected)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", news_item_selected) 
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent handle for the current page identified [%s]", parentHandle)                   
        allHandles = self.driver.window_handles
        self.log.info("There are now 2 windows with different handles [%s]", len(allHandles))
        for handle in allHandles:
            self.log.info("At Handle [%s]", handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                time.sleep(2)                
                #import pdb; pdb.set_trace()
                self.driver.close()
                break
        self.driver.switch_to.window(parentHandle)  

    def verifyNewsItemClicked(self):
        if len(allHandles) == 2:
            return True 
        else:
            return False
                               

    def navigateToCategoryViaHomepg(self):
        elements=[]     
        try:
            elements = self.driver.find_elements_by_xpath(self._category_tiles)
            cat_hovered = elements[randint(0, len(elements) - 1)]
            config.text_cat_hovered = cat_hovered.get_attribute("innerText")
            self.log.info("Text on category tile selected to be clicked [%s]", config.text_cat_hovered)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'end', inline: 'end'});", cat_hovered)
            time.sleep(4)
            actions = ActionChains(self.driver)
            actions.move_to_element(cat_hovered).perform()
            self.log.info("Hovered to element [%s]", cat_hovered)
            time.sleep(2)
            report_link = self._category_tile_link.format(config.text_cat_hovered)
            target = self.driver.find_element_by_xpath(report_link)
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", target)
            #actions.move_to_element(config.target).click().perform()
            time.sleep(4)                               
        except Exception as e:
            self.log.error("Could not click on hovered tile link [%s]",e) 
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))  
         
    def verifyNavigationToCategoryViaTopMenu(self):
        text_on_breadcrumb = self.getText(locator=self._category_breadcrumb,locatorType="xpath")
        return self.util.verifyTextMatch(text_on_breadcrumb, config.text_on_dropdown_item)           

    def verifyNavigationToCategoryViaHomepg(self):
        textafterclick=self.getText(locator=self._category_breadcrumb, locatorType="xpath")
        #import pdb;pdb.set_trace()
        return self.util.verifyTextMatch(textafterclick, config.text_cat_hovered)
        

                     

    
    
