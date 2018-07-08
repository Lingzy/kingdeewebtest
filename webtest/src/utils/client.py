import requests
from .log import logger
from .config import Config

METHOD = ['GET','POST','DELETE','HEAD','TRACE','PUT','OPTION','CONNECT']

class UnSupportMethodException(Exception):
    pass


class HTTPClient(object):

    def __init__(self, url, method='GET', headers=None, cookies=None):
        self.url = url
        self.session = requests.session()
        self.method = method.upper()
        if self.method not in METHOD:
            raise UnSupportMethodException('Not support method:{0},please check params'.format(self.method))

        self.set_headers(headers)
        self.set_cookies(cookies)

    def set_headers(self,headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self,cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send(self,params=None,data=None,**kwargs):
        response = self.session.request(self.method,url=self.url,params=params,data=data,**kwargs)
        response.encoding = 'utf-8'
        logger.debug('{0} {1}'.format(self.method,self.url))
        logger.debug('Request success:{0}\n{1}'.format(response,response.text))
        return response