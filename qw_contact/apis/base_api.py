import requests

from qw_contact.utils.log_utils import logger


class BaseApi:

    BASE_URL = ""

    def send_api(self, req):
        '''
        对 requests进行二次封装
        :return: 接口对应接口
        '''
        if self.BASE_URL:
            req["url"] = self.BASE_URL + req.get("url")
        logger.info(f"发起接口请求收到的请求数据为：{req}")
        r = requests.request(**req)
        logger.info(f"发起接口请求后收到的响应数据为：{r.text}")
        return r
