import unittest
import requests
from ddt import ddt, data, unpack


from library.getData import get_xls_data


@ddt
class APITesting(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

   
    @data(*get_xls_data('./data/post_data.xls'))
    @unpack
    def test_post_topic(self,token,title,tab,content,statuscode):
        url = 'http://118.31.19.120:3000/api'
        post_data={
            "accesstoken":token,
            "title":title,
            "tab":tab,
            "content":content
        }
        res = requests.post(url,post_data)
        assert res.status_code == statuscode

    # def test_post_update(self,token,topic_id,title,tab,content,):
    #     url = 'http://118.31.19.120:3000/api/v1/topics/update'
    #     post_data_update = {
    #         "accesstoken": token,
    #         "topic_id":id,
    #         "title": title,
    #         "tab": tab,
    #         "content": content
    #     }
    #     res_update = requests.post(url, post_data_update)
    #     assert res_update.status_code == 200


    def tearDown(self):
       pass

    @classmethod
    def tearDownClass(self):
        pass
