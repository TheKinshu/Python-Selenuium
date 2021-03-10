import logging

def test_logging():
    # By specifiying the variable you will be giving the name of the test -
    # instead of the root file path
    logger = logging.getLogger(__name__)

    # Create a file handler object to store the logs
    fileHandler = logging.FileHandler('logfile.log')

    # Formating the log statement
    # Ex: yyyy-mm-dd currenttime : <error level> :<name of the test case> :<error message> 
    formatter = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s')
    fileHandler.setFormatter(formatter)

    # Applying the file handler to logger
    logger.addHandler(fileHandler) # filehandler object


    # logging is helpful in many cases, they do precisely what print do and gives timestamp of the debug - 
    # it also has a feature that allow you to disable all logging. Allowing you to save time without deleting/commenting
    # print function out.


    # Different levels of logging state can help provide various amount of information -
    # to different users. The following order is the level of warning debug: 10 - critical: 50 

    # This sets the level of logging it will run from
    # Setting level to INFO will not allow debug level of warning to occur
    logger.setLevel(logging.INFO)

    # Debug: It typical use for debugging problems
    logger.debug('A debug statement is executed')

    # Info: Informational statements concerning of the program state, allowing users -
    # to track program events and or behaviour tracking
    logger.info('Information statement')

    # Warning: A problem or error that occured that can cause potential harm to the -
    # event and or state of the program 
    logger.warning('Something is in warning mode')

    # Error: Error level statement might cause various amount of damage to the program -
    # and should be looked into
    logger.error('A major error has occured')

    # Critical: Fatal error that has occured and will damage the program if not handled
    logger.critical('A critical error has occured')

