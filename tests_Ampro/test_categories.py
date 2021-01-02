from selenium import webdriver
from Pages_Ampro.categories import CategoriesPage
from Utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from Utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CategoriesCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts=StatusCheck(self.driver)
        self.ct=CategoriesPage(self.driver)
    
    @pytest.mark.run(order=11)
    def test_navigateToCategoryViaHomepg(self): 
        self.ct.navigateToCategoryViaHomepg()          
        result=self.ct.verifyNavigationToCategoryViaHomepg()
        self.ts.markFinal("test_navigateToCategoryViaHomepg",result,"Navigation to Category via Home Page successful")

    @pytest.mark.run(order=12)
    def test_navigateToCategoryViaTopMenu(self): 
        self.ct.navigateToCategoryViaTopMenu()           
        result=self.ct.verifyNavigationToCategoryViaTopMenu()
        self.ts.markFinal("test_navigateToCategoryViaTopMenu",result,"Navigation to Category via Top menu successful")

    