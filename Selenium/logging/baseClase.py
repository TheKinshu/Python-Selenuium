import logging, inspect

class BaseClass:

    def getLogger(self):
        # By specifiying the variable you will be giving the name of the test -
        # instead of the root file path

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # Create a file handler object to store the logs
        fileHandler = logging.FileHandler('logfile1.log')

        # Formating the log statement
        # Ex: yyyy-mm-dd currenttime : <error level> :<name of the test case> :<error message> 
        formatter = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s')
        fileHandler.setFormatter(formatter)

        # Applying the file handler to logger
        logger.addHandler(fileHandler) # filehandler object

        # logger.setLevel(logging.CRITICAL)

        return logger

