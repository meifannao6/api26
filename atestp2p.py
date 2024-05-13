import unittest,requests
from lib.db import *



class MyTestCase(unittest.TestCase):
    url="http://192.168.55.1:8082/p2p_management/addProduct"
    def test_add_ok(self):
        if check_product("110"):
            del_product('110')
        data = {"proNum":"110","proName":"010","proLimit":"10","annualized":"10"}
        r = requests.post(url=self.url,json=data)
        self.assertNotIn('失败',r)
    def test_add_err(self):
        if not check_product('110'):
            add_product('110','010',10,10)
        data = {"proNum": "110", "proName": "010", "proLimit": "10", "annualized": "10%"}
        r = requests.post(url=self.url,json=data)
        self.assertIn('400',r.text)



if __name__ == '__main__':
    unittest.main()
