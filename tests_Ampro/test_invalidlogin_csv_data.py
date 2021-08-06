from selenium import webdriver
from pages_Ampro.login_page import LoginPage
from utilities_Ampro.teststatus import StatusCheck
import unittest
import pytest
from ddt import ddt,data,unpack
from utilities_Ampro.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class InvalidLoginCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp=LoginPage(self.driver)
        self.ts=StatusCheck(self.driver)      

    @pytest.mark.run(order=1)
    @data(*getCSVData("D:/Python/Automation2020/AmplifiPROSanity/Test Data_Ampro/testdata_invalid_login.csv"))
    @unpack
    def test_invalidLogin(self,email,password):          
        self.lp.login(email,password)
        result=self.lp.verifyLoginFailed()
        self.ts.markFinal("test_invalidLogin",result,"Invalid Login verified successfully")



