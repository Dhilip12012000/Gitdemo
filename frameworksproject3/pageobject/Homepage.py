from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    appoinment = (By.ID, "btn-make-appointment")
    username = (By.ID, "txt-username")
    password = (By.ID, "txt-password")
    login = (By.ID, "btn-login")
    drop = (By.ID, "combo_facility")
    checkbox = (By.XPATH, "//input[@type='checkbox']")
    label = (By.XPATH, '//label[@class="radio-inline"]')
    date = (By.XPATH, '//input[@type="text"]')
    comment = (By.ID, "txt_comment")
    submit = (By.XPATH, '//button[@type="submit"]')
    grab = (By.XPATH, '//p[@class="lead"]')

    def getappoinment(self):
        return self.driver.find_element(*HomePage.appoinment)

    def getusername(self):
        return self.driver.find_element(*HomePage.username)

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)

    def getlogin(self):
        return self.driver.find_element(*HomePage.login)

    def getdrop(self):
        return self.driver.find_element(*HomePage.drop)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getlabel(self):
        return self.driver.find_elements(*HomePage.label)

    def getdate(self):
        return self.driver.find_element(*HomePage.date)

    def getcomment(self):
        return self.driver.find_element(*HomePage.comment)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getgrab(self):
        return self.driver.find_element(*HomePage.grab)