#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/12 9:53 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: highs_lows2.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import csv

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 提取指定列的数据
    highs = []  # 定义最高温度空列表
    for row in reader:  # 遍历列表，阅读器对象从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行。
        highs.append(row[1])  # 将列表中的第一列值依次写入highs列表

    print(highs)  # 打印列表
