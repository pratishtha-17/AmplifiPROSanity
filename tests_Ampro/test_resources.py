from selenium import webdriver
from pages_Ampro.resources_page import ResourcesPage
from utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ResourcesCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts=StatusCheck(self.driver)
        self.rp=ResourcesPage(self.driver)
    
    @pytest.mark.run(order=43)
    def test_navigateToBlogs(self): 
        self.rp.navigateToResources()
        self.rp.navigateToBlogs()      
        result=self.rp.verifyNavigationToBlogs()
        self.ts.markFinal("test_navigateToBlogs",result,"Navigation to Blogs was successful")

    @pytest.mark.run(order=44)
    def test_navigateToCaseStudies(self): 
        self.rp.navigateToResources()
        self.rp.navigateToCaseStudies()      
        result=self.rp.verifyNavigationToCaseStudies()
        self.ts.markFinal("test_navigateToCaseStudies",result,"Navigation to Case Studies was successful") 

    @pytest.mark.run(order=45)
    def test_navigateToPodcastsnVideos(self): 
        self.rp.navigateToResources()
        self.rp.navigateToPodcastsnVideos()     
        result=self.rp.verifyNavigationToPodcastsnVideos()
        self.ts.markFinal("test_navigateToPodcastsnVideos",result,"Navigation to Podcasts and Videos was successful")

    @pytest.mark.run(order=46)
    def test_navigateToSpendMattersInsights(self): 
        self.rp.navigateToResources()
        self.rp.navigateToSpendMattersInsights()    
        result=self.rp.verifyNavigationToSpendMattersInsights()
        self.ts.markFinal("test_navigateToSpendMattersInsights",result,"Navigation to Spend matters insights was successful")
    
    @pytest.mark.run(order=47)
    def test_navigateToThoughtLeadership(self): 
        self.rp.navigateToResources()
        self.rp.navigateToThoughtLeadership()    
        result=self.rp.verifyNavigationToThoughtLeadership()
        self.ts.markFinal("test_navigateToThoughtLeadership",result,"Navigation to Thought leadership was successful")

    @pytest.mark.run(order=48)
    def test_navigateToCASMEResourceCentre(self): 
        self.rp.navigateToResources()
        self.rp.navigateToCASMEResourceCentre()    
        result=self.rp.verifyNavigationToCASMEResourceCentre()
        self.ts.markFinal("test_navigateToCASMEResourceCentre",result,"Navigation to CASME Resource Centre was successful")
      