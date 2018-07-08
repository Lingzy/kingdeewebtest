import unittest
import sys,os
import time
o_path = os.getcwd().split('\\test')[0]
sys.path.append(o_path)
from utils.config import Config,REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger
from utils.HTMLTestRunner import HTMLTestRunner
from utils.assertion import assertHTTPCode


class TestBingHTTP(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPClient(url=self.URL,method='GET')

    def test_bing_http(self):
        res = self.client.send()
        logger.debug(res.text)
        assertHTTPCode(res,[400])
        self.assertIn('微软Bing', res.text)


if __name__ == '__main__':
    report = REPORT_PATH + '\\' + time.strftime('%Y-%m-%d-%H-%M-%S') + '.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='bingtest_report', description='test report')
        runner.run(TestBingHTTP('test_bing_http'))