#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/13 2:49 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: countries.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
