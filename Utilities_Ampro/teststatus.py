import utilities_Ampro.custom_logger as cl
import logging
from base_Ampro.selenium_driver import SeleniumDriver
from traceback import print_stack
import sys,traceback

class StatusCheck(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(StatusCheck, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                #import pdb;pdb.set_trace()
                if result == True:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screenShot(resultMessage)
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, tcName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)
        
        if "FAIL" in self.resultList:            
            self.log.error(tcName +  " ### TEST FAILED")
            self.resultList.clear()             
        else:
            self.log.info(tcName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
             