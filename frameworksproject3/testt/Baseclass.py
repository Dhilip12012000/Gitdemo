import pytest

from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class Baseclass:

    def verifylink(self, locator):
        Select(locator).select_by_index(1)
