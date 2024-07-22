from selenium.webdriver.common.by import By


class checkoutpage:

    def __init__(self, driver):
        self.driver = driver

    cardtitles = (By.XPATH, '//div[@class="card h-100"]')
    cardfooter = (By.XPATH, '//button[@class="btn btn-info"]')
    cardcheckout = (By.XPATH, '//button[@class="btn btn-success"]')

    def getcardtitles(self):
        return self.driver.find_elements(*checkoutpage.cardtitles)
    #self.driver.find_elements(By.XPATH, '//div[@class="card h-100"]')

    def getcardfooter(self):
        return self.driver.find_elements(*checkoutpage.cardfooter)

    def Checkoutitems(self):
        return self.driver.find_element(*checkoutpage.cardcheckout)
