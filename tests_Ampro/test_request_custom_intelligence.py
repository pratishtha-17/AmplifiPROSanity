from selenium import webdriver
from pages_Ampro.request_custom_intelligence import RequestCustomIntelligencePage
from utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RequestCustomIntelligenceTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts = StatusCheck(self.driver)
        self.rci = RequestCustomIntelligencePage(self.driver)


    @pytest.mark.run(order=53)
    def test_RequestCustomIntelligence(self): 
        self.rci.navigateToRequestCustomIntelligence()
        result = self.rci.verifyNavigationToCustomIntelligence()
        self.ts.markFinal("test_RequestCustomIntelligence", result, "Navigation to Custom Intelligence page")   