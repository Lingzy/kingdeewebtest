import sys
sys.path.append('..')
from selenium.webdriver.common.by import By
from common.page import Page


class BingMainPage(Page):
    loc_search_input = (By.ID, 'sb_form_q')
    loc_search_button = (By.ID,'sb_form_go')

    def search(self,search_text):
        self.find_element(*self.loc_search_input).send_keys(search_text)
        self.find_element(*self.loc_search_button).click()

        
