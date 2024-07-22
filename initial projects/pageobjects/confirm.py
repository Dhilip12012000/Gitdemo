from selenium.webdriver.common.by import By


class confirmPage:

    def __init__(self, driver):
        self.driver = driver

    confirm = (By.ID, "country")
    country = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")



    def getconfirmation(self):
        return self.driver.find_element(*confirmPage.confirm)
    #self.driver.find_element(By.ID, "country").send_keys("ind")

    def getcountry(self):
        return self.driver.find_element(*confirmPage.country)
    #self.driver.find_element(By.LINK_TEXT, "India").click()

    def clickcheckbox(self):
        return self.driver.find_element(*confirmPage.checkbox)
    #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()


#self.driver.find_element(By.CLASS_NAME, "btn-success").click()