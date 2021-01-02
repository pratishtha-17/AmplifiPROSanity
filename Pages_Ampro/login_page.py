from Base_Ampro.selenium_driver import SeleniumDriver
import Utilities_Ampro.custom_logger as cl
import logging,time

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)
    
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        
    #Locators
    _email_field="email"    
    _password_field="password"
    _login_button="//button[contains(text(),'Sign in')]"
    _Ampro_logo="(//nav[@id='tsc_nav_1']/a/img)[1]"
    _incorrect_credentials_msg="spanerrormsg"
    _logout="//span[contains(@class,'glyphicon-log-out')]"

    def enterEmail(self, email):
        self.sendKeys(email,self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password,self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button,locatorType="xpath") 

    def login(self, email="", password=""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(2)
        
    def verifyLoginSuccessful(self):
        result=self.isElementPresent(self._Ampro_logo,locatorType="xpath") 
        return result 

    def verifyLoginFailed(self):
        result=self.isElementPresent(self._incorrect_credentials_msg,locatorType="xpath") 
        return result    

          
        
