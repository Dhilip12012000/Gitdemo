import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageobject.Homepage import Homepage
from testt.Baseclass import Baseclass


class Testone(Baseclass):


    def test(self):
        home = Homepage(self.driver)
        home.getusername().send_keys("standard_user") #self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        home.getpassword().send_keys("secret_sauce")     #self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        home.getlogin().click()   #self.driver.find_element(By.ID, "login-button").click()

        self.select(home.getsort()) #drop = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))

        home.getcart().click()  #self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        home.getshopping().click()  #self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()

        home.getcheckout().click()  #self.driver.find_element(By.ID, "checkout").click()

        home.givefirstname().send_keys("D")  #self.driver.find_element(By.ID, "first-name").send_keys("D")

        home.givelastname().send_keys("D") #self.driver.find_element(By.ID,"last-name").send_keys("D")

        home.givepostalcode().send_keys("666666") #self.driver.find_element(By.ID, "postal-code").send_keys("666666")

        home.getsubmit().click() #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        print(home.givesummary().text)  #print(self.driver.find_element(By.XPATH, "//div[@class='summary_info']").text)

        home.givefinish().click()  #self.driver.find_element(By.ID, "finish").click()

        grabtxt = home.gettext().text

        assert "Thank" in grabtxt

        print(grabtxt)
