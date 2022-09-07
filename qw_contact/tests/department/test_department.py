import json
import os

import allure
import jsonpath

from qw_contact.apis.department.department import Department
from qw_contact.utils import operate_yaml
from qw_contact.utils.log_utils import logger


@allure.feature("部门管理")
class TestDepartment:

    def setup_class(self):
        # path = os.sep.join([Utils.get_frame_root_path(), "config/secrets.yaml"])
        # yaml_data = Utils.get_yaml_data(path)
        # corpid = yaml_data.get("corpid").get("yinian")
        # secret = yaml_data.get("secret").get("contact")
        # self.depart = Department(corpid, secret)
        self.depart = Department()
        self.depart_id = 100
        contact_datas = operate_yaml.get_yaml_data("../../config/contactdata.yaml")
        self.create_data = contact_datas.get("create_data")
        self.update_data = contact_datas.get("update_data")

    @allure.story("流程测试")
    def test_depart_flow(self):
        # 部门新增
        with allure.step("创建部门"):
            create_data = self.depart.create(self.create_data)

            # 获取部门列表，判断是否新增成功
            _list = self.depart.get_simple(self.depart_id)

            # assert create_data.json().get("id") in [de.get("id") for de in _list.json().get("department")]
            assert create_data.json().get("id") in jsonpath.jsonpath(_list.json(), "$..id")
            # assert json.loads(create_data.json()).get("id") in jsonpath.jsonpath(_list.json(), "$..id")

        # 更新部门的信息
        # with allure.step("更新部门"):
        #     self.depart.update(self.update_data)
        #     # 获取部门列表，判断是否新增成功
        #     _list = self.depart.get_get(self.depart_id)
        #
        #     # assert self.update_data.get("name") in [de.get("name") for de in _list.json().get("department")]
        #     assert self.update_data.get("name") in jsonpath.jsonpath(_list.json(), "$..name")
        # 删除部门
        with allure.step("删除部门"):
            self.depart.delete(self.depart_id)
            _list = self.depart.get_simple()
            # assert self.depart_id not in [de.get("id") for de in _list.json().get("department")]
            assert self.depart_id not in jsonpath.jsonpath(_list.json(), "$..id")
