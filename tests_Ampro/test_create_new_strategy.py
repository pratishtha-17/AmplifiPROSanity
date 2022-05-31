from selenium import webdriver
from pages_Ampro.create_new_strategy_homepage import CreateNewStrategyPage
from utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class NewStrategyCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts=StatusCheck(self.driver)
        self.cns=CreateNewStrategyPage(self.driver)
    
    @pytest.mark.run(order=9)
    def test_create_new_strategyfn(self): 
        self.cns.create_new_strategy_home_page()     
        result=self.cns.verifycreatenewstrategy()
        self.ts.markFinal("test_create_new_strategy",result,"Strategy plot created successfully")


    