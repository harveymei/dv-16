#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/13 10:00 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: world_population.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import json
import pygal_maps_world.maps  #
from country_codes import get_country_code


filename = "population_data.json"
with open(filename) as f:  # 打开文件
    pop_data = json.load(f)  # 读取文件

#
cc_populations = {}  # 定义空字典以存储国家人口键值对

for pop_dic in pop_data:  # 遍历列表中的字典
    if pop_dic['Year'] == '2010':  # 判断字典中的年份是否为2010
        country_name = pop_dic['Country Name']  # 获取字典值复制变量
        population = int(float(pop_dic['Value']))  # 获取字典值复制变量
        # print(country_name + ": " + str(population))  # 打印拼接变量
        code = get_country_code(country_name)  # 调用函数传入参数赋值变量
        if code:  # 判断是否为True
            # print(code + ": " + str(population))  # 打印国家代码和人口数量
            cc_populations[code] = population  # 禁用打印，将国别码和人口数量分别作为键和值填充字典
        # else:  # 否则
            # print('Error - ' + country_name)  # 打印错误信息和传入参数国家名称

# 创建实例
wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)
wm.render_to_file('world_population_05141427.svg')
