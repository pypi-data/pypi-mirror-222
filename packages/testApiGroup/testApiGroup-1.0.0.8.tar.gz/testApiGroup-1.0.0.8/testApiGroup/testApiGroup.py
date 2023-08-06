import json

import requests
import logging


class TestApiGroup:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.url = 'http://localhost:8080'
        logging.basicConfig(
            level=logging.DEBUG,  # 设置日志级别为DEBUG
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def 用来测试的api(self, id):
       params = {'id':id}
       data = {"apiKey": "4fddfd63c67fa51ee7d5ff5e560b43d5", "currPage": 1, "pageSize": 10000}
       data["params"] = params
       self.httpSender(data)

    def fortest(self, id):
       params = {'id':id}
       data = {"apiKey": "5612de279f58b2a82502b35a6340596e", "currPage": 1, "pageSize": 10000}
       data["params"] = params
       self.httpSender(data)

    

    def httpSender(self, data):
        logger = logging.getLogger('HttpTest')
        logger.debug('传入参数为: %s', data)
        res = requests.post(url=self.url, data=json.dumps(data), headers=self.headers)
        logger.debug('接口请求结果为: %s', res.text)
        


