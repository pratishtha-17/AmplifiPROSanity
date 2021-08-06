from selenium import webdriver
from pages_Ampro.solutions_page import SolutionsPage
from utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SolutionsCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts=StatusCheck(self.driver)
        self.sp=SolutionsPage(self.driver)
    
    @pytest.mark.run(order=49)
    def test_navigateToSolutions(self): 
        self.sp.navigateToSolutions()
        self.sp.navigateToMysolutions()    
        result=self.sp.verifyNavigationToSolutions()
        self.ts.markFinal("test_navigateToSolutions",result,"Navigation to Solutions was successful")

    @pytest.mark.run(order=50)
    def test_navigateToMyrequest(self): 
        self.sp.navigateToSolutions()
        self.sp.navigateToMyrequest()    
        result=self.sp.verifyNavigationToMyrequest()
        self.ts.markFinal("test_navigateToMyrequest",result,"Navigation to My request was successful") 

    @pytest.mark.run(order=51)
    def test_navigateToMydeliverables(self): 
        self.sp.navigateToSolutions()
        self.sp.navigateToMydeliverables()   
        result=self.sp.verifyNavigationToMydeliverables()
        self.ts.markFinal("test_Mydeliverables",result,"Navigation to My deliverables was successful")
    
    @pytest.mark.run(order=52)
    def test_navigateToMoreofferings(self): 
        self.sp.navigateToSolutions()
        self.sp.navigateToMoreofferings()   
        result=self.sp.verifyNavigationToMoreofferings()
        self.ts.markFinal("test_navigateToMoreofferings",result,"Navigation to More offerings was successful")
      