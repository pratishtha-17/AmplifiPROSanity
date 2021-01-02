from selenium import webdriver
from Pages_Ampro.all_intelligence_page import AllIntelligencePage
from Utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from Utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AllIntelligenceCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts=StatusCheck(self.driver)
        self.al=AllIntelligencePage(self.driver)
    
    @pytest.mark.run(order=14)
    def test_navigateToInsightsReports(self): 
        self.al.navigateToAllIntelligence()
        self.al.navigateToInsightsReports()      
        result=self.al.verifyNavigationToInsightsReports()
        self.ts.markFinal("test_navigateToInsightsReports",result,"Navigation to Insights Reports was successful")

    @pytest.mark.run(order=15)
    def test_navigateToSustainabilityReports(self): 
        self.al.navigateToAllIntelligence()
        self.al.navigateToSustainabilityReports()     
        result=self.al.verifyNavigationToSustainabilityReports()
        self.ts.markFinal("test_navigateToSustainabilityReports",result,"Navigation to Sustainability Reports was successful") 

    @pytest.mark.run(order=16)
    def test_navigateToInnovationTrends(self): 
        self.al.navigateToAllIntelligence()
        self.al.navigateToInnovationTrends()    
        result=self.al.verifyNavigationToInnovationTrends()
        self.ts.markFinal("test_navigateToInnovationTrends",result,"Navigation to Innovation Trends was successful")  

    @pytest.mark.run(order=17)
    def test_navigateToMegaTrends(self): 
        self.al.navigateToAllIntelligence()
        self.al.navigateToMegaTrends()    
        result=self.al.verifyNavigationToMegaTrends()
        self.ts.markFinal("test_navigateToMegaTrends",result,"Navigation to Mega Trends was successful")      

    @pytest.mark.run(order=18)
    def test_navigateToCategoryBriefings(self): 
        self.al.navigateToAllIntelligence()
        self.al.navigateToCategoryBriefings() 
        result=self.al.verifyNavigationToCategoryBriefings()
        self.ts.markFinal("test_navigateToCategoryBriefings",result,"Navigation to Category Briefings was successful")  

    @pytest.mark.run(order=19)
    def test_navigateToCASMEInsights(self): 
        self.al.navigateToAllIntelligence()
        self.al.navigateToCASMEInsights()
        result=self.al.verifyNavigationToCASMEInsights()
        self.ts.markFinal("test_navigateToCASMEInsights",result,"Navigation to CASME insights was successful")  

    @pytest.mark.run(order=20)
    def test_navigateToCostStructuresNDrivers(self): 
        self.al.navigateToAllIntelligence()
        self.al.navigateToCostStructuresNDrivers()
        result1=self.al.verifyNavigationToCostStructuresNDrivers()        
        self.ts.mark(result1,"Navigation to Cost structures and drivers was successful")
        self.al.chartFormation()
        result2=self.al.verifyChartFormation()
        self.ts.markFinal("chartFormation",result2,"Chart formation was successful")  

    @pytest.mark.run(order=21)
    def test_navigateToCommodities(self): 
        self.al.navigateToAllIntelligence()
        self.al.navigateToCommodities()
        result=self.al.verifyNavigationToCommodities()
        self.ts.markFinal("test_navigateToCommodities",result,"Navigation to Commodities was successful")  


    