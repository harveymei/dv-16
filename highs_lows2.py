#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/12 9:53 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: highs_lows2.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import csv
from matplotlib import pyplot as plt
# 处理日期数据
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 提取指定列的数据
    # highs = []  # 定义最高温度空列表
    # 定义日志列表和最高温度列表
    dates, highs = [], []
    for row in reader:  # 遍历列表，阅读器对象从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行。
        # 遍历日期写入列表
        # https://docs.python.org/3/library/datetime.html#datetime.date.strftime
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        # highs.append(row[1])  # 将列表中的第一列值依次写入highs列表
        # 将字符串转换为数值，以供matplotlib使用
        high = int(row[1])
        highs.append(high)

    # print(highs)  # 打印列表

# 绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(highs, c='red')  # 红色显示最高气温
# 添加日期数据
plt.plot(dates, highs, c='red')

# 设置图形格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel("", fontsize=16)  # 暂未包含日期数据，x轴标签为空
# 绘制斜的日期标签，以免它们彼此重叠
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
