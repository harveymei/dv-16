#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/12 9:53 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: highs_lows2.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 提取指定列的数据
    highs = []  # 定义最高温度空列表
    for row in reader:  # 遍历列表，阅读器对象从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行。
        # highs.append(row[1])  # 将列表中的第一列值依次写入highs列表
        # 将字符串转换为数值，以供matplotlib使用
        high = int(row[1])
        highs.append(high)

    # print(highs)  # 打印列表

# 绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# 设置图形格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel("", fontsize=16)  # 暂未包含日期数据，x轴标签为空
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
