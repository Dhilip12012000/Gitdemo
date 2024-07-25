import pytest

from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login = (By.ID, "login-button")
    sort = (By.CLASS_NAME, "product_sort_container")
    cart = (By.ID, "add-to-cart-sauce-labs-onesie")
    shopping = (By.XPATH, "//span[@class='shopping_cart_badge']")
    checkout = (By.ID, "checkout")
    firstname = (By.ID, "first-name")
    lastname = (By.ID,"last-name")
    postalcode = (By.ID, "postal-code")
    submit = (By.XPATH, "//input[@type='submit']")
    summary = (By.XPATH, "//div[@class='summary_info']")
    finish = (By.ID, "finish")
    finaltext = (By.XPATH, "//h2[@class='complete-header']")

    def getusername(self):
        return self.driver.find_element(*Homepage.username)

    def getpassword(self):
        return self.driver.find_element(*Homepage.password)

    def getlogin(self):
        return self.driver.find_element(*Homepage.login)

    def getsort(self):
        return self.driver.find_element(*Homepage.sort)

    def getcart(self):
        return self.driver.find_element(*Homepage.cart)

    def getshopping(self):
        return self.driver.find_element(*Homepage.shopping)

    def getcheckout(self):
        return self.driver.find_element(*Homepage.checkout)

    def givefirstname(self):
        return self.driver.find_element(*Homepage.firstname)

    def givelastname(self):
        return self.driver.find_element(*Homepage.lastname)

    def givepostalcode(self):
        return self.driver.find_element(*Homepage.postalcode)

    def getsubmit(self):
        return self.driver.find_element(*Homepage.submit)

    def givesummary(self):
        return self.driver.find_element(*Homepage.summary)

    def givefinish(self):
        return self.driver.find_element(*Homepage.finish)

    def gettext(self):
        return self.driver.find_element(*Homepage.finaltext)