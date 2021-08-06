from selenium import webdriver
from pages_Ampro.tools_templates_page import ToolsnTemplatesPage
from utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from utilities_Ampro.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ToolsCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts = StatusCheck(self.driver)
        self.tnt = ToolsnTemplatesPage(self.driver)        
    
    @pytest.mark.run(order=28)
    def test_navigateToToolsnTemplates(self):            
        self.tnt.navigateToToolsnTemplates()
        result=self.tnt.verifyNavigationToToolsnTemplates()
        #import pdb;pdb.set_trace()
        self.ts.markFinal("test_navigateToToolsnTemplates", result,"Navigation to Tools & templates successful")

    @pytest.mark.run(order=29)
    def test_strategy_tool(self):  
        self.tnt.navigateToToolsnTemplates()          
        self.tnt.create_new_strategy_tools_templates()
        result=self.tnt.verifyStrategyCreation()
        #import pdb;pdb.set_trace()
        self.ts.markFinal("test_strategy_tool", result, "Creation of Strategy plot") 

    @pytest.mark.run(order=30)
    def test_cost_calculator(self):
        self.tnt.navigateToToolsnTemplates()            
        self.tnt.costCalculator()
        result=self.tnt.verifyCostCalculator()
        self.ts.markFinal("test_cost_calculator", result, "Cost Calculator chart formation")

    @pytest.mark.run(order=31)
    def test_tabular_view_cost_calculator(self): 
        self.tnt.tabularData()   
        result = self.tnt.verifyTabularData()
        self.ts.markFinal("test_tabular_view_cost_calculator", result, "Redirection to Tabular Data on Cost Calculator")

    @pytest.mark.run(order=32)
    def test_download_pdf_cost_calculator(self):    
        self.tnt.downloadPDF()
        result3=self.tnt.verifyDownloadPdf()
        self.ts.markFinal("test_download_pdf_cost_calculator", result3, "PDF Download for Cost Calculator")  

    @pytest.mark.run(order=33)
    def test_net_profit_margin(self):            
        result = self.tnt.verifyNetProfitMargin()
        self.ts.markFinal("test_net_profit_margin", result, "Net Profit Margin on chart view and tabular view")

    @pytest.mark.run(order=34)
    def test_banner_cost_calculator(self):    
        self.tnt.clickOnCostCalculatorBanner()
        result=self.tnt.verifyRedirectionOnBannerClick()
        self.ts.markFinal("test_cost_calculator", result, "Cost Calculator Banner click")       

    @pytest.mark.run(order=35)  
    @data(*getCSVData("D:/Python/Automation2020/AmplifiPROSanity/Test Data_Ampro/testdata_tools_n_templates.csv"))
    @unpack     
    def test_fileSharing(self,Email, Comment):   
        self.tnt.navigateToToolsnTemplates()     
        result= self.tnt.fileSharing(Email, Comment)
        #import pdb;pdb.set_trace()
        self.ts.markFinal("test_fileSharing", result, "File Sharing on tools and templates")
    