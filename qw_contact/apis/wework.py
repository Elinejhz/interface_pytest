from qw_contact.apis.base_api import BaseApi


class WeWork(BaseApi):

    def __init__(self):
        self.access_token = None

    def get_token(self, corpid, secret):
        '''
        获取token
        :return: access_token的值
        '''
        # 定义 corpid 和 contact_secret
        # corpid = "ww75abb8519b57cec6"
        # contact_secret = "vvavK-3lew1LhtP2sLdfkieOEe8CJy5hJpdJ2ceKiEI"
        # 定义url
        url = "/gettoken"
        # 定义使用的参数
        params = {
            "corpid": corpid,
            "corpsecret": secret
        }

        # 组装调用send的参数
        req = {
            "method": "GET",
            "url": url,
            "params": params
        }
        # 发起接口请求
        # r = requests.request("GET", url=url, params=params)
        r = self.send_api(req)
        # 提取token
        self.access_token = r.json().get("access_token")
