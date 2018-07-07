import os
import sys
o_path = os.getcwd().split('\\test')[0]
sys.path.append(o_path)
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config,DRIVER_PATH,DATA_PATH,REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner


class TestBing(unittest.TestCase):

    URL = Config().get('URL')
    # base_path = os.path.dirname(os.path.dirname(__file__)) + '\..\..'
    # driver_path = os.path.abspath(base_path + '\drivers\chromedriver.exe')
    excel = DATA_PATH + '/testdata.xlsx'

    locator_input = (By.ID,'sb_form_q')
    locator_btn = (By.ID,'sb_form_go')
    locator_result = (By.XPATH,'//li[@class="b_algo"]/h2/a')

    def sub_setUp(self):

        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    # def test_search_0(self):
    #     self.driver.find_element(*self.locator_input).send_keys("selenium 灰蓝")
    #     self.driver.find_element(*self.locator_btn).click()
    #     time.sleep(2)
    #     links = self.driver.find_elements(*self.locator_result)
    #     for link in links:
    #         logger.info(link.text)

    # def test_search_1(self):
    #     self.driver.find_element(*self.locator_input).send_keys("selenium python")
    #     self.driver.find_element(*self.locator_btn).click()
    #     time.sleep(2)
    #     links = self.driver.find_elements(*self.locator_result)
    #     for link in links:
    #         logger.info(link.text)

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_input).send_keys(d['search'])
                self.driver.find_element(*self.locator_btn).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report = REPORT_PATH + time.strftime('%Y-%m-%d-%H-%M-%S') + '.html'
    logger.info(report)
    print(report)
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='bingtest_report',description='test report')
        runner.run(TestBing('test_search'))
    # unittest.main(verbosity=2)