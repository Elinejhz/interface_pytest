import logging
import yaml


# 读取yaml文件
def get_yaml_data(filename):
    logging.info("获取数据")
    with open(filename) as f:
        datas = yaml.safe_load(f)
        return datas
