import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.HomePage import HomePage
from testt.BaseClass import Baseclass


class Testtwo(Baseclass):

    def test_submission(self, getData):
        homepage = HomePage(self.driver)
        homepage.getname().send_keys(getData[0])  #driver.find_element(By.NAME, 'name').send_keys('Amir')

        homepage.getemail().send_keys('hello@gmail.com')  #driver.find_element(By.NAME, 'email').send_keys('hello@gmail.com')

        homepage.getpassword().send_keys('123456')  #driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')

        self.selectoption(homepage.getgender(), getData[2])  #Select(self.driver.find_element(By.ID, 'exampleFormControlSelect1')).select_by_visible_text("Male")

        homepage.getcheckbox().click()  #self.driver.find_element(By.ID, 'exampleCheck1').click()

        homepage.getsubmit().click()  #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        mssge = homepage.getalert().text  #mssge = self.driver.find_element(By.CLASS_NAME, 'alert-success').text

        print(mssge)
        self.driver.refresh()

    @pytest.fixture(params=[("Rahul", "Shetty", "Male"), ("Amir", "Khan", "Male")])
    def getData(self, request):
        return request.param



