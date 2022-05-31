from inspect import stack
from pdb import set_trace
from base_Ampro.basepage import BasePage
import utilities_Ampro.custom_logger as cl
import logging, time, os.path
import random, traceback
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from configfiles_ampro import config
from traceback import print_stack

class ToolsnTemplatesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    _ampro_logo = "(//nav[@id='tsc_nav_1']/a/img)[1]"
    _tools_n_templates = "//ul[@class='navbar-nav mt-3']//li[4]" 
    _tools_templates_breadcrumb = "//div[@class='row']//li[contains(@class,'breadcrumb-item active')]"    
    _email = "shareEmail"
    _comment = "shareComment"
    _share_icons = "shareTools"
    _share_button = "btnShareTools"
    _share_success_msg = "errorMsgShare"    
    _strategy_tool = "(//div[@id='loadToolsData']//a)[1]"
    _create_strategy_radio_2 = "radio2"
    _continue_button = "//div[@id='div2']//a" 
    _Saved_Strategy = "//div[@class='col-sm-12 text-right']//a[@title='Saved Strategy']"   
    _questions="//form[contains(@class,'qaForm margin0')]//div//span[contains(@class,'quesNum')]//parent::label"
    _individual_question = "(//form[contains(@class,'qaFormExternal margin0')]//span[contains(@class,'quesNum')]//parent::label)[{0}]" 
    _all_options = "(//span[contains(@class,'quesNum')]//parent::label)[{0}]//following-sibling::ul//li//label"  
    _continue_button_SP = "//button[@id='btnQASubmit1']" 
    _show_my_strategy_button = "//button[@id='btnQASubmit']"
    _demand_power_header = "//h1[contains(text(),'Demand power')]"
    _strategy_plot = "strategeyDiv"
    _cost_calculator = "(//div[@id='loadToolsData']//a)[2]"       
    _product_drpdwn = "//select[@id='drpCatCostCalc']" 
    _region_drpdwn = "//select[@id='drpRegCostCalc']"
    _currency_drpdwn = "//select[@id='drpCurrency']"
    _total_input_fields = "//form[@id='myform1']//tr[@class='d-block']//input[contains(@class,'form-control text-right decimalOnly inputrange')]"
    _individual_textbox = "(//form[@id='myform1']//tr[@class='d-block']//input[contains(@class,'form-control text-right decimalOnly inputrange')])[{0}]"
    _min_range = "(//form[@id='myform1']//tr[@class='d-block']//input[contains(@class,'form-control text-right decimalOnly inputrange')])[{0}]//following-sibling::input[1]"
    _max_range = "(//form[@id='myform1']//tr[@class='d-block']//input[contains(@class,'form-control text-right decimalOnly inputrange')])[{0}]//following-sibling::input[2]"
    #_calculate_button = "//input[@type='button']"
    _calculate_button = "//div[@id='inputtableL']//input[@id='calCostData']"
    _chart_header = "//div[@class='chartHeading']//h2"
    _close_button = "//div[@id='shareToolsPopUp']//div/button/span"
    _tabular_data ="//button[@id='tabButton']//span[contains(text(),'Tabular data')]"
    _cost_parameters = "//form[@id='myform']//th[contains(text(),'Cost parameters')]"
    #_net_profit_margin_chart = "//td[@class='text-center green_indicator']"
    _net_profit_margin_chart = "//table[@id='tableOutputdata']//td[2]"
    #_net_profit_margin_table = "//td[@class='text-right darkGray green_indicator']"
    _net_profit_margin_table = "//table//tr[@id='netProfitMarginInChartView']//td[3]"
    #_download_pdf = "//button[@id='btndownLoad']"
    _download_pdf = "//div[@class='chartHeading']//button"    
    _first_tooltip = "(//span[contains(@class,'fa-info-circle')])[1]"
    _banner = "(//div[@class='py-2 banner-image']//a//img)[1]"
    _close_strategy = "//div[contains(@class,'modal-header')]//button[@actionname='Strategy']//span"
    _close_cost_calculator = "//button[@actionname='Cost Calculator']//span"    

    def navigateToHome(self):
        self.elementClick(locator=self._ampro_logo,locatorType="xpath")

    def navigateToToolsnTemplates(self):
        self.elementClick(locator=self._tools_n_templates,locatorType="xpath") 
        #time.sleep(2)
        self.waitForVisibilityOfElement(self._strategy_tool, locatorType='xpath')

    def create_new_strategy_tools_templates(self):
        try:
            self.elementClick(self._strategy_tool, locatorType='xpath')          
            self.driver.switch_to.frame("iframeAutoLogin")
            self.waitForElement(self._continue_button, locatorType='xpath')
            self.elementClick(self._create_strategy_radio_2)            
            self.elementClick(self._continue_button, locatorType='xpath')
            #create new strategy for a different category from scratch          
            self.waitForElement(self._Saved_Strategy, locatorType='xpath')
            
            for q in range(1, 15):                
                question = self.getElement(self._individual_question.format(q),locatorType='xpath')  
                self.log.info("Question located [%s]", question.text)                         
                self.driver.execute_script("arguments[0].scrollIntoView(true);", question)                
                all_options = self.getElements(self._all_options.format(q), locatorType='xpath')
                chosen_answer = all_options[randint(0, len(all_options)-1)]
                self.log.info("Chosen answer for question [%s] is [%s]" % (q, chosen_answer))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", chosen_answer)
                self.driver.execute_script("arguments[0].click();", chosen_answer)
                time.sleep(2)
            Continue_button = self.getElement(self._continue_button_SP, locatorType='xpath')    
            self.driver.execute_script("arguments[0].click();",Continue_button)              
            self.waitForVisibilityOfElement(self._demand_power_header, locatorType='xpath')
            for q in range(1,13):
                question = self.getElement(self._individual_question.format(q),locatorType='xpath')                
                self.driver.execute_script("arguments[0].scrollIntoView(true);", question)
                all_options = self.getElements(self._all_options.format(q), locatorType='xpath')
                chosen_answer = all_options[randint(0, len(all_options)-1)]
                self.log.info("Chosen answer for question [%s] is [%s]" % (q, chosen_answer))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", chosen_answer)
                self.driver.execute_script("arguments[0].click();", chosen_answer)
                time.sleep(2)                  
            #self.driver.find_element_by_tag_name('body').send_keys(Keys.END)    
            submit_button = self.getElement(self._show_my_strategy_button, locatorType='xpath')
            self.driver.execute_script("arguments[0].click();", submit_button)
            self.waitForElement(self._strategy_plot)
        except Exception as e:
                self.log.error("Could not click on hovered tile link [%s]",e) 
                self.log.error("Exception Caught: {}".format(traceback.format_exc()))
                self.log.error("".join(traceback.format_stack()))                                        
            
    def verifyStrategyCreation(self):
        result = self.isElementPresent(self._strategy_plot)
        self.driver.switch_to.default_content()
        close_button = self.getElement(self._close_strategy, locatorType= 'xpath')
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
        # time.sleep(2)
        self.driver.execute_script("arguments[0].click();", close_button)
        time.sleep(2)
        return result

    def costCalculator(self): 
        try:                
            self.elementClick(self._cost_calculator,locatorType="xpath")                       
            self.driver.switch_to.frame("iframeAutoLoginCC")
            self.waitForElement(self._currency_drpdwn, locatorType='xpath')
            product_drpdwn = self.getElement(self._product_drpdwn, locatorType='xpath')
            sel = Select(product_drpdwn)
            #storing all options in product drpdwn in list1
            list1 = []
            list1 = sel.options
            product_count = len(list1)         
            self.log.info("Number of products in the list [%s]",product_count)
            sel.select_by_index(randint(0, product_count-1))
            config.product_selected = sel.first_selected_option.get_attribute("innerText")
            time.sleep(2)
            #finding region dropdown via xpath
            region_drpdwn = self.getElement(self._region_drpdwn, locatorType='xpath')
            sel2 = Select(region_drpdwn)
            list2 = []
            list2 = sel2.options
            region_count = len(list2)
            #import pdb;pdb.set_trace()
            self.log.info("Total number of regions corresponding to the Product selected [%s]",region_count)
            if region_count==1:
                sel2.select_by_index(0)
                config.region_selected = sel2.first_selected_option.get_attribute("innerText")
            else:
                sel2.select_by_index(randint(0,(region_count-1))) 
                config.region_selected = sel2.first_selected_option.get_attribute("innerText")  
            time.sleep(2)
            #finding currency dropdown
            currency_drpdwn = self.getElement(self._currency_drpdwn,locatorType='xpath')
            sel3 = Select(currency_drpdwn)
            list3 = []
            list3 = sel3.options
            currency_count = len(list3)
            #import pdb;pdb.set_trace()
            self.log.info("Total number of currencies corresponding to the Region selected [%s]",currency_count)
            if currency_count==1:
                sel3.select_by_index(0)
            else:
                sel3.select_by_index(randint(0,(currency_count-1)))
            
            input_parameters = []
            input_parameters = self.driver.find_elements_by_xpath(self._total_input_fields)
            #t_inputs = len(input_parameters)
            for i in range(1, len(input_parameters)):
                low_value_attribute = self.getElement(self._min_range.format(i), locatorType='xpath').get_attribute("value")
                low_value = float(low_value_attribute)         
                self.log.info("Lowest value detected [%s]", low_value)
                high_value_attribute = self.getElement(self._max_range.format(i), locatorType='xpath').get_attribute("value")
                high_value = float(high_value_attribute)
                self.log.info("Highest value detected [%s]", high_value)
                temp_value = random.uniform(low_value, high_value)
                final_value = round(temp_value, 1)
                self.log.info("Final value selected [%s]", final_value)
                self.sendKeys(str(final_value), self._individual_textbox.format(i), locatorType='xpath')
                time.sleep(2)
                #import pdb;pdb.set_trace()
            self.sendKeys(100, self._individual_textbox.format(len(input_parameters)), locatorType='xpath')
            time.sleep(1)
            calculate_button = self.getElement(self._calculate_button, locatorType='xpath')  
            #self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", calculate_button)      
            self.driver.execute_script("arguments[0].click();", calculate_button)
            config.net_profit_margin_chart = self.getText(self._net_profit_margin_chart, locatorType='xpath')
            time.sleep(2)
        except:
            self.log.error("### Exception Occurred !!!")
            print_stack()    

    def downloadPDF(self):
        self.elementClick(self._download_pdf, locatorType='xpath')
        time.sleep(14)           
        
    def verifyCostCalculator(self):
        try:
            chart_header = self.getElement(self._chart_header, locatorType='xpath')
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", chart_header)
            text_chart_header = chart_header.get_attribute("innerText")
            l1 = []
            l1 = text_chart_header.split("–", 1)
            l1[0] = l1[0].strip()
            l1[1] = l1[1].strip()
            #self.log.info("list l1 [%s]", l1)
            self.log.info("Region on Chart header detected [%s]", l1[0])
            self.log.info("Product on Chart header detected [%s]", l1[1])
            self.log.info("Text on Product selected via dropdown [%s]", config.product_selected)
            self.log.info("Text on Region selected via drodpown [%s]", config.region_selected)                        
            if (l1[1].lower()) == (config.product_selected.lower()) and (l1[0].lower()) == (config.region_selected.lower()):
                #import pdb;pdb.set_trace()
                return True
            else:
                return False
        except:
            self.log.error("### Exception Occurred !!!")
            print_stack() 

    def dynamic_file_path(self):
           
        first = "C:/Users/pratishtha.bhadula/Downloads/"
        #last = ".pdf"
        final_product = ''.join(e for e in config.product_selected.strip() if e.isalnum())
        final_region = ''.join(e for e in config.region_selected.strip() if e.isalnum())
        result = first + final_product + "-" + final_region + "-CostCal.pdf" 
        #result = first + final_product + "-" + final_region + "-CostCal"
        return result        

    def verifyDownloadPdf(self):
        #import pdb;pdb.set_trace()
        path=self.dynamic_file_path()
        self.log.info("Dynamic file path [%s]",path)
        result=os.path.isfile(path)
        self.log.info("File download complete [%s]",result)
        return result

    def clickOnCostCalculatorBanner(self):        
        global allHandles        
        parentHandle = self.driver.current_window_handle
        self.log.info("Parent handle for the current page identified [%s]",parentHandle)
        banner = self.getElement(self._banner, locatorType="xpath")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", banner)
        self.driver.execute_script("arguments[0].click();", banner)
        self.log.info("Clicked on CC Banner")
        time.sleep(2)        
        allHandles = self.driver.window_handles
        self.log.info("There are now 2 windows with different handles [%s]",len(allHandles))
        for handle in allHandles:
            self.log.info("At Handle [%s]", handle)
            if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                self.driver.close()
                break
        self.driver.switch_to.window(parentHandle)

    def verifyRedirectionOnBannerClick(self):             
        if len(allHandles) == 2:
            self.driver.switch_to.default_content()
            self.elementClick(self._close_cost_calculator, locatorType='xpath')
            return True 
        else:
            self.driver.switch_to.default_content()
            self.elementClick(self._close_cost_calculator, locatorType='xpath')
            return False 

    def tabularData(self):
        self.elementClick(self._tabular_data, locatorType='xpath')
        time.sleep(4)

    def verifyTabularData(self):        
        result=self.isElementPresent(self._cost_parameters, locatorType='xpath')
        return result
        #import pdb;pdb.set_trace()

    def verifyNetProfitMargin(self):    
        if self.getText(self._net_profit_margin_table,locatorType='xpath') == config.net_profit_margin_chart:
            #import pdb;pdb.set_trace()
            return True
        else:
            return False   

    #this method randomly clicks on the available share icons on page  
    def fileSharing(self, Email, Comment):
        try:                 
            return self.verifyFileSharing(self._share_icons, self._email, self._comment, Email, Comment, self._share_button,self._share_success_msg, self._close_button)
        except:  
            self.log.error("Could not call verifyFileSharing") 
            traceback.print_stack()  

    def verifyNavigationToToolsnTemplates(self):
        result=self.isElementPresent(self._tools_templates_breadcrumb,locatorType="xpath") 
        return result

       

    
