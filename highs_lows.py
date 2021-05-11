#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/11 11:49 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: highs_lows.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

"""
数据可视化之CSV文件操作
"""

import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:  # 打开文件
    reader = csv.reader(f)  # 读取文件
    header_row = next(reader)  # 调用方法读取下一行
    # print(header_row)  # 打印读取到的内容
    # 打印文件头及其位置
    for index, column_header in enumerate(header_row):  # 遍历并获取每个元素的索引及其值
        print(index, column_header)  # 打印索引及对应值
