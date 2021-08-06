from selenium import webdriver
from pages_Ampro.home_page import HomePage
from utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class HomePageTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = StatusCheck(self.driver)          
    
    @pytest.mark.run(order=3)
    def test_redirectionToTermsnConditions(self):
        self.hp.navigationToTermsnConditions()
        result = self.hp.verifyNavigationToTermsnConditions()
        self.ts.markFinal("test_redirectionToTermsnConditions",result,"Navigation to Terms and Conditions page")
    
    @pytest.mark.run(order=4)
    def test_redirectionToFAQ(self):
        self.hp.navigationToFAQ()
        result = self.hp.verifyNavigationToFAQ()
        self.ts.markFinal("test_redirectionToFAQ", result, "Navigation to FAQ page")

    @pytest.mark.run(order=5)
    def test_navigationToProfile(self):
        self.hp.navigateToProfile()
        result = self.hp.verifyNavigationToProfile()
        self.ts.markFinal("test_navigationToProfile", result, "Navigation to Profile")  

    @pytest.mark.run(order=6)
    def test_TierNavigation(self):
        self.hp.clickTierName()
        result = self.hp.verifyTierPopUp()
        self.ts.markFinal("test_TierNavigation", result, "Tier name clicked")         

    @pytest.mark.run(order=7)
    def test_signOut(self):
        self.hp.signOut()
        result = self.hp.verifySignOut()
        self.ts.markFinal("test_sign_out", result, "Sign out from the application")    

           






