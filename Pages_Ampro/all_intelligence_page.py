from base_Ampro.basepage import BasePage
from selenium.webdriver import ActionChains
import utilities_Ampro.custom_logger as cl
import logging, time, traceback, os.path
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from configfiles_ampro import config

class AllIntelligencePage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    #_all_intelligence="//div[@id='navbarNavDropdown']/div/ul[2]/li[2]/a"
    _all_intelligence="//ul[@class='navbar-nav mt-3']//li[3]"
    _insights_reports="rpTypeId_1"
    #_breadcrumb="//div[contains(@class,'pageheading')]//ol//li[3]//a"
    _breadcrumb="//div[contains(@class,'pageheading')]//li[@class='breadcrumb-item active']//a"
    _sustainability_trends="rpTypeId_2"
    _innovation_trends="rpTypeId_3"
    _mega_trends="rpTypeId_4"
    _Quarterly_category_briefings="rpTypeId_9" 
    _category_deep_dive="rpTypeId_20"   
    _CASME_insights="rpTypeId_6"
    _cost_structures_drivers="(//a[contains(text(),'Cost structures and drivers')])[1]"
    _commodities="//ul[@class='navbar-nav mt-3']//li[3]//a[contains(text(),'Commodities')]"
    _select_country="//div[@id='collapseFilter']//button[@title='--Select country--']"
    _select_cost_structure="//div[@id='collapseFilter']//button[@title='-- Select cost structure --']"    
    _first_country="(//ul[contains(@class,'multiselect-container dropdown-menu')]//li[3]//label)[1]"
    _first_cs="(//label[@title='-- Select cost structure --']//ancestor::li//following-sibling::li//a//label)[1]"
    _chart="//section[@class='chartArea']//div[@id='cs_chart']"    
    _commodity_group_c="(//div[@class='btn-group']//button//span)[1]"
    _region_country="(//div[@class='btn-group']//button//span)[2]"
    _commodity="(//div[@class='btn-group']//button//span)[3]" 
    _first_c_g="(//label[@title='--Select commodity group--'])[1]//ancestor::li//following-sibling::li[1]//label"
    _first_r_c="(//label[@title='-- Select country --'])[1]//ancestor::li//following-sibling::li[1]//label"
    _first_commodity="(//label[@title='-- Select commodity --'])[1]//ancestor::li//following-sibling::li[1]//label"
    _apply_button="//div[@id='collapseFilter']//button[contains(text(),'Apply')]"
    _apply_button2="applyFilter"
    _key_insights="overAllSummary"
    _first_c_g_sd="((//label[@title='-- Select --'])[1]//ancestor::li//following-sibling::li//label)[1]"
    _first_commodity_sd="((//label[@title='-- Select --'])[2]//ancestor::li//following-sibling::li//label)[1]"
    _first_dest_country_sd="((//label[@title='-- Select --'])[3]//ancestor::li//following-sibling::li)[1]//label"
    _tile_category_deep_dive = "//div[@class='catContainer border']//a[@sectionofpage='View report']"
    _header_on_reportdashboard = "//h1[@class='d-inline']"
    _tabs_quarterly_cat_briefings = "//ul[@id='reportTabsId']//li//a"
    
    def navigateToInsightsReports(self):
        actions = ActionChains(self.driver)
        first_link=self.getElement(self._insights_reports)
        actions.move_to_element(first_link).click().perform()
        self.log.info("Clicked on Insight Reports under All Intelligence top menu")
        time.sleep(4)

    def verifyNavigationToInsightsReports(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Insight reports [%s]",breadcrumb)        
        if text=="Insights reports":
            return True 
        else:
            return False

    def navigateToSustainabilityTrends(self):
        actions = ActionChains(self.driver)
        second_link=self.getElement(self._sustainability_trends)
        actions.move_to_element(second_link).click().perform()
        self.log.info("Clicked on Sustainability Trends under All Intelligence top menu")
        time.sleep(4)

    def verifyNavigationToSustainabilityTrends(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Sustainability reports [%s]",breadcrumb)        
        if text=="Sustainability trends":
            return True 
        else:
            return False        

    def navigateToInnovationTrends(self):
        actions = ActionChains(self.driver)
        third_link=self.getElement(self._innovation_trends)
        actions.move_to_element(third_link).click().perform()
        self.log.info("Clicked on Innovation trends under All intelligence top menu")
        time.sleep(4)

    def verifyNavigationToInnovationTrends(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Innovation trends [%s]",breadcrumb)
        if text=="Innovation trends":
            return True 
        else:
            return False 

    def navigateToMegaTrends(self):
        actions = ActionChains(self.driver)
        fourth_link=self.getElement(self._mega_trends)
        actions.move_to_element(fourth_link).click().perform()
        self.log.info("Clicked on Mega trends under All intelligence top menu")
        time.sleep(4)

    def verifyNavigationToMegaTrends(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Mega trends [%s]",breadcrumb)        
        if text=="Mega trends":
            return True 
        else:
            return False 

    def navigateToQuarterlyCategoryBriefings(self):
        actions = ActionChains(self.driver)
        fifth_link=self.getElement(self._Quarterly_category_briefings)
        actions.move_to_element(fifth_link).click().perform()
        self.log.info("Clicked on Category Briefings under All intelligence top menu")
        time.sleep(4)

    def verifyNavigationToQuarterlyCategoryBriefings(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Category briefings [%s]",breadcrumb)        
        if text=="Category briefings":
            return True 
        else:
            return False  
    
    def clickOnSectorTabs(self):
        elements = self.driver.find_elements_by_xpath(self._tabs_quarterly_cat_briefings)  
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

    def navigateToCategoryDeepDive(self):
        actions = ActionChains(self.driver)
        link=self.getElement(self._category_deep_dive)
        actions.move_to_element(link).click().perform()
        self.log.info("Clicked on Category deep-dive under All intelligence top menu")
        time.sleep(4) 
        

    def verifyReportFromCategoryDeepDive(self):
        return self.util.verifyTextMatch(config.text_on_new_window_header,config.text_on_category_deep_dive)

    def viewReportCategoryDeepDive(self):
        actions = ActionChains(self.driver)
        elements = self.getElements(self._tile_category_deep_dive,locatorType='xpath')
        element_to_be_clicked = elements[randint(0, len(elements))]
        config.text_on_category_deep_dive = element_to_be_clicked.text
        actions.move_to_element(element_to_be_clicked).click().perform()
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent handle for the current page identified [%s]", parentHandle)                   
        allHandles = self.driver.window_handles
        self.log.info("There are now 2 windows with different handles [%s]", len(allHandles))
        for handle in allHandles:
            self.log.info("At Handle [%s]", handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                time.sleep(4)
                config.text_on_new_window_header = self.getText(self._header_on_reportdashboard,locatorType='xpath')
                #import pdb; pdb.set_trace()
                self.driver.close()
                break
        self.driver.switch_to.window(parentHandle)

    def verifyNavigationToCategoryDeepDive(self):   
        actualText = self.getText(self._breadcrumb,locatorType='xpath')   
        return self.util.verifyTextMatch(actualText, "Category deep-dives")             

    def navigateToCASMEInsights(self):
        actions = ActionChains(self.driver)
        sixth_link=self.getElement(self._CASME_insights)
        actions.move_to_element(sixth_link).click().perform()
        self.log.info("Clicked on CASME insights under All intelligence top menu")
        time.sleep(4)

    def verifyNavigationToCASMEInsights(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to CASME insights [%s]",breadcrumb)        
        if text=="CASME insights":
            return True 
        else:
            return False 

    def navigateToCostStructuresNDrivers(self):
        actions = ActionChains(self.driver)
        seventh_link=self.getElement(self._cost_structures_drivers,locatorType="xpath")
        actions.move_to_element(seventh_link).click().perform()
        self.log.info("Clicked on Cost structures and drivers under All intelligence top menu")
        time.sleep(2)

    def chartFormation(self):
        try:
            self.elementClick(self._select_country,locatorType="xpath")
            self.log.info("Select country dropdown clicked on Cost Structures and drivers")
            actions = ActionChains(self.driver)
            element1=self.getElement(self._first_country,locatorType="xpath")
            actions.move_to_element(element1).click().perform()
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
        except Exception as e:
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
        if text=="Cost structures and drivers":
            return True 
        else:
            return False 

    def navigateToCommodities(self):
        actions = ActionChains(self.driver)
        eighth_link=self.getElement(self._commodities,locatorType="xpath")
        #import pdb;pdb.set_trace()
        actions.move_to_element(eighth_link).click().perform()
        self.log.info("Clicked on Commodities under All intelligence top menu")
        try:
            self.elementClick(self._commodity_group_c, locatorType="xpath")
            self.log.info("Select Commodity group dropdown clicked")            
            element1 = self.getElement(self._first_c_g, locatorType="xpath")
            self.driver.execute_script("arguments[0].click();", element1)
            self.log.info("First Commodity Group selected from dropdown")
            time.sleep(2)
            self.elementClick(self._region_country,locatorType="xpath")
            self.log.info("Select Region/Country dropdown clicked")
            element2=self.getElement(self._first_r_c,locatorType="xpath")
            self.driver.execute_script("arguments[0].click();", element2)
            time.sleep(2)
            self.elementClick(self._commodity,locatorType="xpath")
            self.log.info("Select Destination Country dropdown clicked")            
            element3=self.getElement(self._first_commodity,locatorType="xpath")
            self.driver.execute_script("arguments[0].click();", element3)
            time.sleep(2)
            self.elementClick(self._apply_button,locatorType='xpath')
            self.log.info("Filter applied")
            time.sleep(2)                      
        except Exception as e:
            self.log.error("Could not click on hovered tile link [%s]",e) 
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))
        time.sleep(4)

    def verifyNavigationToCommodities(self):
        breadcrumb=self.getElement(self._breadcrumb,locatorType = "xpath")
        text=self.getText(element=breadcrumb)
        self.log.info("Redirected to Commodities [%s]",breadcrumb)        
        if text=="Commodities":
            return True 
        else:
            return False      

    def dynamic_file_path(self):
           
        first = "C:/Users/pratishtha.bhadula/Downloads/"
        last = ".xlsx"
        final_commodity = ''.join(e for e in config.text_commodity if e.isalnum())
        final_country = ''.join(e for e in config.text_country if e.isalnum())
        result = first + final_commodity + "-" + final_country + last 
        return result

            

    def verifyDownload(self):
        #import pdb;pdb.set_trace()
        path=self.dynamic_file_path()
        self.log.info("Dynamic file path [%s]",path)
        result=os.path.isfile(path)
        self.log.info("File download complete [%s]",result)
        return result
                  

            
                                                      


        
    
