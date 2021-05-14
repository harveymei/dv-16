#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/13 4:43 下午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: americas.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import pygal_maps_world.maps


# http://www.pygal.org/en/stable/documentation/types/maps/pygal_maps_world.html
# wm = pygal.Worldmap()  # 无效
wm = pygal_maps_world.maps.World()

wm.title = "North, Central, and South America"
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas_05141038.svg')
