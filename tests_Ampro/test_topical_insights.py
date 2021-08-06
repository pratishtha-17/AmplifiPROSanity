from selenium import webdriver
from pages_Ampro.login_page import LoginPage
from pages_Ampro.topical_insights_page import TopicalInsightsPage
from utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TopicalInsightsTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts=StatusCheck(self.driver)
        #import pdb;pdb.set_trace()
        self.nav=TopicalInsightsPage(self.driver)
    
    @pytest.mark.run(order=10)
    def test_navigateToTopicalInsights(self):         
        self.nav.navigateToTopicalInsights()
        result=self.nav.verifyNavigationToTopicalInsights()      
        self.ts.markFinal("test_navigation",result,"Navigation to Topical insights successful")

    @pytest.mark.run(order=11)       
    def test_navigateToLatestTopics(self):
        self.nav.navigateToLatestTopics()
        result=self.nav.verifyNavigationToLatestTopics()       
        self.ts.markFinal("test_navigateToLatestTopics",result,"Navigation to Latest Topics successful")

    @pytest.mark.run(order=12)
    def test_navigateToCovid19(self):
        self.nav.navigateToCovid19()
        result=self.nav.verifyNavigationToCovid19()      
        self.ts.markFinal("test_navigateToCategorySnapshot",result,"Navigation to Covid-19 successful")

    @pytest.mark.run(order=13)
    def test_navigateToAllTopics(self):
        self.nav.navigateToAllTopics()
        result=self.nav.verifyNavigationToAllTopics()  
        self.ts.markFinal("test_navigateToAllTopics",result,"Navigation to All topics successful")

              





