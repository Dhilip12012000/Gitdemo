from datetime import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class Baseclass:

    def select(self, locator):
        Select(locator).select_by_index(2)

