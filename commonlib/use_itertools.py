#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

"""
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
"无限" 迭代器
"""

# natuals = itertools.count(1)
# for n in natuals:
#     print (n)
#     if n >= 100:
#         break
#
# cs = itertools.cycle('ABC')
# t = 10
# for c in cs:
#     print (c)
#     t = t - 1
#     if t == 0:
#         break

#######################################################################
"""
takewhile 
"""
natuals = itertools.count(1)
print (natuals)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print (list(ns))







