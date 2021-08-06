from base_Ampro.basepage import BasePage
from selenium.webdriver import ActionChains
import utilities_Ampro.custom_logger as cl
import logging, time, traceback
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from configfiles_ampro import config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class CreateNewStrategyPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _categories_dropdown="//div[@id='navbarNavDropdown']/div/ul[2]/li[1]/a"
    _category="//section[@id='loadTopCategory']//aside"
    _category_breadcrumb="//div[contains(@class,'pageheading')]//a[@id='clickCategory']"
    _category_tiles="//div[@id='loadCategoryGroup']//div[contains(@class,'carousel-inner')]"
    #_category_tiles = "//div[@id='loadCategoryGroup']//div[contains(@class,'carousel-inner')]//a[text()='Insights reports']"
    _category_tile_link="(//a[contains(@sectionofpage,'{0}')])[1]"
    _select_category_drpdwn = "//select[@id='_Report']"
    _strategy_icon="(//div[contains(@class,'icons')]/a/i)[1]"
    #_insights_reports_tile="(//div[@id='loadReports1']//div[contains(@class,'catContainer border')]//div/img)[1]"
    _insights_reports_tile ="(//div[@id='loadReports1']//div[contains(@class,'catContainer border')])[1]"
    _continue_button="IdContinue"
    _questions="//form[contains(@class,'qaForm margin0')]//div//span[contains(@class,'quesNum')]//parent::label"
    _first_answer="(//form[contains(@class,'qaForm margin0')]//div[{0}]//li[1]//div[contains(@class,'radio-btn')]//label)[1]"
    _show_my_strategy_button="btnQASubmit"
    _strategy_plot="strategeyDiv"

    def create_new_strategy_home_page(self):
        elements=[]     
        elements=self.driver.find_elements_by_xpath(self._category_tiles)
        try:
            for x in elements:
            #self.log.info("Inside loop")
                cat_hovered=elements[randint(0, len(elements) - 1)]
                self.log.info("Category idetified randomly %s", cat_hovered)
                text_cat_hovered=self.getText(element=cat_hovered)
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", cat_hovered)
                time.sleep(4)
                action1 = ActionChains(self.driver)
                action1.move_to_element(cat_hovered).perform()
                self.log.info("Hovered to element [%s]", cat_hovered)
                time.sleep(2)
                report_link = self._category_tile_link.format(text_cat_hovered)
                target = self.driver.find_element_by_xpath(report_link)
                target_text=self.getText(element=target)
                self.log.info("Link text on category tile [%s]", target_text)
                if target_text not in "Insights reports":
                    continue
                else:
                    break
            self.driver.execute_script("arguments[0].click();",target)
            time.sleep(4)
            #self.log.info("Landed on insight reports page %s",self.isElementPresent(self._random_click_insight_reports,locatorType="xpath"))
            tile=self.waitForElement(self._insights_reports_tile,locatorType="xpath")
            action2 = ActionChains(self.driver)
            action2.move_to_element(tile).perform()
            self.log.info("Tile found [%s] [%s]",tile.is_displayed(),tile)
            self.log.info("Hovered over Insight reports tile")
            icon=self.getElement(self._strategy_icon,locatorType="xpath")
            self.log.info("Strategy icon identified [%s]",icon)
            action2.move_to_element(icon).click().perform()
            self.waitForElement("iframeAutoLogin")
            self.driver.switch_to.frame("iframeAutoLogin")
            # create new strategy for a selected category from dropdown          
            time.sleep(2)
            self.elementClick(self._continue_button)            
            for q in range(1,14):
                answer_clicked = self.getElement(self._first_answer.format(q),locatorType="xpath")
                self.log.info("Answer selected [%s]",self.getText(element=answer_clicked))
                self.driver.execute_script("arguments[0].click();",answer_clicked)
                self.log.info("Question [%s] answered",q)
                time.sleep(2)
                
            #self.driver.find_element_by_tag_name('body').send_keys(Keys.END)    
            submit_button = self.getElement(self._show_my_strategy_button)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'end', inline: 'end'});", submit_button)
            self.driver.execute_script("arguments[0].click();",submit_button)
            time.sleep(3)

        except Exception as e:
                self.log.error("Could not click on hovered tile link [%s]",e) 
                self.log.error("Exception Caught: {}".format(traceback.format_exc()))
                self.log.error("".join(traceback.format_stack()))                
                                  
            
    def verifycreatenewstrategy(self):
        result = self.isElementPresent(self._strategy_plot)
        return result
                 

    
    
