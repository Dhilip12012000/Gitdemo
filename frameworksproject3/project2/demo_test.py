from pageobject.Homepage import HomePage
from testt.Baseclass import Baseclass


class TestLogin(Baseclass):


    def test_login(self):

        homepage = HomePage(self.driver)

        homepage.getappoinment().click()

        homepage.getusername().send_keys("John Doe")

        homepage.getpassword().send_keys("ThisIsNotAPassword")

        homepage.getlogin().click()

        homepage.getdrop()

        homepage.getcheckbox().click()

        radio = homepage.getlabel()
        for i in radio:
            if i.text == "Medicaid":
                i.click()
                break

        homepage.getdate().send_keys("17/07/2024")

        homepage.getcomment().send_keys("Need Appointment")

        homepage.getsubmit().click()

        print(homepage.getgrab().text)
