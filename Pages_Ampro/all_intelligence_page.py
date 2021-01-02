from Base_Ampro.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
import Utilities_Ampro.custom_logger as cl
import logging, time, traceback
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

class AllIntelligencePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _all_intelligence="//div[@id='navbarNavDropdown']/div/ul[2]/li[4]/a"
    _insights_reports="(//a[contains(text(),'Insights reports')])[1]"
    _breadcrumb="//div[contains(@class,'pageheading')]//ol//li[3]//a"
    _sustainability_reports="(//a[contains(text(),'Sustainability reports')])[1]"
    _innovation_trends="(//a[contains(text(),'Innovation trends')])[1]"
    _mega_trends="(//a[contains(text(),'Mega trends')])[1]"
    _category_briefings="(//a[contains(text(),'Category briefings')])[1]"    
    _CASME_insights="(//a[contains(text(),'CASME insights')])[1]"
    _cost_structures_drivers="(//a[contains(text(),'Cost structures and drivers')])[1]"
    _commodities="(//a[contains(text(),'Commodities')])[1]"
    _select_country="//div[@id='collapseFilter']//button[@title='--Select country--']"
    _select_cost_structure="//div[@id='collapseFilter']//button[@title='-- Select cost structure --']"
    _apply_button="//div[@id='collapseFilter']//button[contains(text(),'Apply')]"
    _first_country="(//ul[contains(@class,'multiselect-container dropdown-menu')]//li[3]//label)[1]"
    _first_cs="//div[@id='collapseFilter']/div[2]/span[2]/div/ul/li[3]/a/label"
    _chart="//div[@id='cs_chart']/div[2]"
    
    def navigateToAllIntelligence(self):
        self.elementClick(self._all_intelligence,locatorType="xpath")
        self.log.info("Clicked on All Intelligence top menu")

    def navigateToInsightsReports(self):
        action=ActionChains(self.driver)
        first_link=self.getElement(self._insights_reports,locatorType="xpath")
        action.move_to_element(first_link).click().perform()
        self.log.info("Clicked on Insight Reports under All Intelligence top menu")
        time.sleep(4)

    def verifyNavigationToInsightsReports(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Insight reports [%s]",breadcrumb)
        attribute_value=breadcrumb.get_attribute("pagename")
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Insights reports" and attribute_value=="All intelligence - Insights reports":
            return True 
        else:
            return False

    def navigateToSustainabilityReports(self):
        action=ActionChains(self.driver)
        second_link=self.getElement(self._sustainability_reports,locatorType="xpath")
        action.move_to_element(second_link).click().perform()
        self.log.info("Clicked on Sustainability Reports under All Intelligence top menu")
        time.sleep(4)

    def verifyNavigationToSustainabilityReports(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Sustainability reports [%s]",breadcrumb)
        attribute_value=breadcrumb.get_attribute("pagename")
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Sustainability reports" and attribute_value=="All intelligence - Sustainability reports":
            return True 
        else:
            return False        

    def navigateToInnovationTrends(self):
        action=ActionChains(self.driver)
        third_link=self.getElement(self._innovation_trends,locatorType="xpath")
        action.move_to_element(third_link).click().perform()
        self.log.info("Clicked on Innovation trends under All intelligence top menu")
        time.sleep(4)

    def verifyNavigationToInnovationTrends(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Innovation trends [%s]",breadcrumb)
        attribute_value=breadcrumb.get_attribute("pagename")
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Innovation trends" and attribute_value=="All intelligence - Innovation trends":
            return True 
        else:
            return False 

    def navigateToMegaTrends(self):
        action=ActionChains(self.driver)
        fourth_link=self.getElement(self._mega_trends,locatorType="xpath")
        action.move_to_element(fourth_link).click().perform()
        self.log.info("Clicked on Mega trends under All intelligence top menu")
        time.sleep(4)

    def verifyNavigationToMegaTrends(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Mega trends [%s]",breadcrumb)
        attribute_value=breadcrumb.get_attribute("pagename")
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Mega trends" and attribute_value=="All intelligence - Mega trends":
            return True 
        else:
            return False 

    def navigateToCategoryBriefings(self):
        action=ActionChains(self.driver)
        fifth_link=self.getElement(self._category_briefings,locatorType="xpath")
        action.move_to_element(fifth_link).click().perform()
        self.log.info("Clicked on Category Briefings under All intelligence top menu")
        time.sleep(4)

    def verifyNavigationToCategoryBriefings(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Category briefings [%s]",breadcrumb)
        attribute_value=breadcrumb.get_attribute("pagename")
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Category briefings" and attribute_value=="All intelligence - Category briefings":
            return True 
        else:
            return False 

    def navigateToCASMEInsights(self):
        action=ActionChains(self.driver)
        sixth_link=self.getElement(self._CASME_insights,locatorType="xpath")
        action.move_to_element(sixth_link).click().perform()
        self.log.info("Clicked on CASME insights under All intelligence top menu")
        time.sleep(4)

    def verifyNavigationToCASMEInsights(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to CASME insights [%s]",breadcrumb)
        attribute_value=breadcrumb.get_attribute("pagename")
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="CASME insights" and attribute_value=="All intelligence - CASME insights":
            return True 
        else:
            return False 

    def navigateToCostStructuresNDrivers(self):
        action=ActionChains(self.driver)
        seventh_link=self.getElement(self._cost_structures_drivers,locatorType="xpath")
        action.move_to_element(seventh_link).click().perform()
        self.log.info("Clicked on Cost structures and drivers under All intelligence top menu")
        time.sleep(2)

    def chartFormation(self):
        try:
            self.elementClick(self._select_country,locatorType="xpath")
            self.log.info("Select country dropdown clicked on Cost Structures and drivers")
            action=ActionChains(self.driver)
            element1=self.getElement(self._first_country,locatorType="xpath")
            action.move_to_element(element1).click().perform()
            self.log.info("First country selected from dropdown")
            time.sleep(2)
            self.elementClick(self._select_cost_structure,locatorType="xpath")
            self.log.info("Select cost structure dropdown clicked on Cost Structures and drivers")
            time.sleep(2)
            element2=self.getElement(self._first_cs,locatorType="xpath")
            self.driver.execute_script("arguments[0].click();",element2)
            self.log.info("First cost structure selected")
            time.sleep(2)
            self.elementClick(self._apply_button,locatorType="xpath")
            self.log.info("Apply button clicked")
            time.sleep(2)
        except:
            self.log.error("Could not click on hovered tile link [%s]",e) 
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))  

    def verifyChartFormation(self):
        result=self.isElementPresent(self._chart,locatorType="xpath")
        if result == True:
            return result
        else:
            return False   

    def verifyNavigationToCostStructuresNDrivers(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Cost structures and drivers [%s]",breadcrumb)
        attribute_value=breadcrumb.get_attribute("pagename")
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Cost structures and drivers" and attribute_value=="All intelligence - Cost structures and drivers":
            return True 
        else:
            return False 

    def navigateToCommodities(self):
        action=ActionChains(self.driver)
        eighth_link=self.getElement(self._commodities,locatorType="xpath")
        #import pdb;pdb.set_trace()
        action.move_to_element(eighth_link).click().perform()
        self.log.info("Clicked on Commodities under All intelligence top menu")
        time.sleep(4)

    def verifyNavigationToCommodities(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Commodities [%s]",breadcrumb)
        attribute_value=breadcrumb.get_attribute("pagename")
        self.log.info("Attribute value for pagename on breadcrumb [%s]",attribute_value)
        if text=="Commodities" and attribute_value=="All intelligence - Commodities":
            return True 
        else:
            return False 
            
                                                      


        
    
