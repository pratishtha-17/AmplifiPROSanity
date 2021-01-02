from selenium import webdriver
from Pages_Ampro.add_to_favourite import AddToFavouritePage
from Utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from Utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AddToFavouriteTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts=StatusCheck(self.driver)
        self.atf=AddToFavouritePage(self.driver)
    
    @pytest.mark.run(order=1)
    def test_add_to_favfn(self): 
        self.atf.add_to_favouritefn()     
        result = self.atf.verifyAddToFavourite()
        self.ts.markFinal("test_add_to_favfn",result,"Category added to My favourites successfully")


    