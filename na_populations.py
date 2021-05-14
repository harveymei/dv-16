#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/5/14 11:32 上午
# @Author  : Harvey Mei <harvey.mei@msn.com>
# @FileName: na_populations.py
# @IDE     : PyCharm
# @GitHub  : https://github.com/harveymei/

import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()

wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')
