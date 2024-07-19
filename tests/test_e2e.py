import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.HomePage import HomePage
from pageobjects.checkoutpage import checkoutpage
from pageobjects.confirm import confirmPage
from testt.BaseClass import Baseclass


class Testone(Baseclass):

    def test(self):
        home = HomePage(self.driver)
        home.Shopitems().click()
        checkout = checkoutpage(self.driver)
        log = self.getLogger()
        products = checkout.getcardtitles()
        log.info("getting card titles")
        #self.driver.find_elements(By.XPATH, '//div[@class="card h-100"]')
        for product in products:
            name = product.text
            #name = product.find_element(By.XPATH, 'div/h4/a').text
            if name == "Blackberry":
                checkout.getcardfooter().click()


        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        checkout.Checkoutitems().click()

        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        confirmation = confirmPage(self.driver)
        confirmation.getconfirmation().send_keys("ind")
        log.info("Verify the word ind")

        #self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifylinkpresence("India")

        # self.driver.find_element(By.LINK_TEXT, "India").click()
        Country = confirmPage(self.driver)
        Country.getcountry().click()

        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        Checkbox = confirmPage(self.driver)
        Checkbox.clickcheckbox().click()

        self.driver.find_element(By.CLASS_NAME, "btn-success").click()
        sucessmsge = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("getting the success message" + sucessmsge)
        print(sucessmsge)
        assert "Success! Thank you!" in sucessmsge










































