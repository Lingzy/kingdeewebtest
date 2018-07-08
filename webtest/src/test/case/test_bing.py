import os
import sys
o_path = os.getcwd().split('\\test')[0]
sys.path.append(o_path)
sys.path.append('..')
import time
import unittest
from utils.config import Config,DRIVER_PATH,DATA_PATH,REPORT_PATH
from utils.log import logger
from utils.file_reader import ExcelReader
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from page_obj.bing_main_page import BingMainPage
from page_obj.bing_result_page import BingResultPage


class TestBing(unittest.TestCase):

    URL = Config().get('URL')
    # base_path = os.path.dirname(os.path.dirname(__file__)) + '\..\..'
    # driver_path = os.path.abspath(base_path + '\drivers\chromedriver.exe')
    excel = DATA_PATH + '/testdata.xlsx'

    # locator_input = (By.ID,'sb_form_q')
    # locator_btn = (By.ID,'sb_form_go')
    # locator_result = (By.XPATH,'//li[@class="b_algo"]/h2/a')

    def sub_setUp(self):

        # self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        # self.driver.get(self.URL)
        self.page = BingMainPage(browser_type='chrome')
        self.page.get(self.URL,maximize_window=False)
    def sub_tearDown(self):
        # self.driver.quit()
        self.page.quit()

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
                # self.driver.find_element(*self.locator_input).send_keys(d['search'])
                # self.driver.find_element(*self.locator_btn).click()
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BingResultPage(self.page)
                # links = self.driver.find_elements(*self.locator_result)
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report = REPORT_PATH + '\\' + time.strftime('%Y-%m-%d-%H-%M-%S') + '.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='bing_http_test_report',description='test report')
        runner.run(TestBing('test_bing'))
    # unittest.main(verbosity=2)
    e = Email(
        title='bing test report',
        message='This is the test report ,please check it',
        receiver='guoguoqing@outlook.com',
        server='smtp.126.com',
        sender='yezuidiao@126.com',
        password='guoqing1010',
        path=report)
    e.send()
