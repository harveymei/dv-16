#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/13 3:45 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: country_codes.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

from pygal_maps_world.i18n import COUNTRIES


# 定义函数
def get_country_code(country_name):
    for code, name in COUNTRIES.items():  # 遍历国家代码与国家名称
        if name == country_name:  # 判断传入参数是否与国家名称一致
            return code  # 一致则返回国家代码
    return None  # 否则返回None


# 传入参数测试
# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))
