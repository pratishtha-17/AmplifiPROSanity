from pages_Ampro.navigation_page import NavigationPage
from selenium import webdriver
from pages_Ampro.all_intelligence_page import AllIntelligencePage
from utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from utilities_Ampro.read_data import getCSVData
from pages_Ampro.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AllIntelligenceCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts = StatusCheck(self.driver)
        self.al = AllIntelligencePage(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=18)
    def test_navigateToInsightsReports(self): 
        self.nav.navigateToAllIntelligence()
        self.al.navigateToInsightsReports()      
        result = self.al.verifyNavigationToInsightsReports()
        self.ts.markFinal("test_navigateToInsightsReports",result,"Navigation to Insights Reports was successful")  

    @pytest.mark.run(order=19)
    def test_navigateToCategoryDeepDive(self): 
        self.nav.navigateToAllIntelligence()
        self.al.navigateToCategoryDeepDive() 
        result = self.al.verifyNavigationToCategoryDeepDive()
        self.ts.markFinal("test_navigateToCategoryDeepDive",result,"Navigation to Deep Dive was successful")  
    
    @pytest.mark.run(order=20)
    def test_clickOnReportCategoryDeepDive(self):
        self.nav.navigateToAllIntelligence()
        self.al.viewReportCategoryDeepDive()
        result = self.al.verifyReportFromCategoryDeepDive()
        self.ts.markFinal("test_clickOnReportCategoryDeepDive",result,"Click on any random report and redirection to report dashboard")       

    @pytest.mark.run(order=21)
    def test_navigateToQuarterlyCategoryBriefings(self): 
        self.nav.navigateToAllIntelligence()
        self.al.navigateToQuarterlyCategoryBriefings() 
        result = self.al.verifyNavigationToQuarterlyCategoryBriefings()
        self.ts.markFinal("test_navigateToCategoryBriefings",result,"Navigation to Quarterly Category Briefings was successful")  

    @pytest.mark.run(order=22)
    def test_navigateToCASMEInsights(self): 
        self.nav.navigateToAllIntelligence()
        self.al.navigateToCASMEInsights()
        result = self.al.verifyNavigationToCASMEInsights()
        self.ts.markFinal("test_navigateToCASMEInsights",result,"Navigation to CASME insights was successful")        

    @pytest.mark.run(order=23)
    def test_navigateToInnovationTrends(self): 
        self.nav.navigateToAllIntelligence()
        self.al.navigateToInnovationTrends()    
        result = self.al.verifyNavigationToInnovationTrends()
        self.ts.markFinal("test_navigateToInnovationTrends",result,"Navigation to Innovation Trends was successful")    

    @pytest.mark.run(order=24)
    def test_navigateToSustainabilityTrends(self): 
        self.nav.navigateToAllIntelligence()
        self.al.navigateToSustainabilityTrends() 
        result=self.al.verifyNavigationToSustainabilityTrends()
        self.ts.markFinal("test_navigateToSustainabilityReports",result,"Navigation to Sustainability trends was successful") 
    
    @pytest.mark.run(order=25)
    def test_navigateToMegaTrends(self): 
        self.nav.navigateToAllIntelligence()
        self.al.navigateToMegaTrends()    
        result = self.al.verifyNavigationToMegaTrends()
        self.ts.markFinal("test_navigateToMegaTrends",result,"Navigation to Mega Trends was successful")      
    
    @pytest.mark.run(order=26)
    def test_navigateToCostStructuresNDrivers(self): 
        self.nav.navigateToAllIntelligence()
        self.al.navigateToCostStructuresNDrivers()
        result1 = self.al.verifyNavigationToCostStructuresNDrivers()        
        self.ts.mark(result1,"Navigation to Cost structures and drivers was successful")
        self.al.chartFormation()
        result2 = self.al.verifyChartFormation()
        self.ts.markFinal("chartFormation",result2,"Chart formation was successful")  

    @pytest.mark.run(order=27)
    def test_navigateToCommodities(self): 
        self.nav.navigateToAllIntelligence()
        self.al.navigateToCommodities()
        result = self.al.verifyNavigationToCommodities()
        self.ts.markFinal("test_navigateToCommodities",result,"Navigation to Commodities was successful")  

    