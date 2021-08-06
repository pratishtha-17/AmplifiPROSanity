import inspect
import logging
import datetime

def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    # now = datetime.datetime.now()
    # file_name = "D:/Python/Automation2020/AmplifiPROSanity/Logs/" + "AmplifiPRO_Automation" + str(now).replace(":","-")

    # fileHandler = logging.FileHandler("{0}.log".format(file_name), mode='a')
    fileHandler = logging.FileHandler("Automation.log" , mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
