#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/13 10:00 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: world_population.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import json

filename = "population_data.json"
with open(filename) as f:  # 打开文件
    pop_data = json.load(f)  # 读取文件

#
for pop_dic in pop_data:  # 遍历列表中的字典
    if pop_dic['Year'] == '2010':  # 判断字典中的年份是否为2010
        country_name = pop_dic['Country Name']  # 获取字典值复制变量
        population = int(float(pop_dic['Value']))  # 获取字典值复制变量
        print(country_name + ": " + str(population))  # 打印拼接变量

