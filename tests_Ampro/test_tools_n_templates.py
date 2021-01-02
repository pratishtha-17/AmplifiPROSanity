from selenium import webdriver
from Pages_Ampro.tools_templates_page import ToolsnTemplatesPage
from Utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from Utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class ToolsCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts=StatusCheck(self.driver)
        self.tnt=ToolsnTemplatesPage(self.driver)
    
    @pytest.mark.run(order=8)
    def test_navigateToToolsnTemplates(self):            
        self.tnt.navigateToToolsnTemplates()
        result=self.tnt.verifyNavigationToToolsnTemplates()
        #import pdb;pdb.set_trace()
        self.ts.markFinal("test_navigateToToolsnTemplates",result,"Navigation to Tools & templates successful")

    @pytest.mark.run(order=9)
    def test_strategy_tool(self):            
        self.tnt.strategyTool()
        result=self.tnt.verifyStrategyCreation()
        #import pdb;pdb.set_trace()
        self.ts.markFinal("test_strategy_tool",result,"Strategy tool was clicked successful")    

    @pytest.mark.run(order=10)  
    @data(*getCSVData("D:/Python/Automation2020/AmplifiPROSanity/Test Data_Ampro/testdata_tools_n_templates.csv"))
    @unpack     
    def test_fileSharing(self,Email,Comment):
        self.tnt.fileSharing(Email,Comment)
        result=self.tnt.verifyFileSharing()
        #import pdb;pdb.set_trace()
        self.ts.markFinal("test_fileSharing",result,"File Sharing successful")

    