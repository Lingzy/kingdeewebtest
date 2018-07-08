from selenium.webdriver.common.by import By
from .bing_main_page import BingMainPage

class BingResultPage(BingMainPage):
    loc_result_links = (By.XPATH, '//li[@class="b_algo"]/h2/a')

    @property
    def result_links(self):
        return self.find_elements(*self.loc_result_links)
