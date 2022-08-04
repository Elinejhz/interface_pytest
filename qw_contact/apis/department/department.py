import os


from qw_contact.apis.wework import WeWork
from qw_contact.utils.utils import Utils


class Department(WeWork):
    '''
    接口实现只描述接口信息，不要做断言等
    '''

    def __init__(self):
        super().__init__()
        path = os.sep.join([Utils.get_frame_root_path(), "config/secrets.yaml"])
        yaml_data = Utils.get_yaml_data(path)
        corpid = yaml_data.get("corpid").get("yinian")
        secret = yaml_data.get("secret").get("contact")
        _env = os.getenv("test_env")
        self.BASE_URL = yaml_data.get(_env).get("BASE_URL")
        self.get_token(corpid, secret)
        _env = os.getenv("test_env")

    def create(self, data):
        '''
        创建部门
        :return:
        '''
        # 定义创建url
        create_url = "/department/create"
        # 定义参数
        params = {
            "access_token": self.access_token
        }

        # 组装调用send的参数
        req = {
            "method": "POST",
            "url": create_url,
            "params": params,
            "json": data
        }
        # 发起请求
        # r = requests.request("POST", url=create_url, params=params, json=data)
        r = self.send_api(req)
        # 返回请求得到的结果
        return r

    def update(self, data):
        '''
        更新部门
        :return:
        '''
        # 定义更新url
        update_url = "/department/update"
        # 定义参数
        params = {
            "access_token": self.access_token
        }

        # 组装调用send的参数
        req = {
            "method": "POST",
            "url": update_url,
            "params": params,
            "json": data
        }
        # 发起请求
        # r = requests.request("POST", url=update_url, params=params, json=data)
        r = self.send_api(req)
        # 返回请求得到的结果
        return r

    def delete(self, _id):
        '''
        删除部门
        :return:
        '''
        # 定义删除url
        delete_url = "/department/delete"
        # 定义请求参数
        params = {
            "access_token": self.access_token,
            "id": _id
        }

        # 组装调用send的参数
        req = {
            "method": "GET",
            "url": delete_url,
            "params": params
        }
        # 发起请求
        # r = requests.request("GET", url=delete_url, params=params)
        r = self.send_api(req)
        # 返回请求得到的结果
        return r

    def get(self, _id=None):
        '''
        获取部门信息
        :return:
        '''
        # 定义获取列表url
        get_list_url = "/department/list"
        # 定义请求参数
        params = {
            "access_token": self.access_token,
            "id": _id
        }

        # 组装调用send的参数
        req = {
            "method": "GET",
            "url": get_list_url,
            "params": params
        }
        # 发起请求
        # r = requests.request("GET", url=get_list_url, params=params)
        r = self.send_api(req)
        # 返回请求得到的结果
        return r
