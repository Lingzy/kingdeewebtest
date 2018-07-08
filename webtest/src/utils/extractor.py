import json
import jmespath
from .client import HTTPClient


class JMESPathExtrator(object):

    def extract(self,query=None, body=None):
        try:
            return jmespath.search(query,json.loads(body))
        except Exception as e:
            raise ValueError("Invalid query" + query + ":" + str(e))


if __name__ == '__main__':

    res = HTTPClient(url='http://wthrcdn.etouch.cn/weather_mini?citykey=101010100').send()
    print(res.text)
    j = JMESPathExtrator()
    j_1 = j.extract(query='data.forecast[1].date',body=res.text)
    j_2 = j.extract(query='data.ganmao',body=res.text)
    print(j_1,j_2)