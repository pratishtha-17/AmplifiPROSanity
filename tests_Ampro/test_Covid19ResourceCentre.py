from selenium import webdriver
from Pages_Ampro.login_page import LoginPage
from Pages_Ampro.covid19_page import Covid19ResourceCentrePage
from Utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from Utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
#@ddt
class Covid19CSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts=StatusCheck(self.driver)
        self.nav=Covid19ResourceCentrePage(self.driver)
    
    @pytest.mark.run(order=3)
    # @data(*getCSVData("D:/Python/Automation2020/AmplifiPROSanity/Test Data_Ampro/testdata_valid_login.csv"))
    # @unpack
    def test_navigateToCovid19ResourceCentre(self):            
        self.nav.navigateToCovid19ResourceCentre()
        result=self.nav.verifyNavigationToCovid19Tab()
        self.ts.markFinal("test_navigation",result,"Navigation to Covid 19 resource centre successful")

    @pytest.mark.run(order=4)       
    def test_navigateToSectorDeepDive(self):
        self.nav.navigateToSectorDeepDive()
        result=self.nav.verifyNavigationToSectorDeepDive()
        self.ts.markFinal("test_navigateToSectorDeepDive",result,"Navigation to Sector deep dive successful")

    @pytest.mark.run(order=5)
    def test_navigateToCategorySnapshot(self):
        self.nav.navigateToCategorySnapshot()
        result=self.nav.verifyNavigationToCategorySnapshot()
        self.ts.markFinal("test_navigateToCategorySnapshot",result,"Navigation to Category Snapshot successful")

    @pytest.mark.run(order=6)
    def test_navigateTo100DayFramework(self):
        self.nav.navigateTo100DayFramework()
        result=self.nav.verifyNavigationTo100DayFramework()
        self.ts.markFinal("test_navigateTo100DayFramework",result,"Navigation to 100 Day Framework successful")

    @pytest.mark.run(order=7)
    def test_navigateToCovid19VideoSeries(self):
        self.nav.navigateToCovid19VideoSeries()
        result=self.nav.verifyNavigationToCovid19VideoSeries()
        self.ts.markFinal("test_navigateToCovid19VideoSeries",result,"Navigation to Covid19 Video Series successful")            





