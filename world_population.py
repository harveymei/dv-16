#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/13 10:00 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: world_population.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import json
import pygal_maps_world.maps  # 引入地图模块
from pygal.style import RotateStyle  # 引入模块以设置地图样式
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

# 根据人口数量分为三个组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}  # 定义三个分组字典
for cc, pop in cc_populations.items():
    if pop < 10000000:  # 小于1000万
        cc_pops_1[cc] = pop  # 写入字典1
    elif pop < 1000000000:  # 小于10亿
        cc_pops_2[cc] = pop  # 写入字典2
    else:  # 大于10亿
        cc_pops_3[cc] = pop  # 写入字典3

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))  # 打印每一组的国家数量

#
wm_style = RotateStyle('#336699')
# 创建实例
# wm = pygal_maps_world.maps.World()
#
wm = pygal_maps_world.maps.World(wm_style)
wm.title = 'World Population in 2010, by Country'
# wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>10bn', cc_pops_3)
wm.render_to_file('world_population_05141525.svg')

# Traceback (most recent call last):
#   File "/Users/harveymei/PycharmProjects/dv-16/world_population.py", line 51, in <module>
#     wm = pygal_maps_world.maps.World(wm_style)
#   File "/Users/harveymei/PycharmProjects/dv-16/venv/lib/python3.9/site-packages/pygal/graph/base.py",
#   line 50, in __init__
#     config = config.copy()
# AttributeError: 'RotateStyle' object has no attribute 'copy'
