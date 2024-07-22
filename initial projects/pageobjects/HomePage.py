from selenium.webdriver.common.by import By
#first we r creating a class
#then we r creating a class variable there we are creating pageobject, locator nd location path
#nxt we r creating method in class driver.findelement nd mapping with class name nd class variable
#after this we are returning the values nd nxt we need to make cnnction for that driver with the help of constructor
#so we are def __init__(self, driver)by passing driver as parameter nd then assign that parameter
#nxt we need to make cnnction for that driver to test case driver
#there we are passing this classname(self.driver)nd store it in object
#nxt simply we can call the object.methodname.click to make code more readable
#whenever creating obj of class we need to pass driver as an argument in test case
class HomePage:

    def __init__(self, driver):
        self.driver = driver
    Shop = (By.XPATH, '//a[text()="Shop"]')
    name = (By.NAME, 'name')
    mail = (By.NAME, 'email')
    password = (By.ID, 'exampleInputPassword1')
    checkbox = (By.ID, 'exampleCheck1')
    gender = (By.ID, 'exampleFormControlSelect1')
    submit = (By.XPATH, "//input[@type='submit']")
    alerttxt = (By.CLASS_NAME, 'alert-success')

    def Shopitems(self):
        return self.driver.find_element(*HomePage.Shop)
        #driver.find_element(By.XPATH, '//a[text()="Shop"]').click()

    def getname(self):
        return self.driver.find_element(*HomePage.name)
    # driver.find_element(By.NAME, 'name').send_keys('Amir')

    def getemail(self):
        return self.driver.find_element(*HomePage.mail)
    # driver.find_element(By.NAME, 'email').send_keys('hello@gmail.com')

    def getpassword(self):
        return self.driver.find_element(*HomePage.password)
    # driver.find_element(By.ID, 'exampleInputPassword1').send_keys('123456')

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)
    # self.driver.find_element(By.ID, 'exampleCheck1').click()

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)
    # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

    def getalert(self):
        return self.driver.find_element(*HomePage.alerttxt)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)


