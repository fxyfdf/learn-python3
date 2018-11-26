#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

#获取当前时间
now = datetime.now()
print ("now=",now)
print ("type(now)=",type(now))

#用指定日期时间创建 datetime
dt = datetime(2015,4,19,12,20)
print ("dt=",dt)