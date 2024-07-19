import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Baseclass:

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)  # pulling the logs nd __name__ is to identify the testfile where error occured

        filehandler = logging.FileHandler('logfile.log')  # filehandler which is used to store the logs with the given name
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :  %(message)s")
        filehandler.setFormatter(formatter)  # make cnnctn bw filehandler nd formatter
        logger.addHandler(filehandler)  # used for creating the log file with filehandler

        logger.setLevel(logging.INFO)
        return logger

    def verifylinkpresence(self, text):
        (WebDriverWait(self.driver, 10).
         until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text))))

    #verify using custom utilities n number of times
    def selectoption(self, locator, text):
        Select(locator).select_by_visible_text(text)
