from pages_Ampro.navigation_page import NavigationPage
from selenium import webdriver
from pages_Ampro.categories import CategoriesPage
from utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from utilities_Ampro.read_data import getCSVData
from pages_Ampro.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CategoriesCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts=StatusCheck(self.driver)
        self.ct=CategoriesPage(self.driver)
        self.nav= NavigationPage(self.driver)
    
    @pytest.mark.run(order=17)
    def test_navigateToCategoryViaHomepg(self): 
        self.nav.navigateToHomePage()
        self.ct.navigateToCategoryViaHomepg()          
        result=self.ct.verifyNavigationToCategoryViaHomepg()
        self.ts.markFinal("test_navigateToCategoryViaHomepg",result,"Navigation to Category via Home Page successful")
    
    @pytest.mark.run(order=16)
    def test_navigateToEachTabCategoryView(self): 
        self.ct.clickOnEachTabOnCategoryView()
        result = self.ct.verifyClickOnEachTab()
        self.ts.markFinal("test_navigateToEachTabCategoryView", result, "Click on each tab on category vbiew")   
    
    @pytest.mark.run(order=15)
    def test_clickOnCategoryNews(self):
        self.ct.clickCategoryNews()
        result = self.ct.verifyNewsItemClicked()
        self.ts.markFinal("test_clickOnCategoryNews",result, "Clicked on a random Category News item")    

    @pytest.mark.run(order=14)
    def test_navigateToCategoryViaTopMenu(self): 
        self.ct.navigateToCategoryViaTopMenu()           
        result=self.ct.verifyNavigationToCategoryViaTopMenu()
        self.ts.markFinal("test_navigateToCategoryViaTopMenu",result,"Navigation to Category via Top menu successful")

    