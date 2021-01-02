from selenium import webdriver
from Pages_Ampro.login_page import LoginPage
from Utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from Utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp=LoginPage(self.driver)
        self.ts=StatusCheck(self.driver)
            
    @pytest.mark.run(order=2)
    @data(*getCSVData("D:/Python/Automation2020/AmplifiPROSanity/Test Data_Ampro/testdata_valid_login.csv"))
    @unpack
    def test_validLogin(self,email,password):            
        self.lp.login(email,password)
        result=self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin",result,"Login Successful")
           






