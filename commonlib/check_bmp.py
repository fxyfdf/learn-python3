#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct

bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

print(struct.unpack('<ccIIIIIIHH', bmp_header))

"""
好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
struct的pack函数把任意数据类型变成bytes：
"""

"""
struct

import struct
def isBMP(img):
    f = open(img,'rb')
    b = f.read(30)
    s=struct.unpack('<ccIIIIIIHH',b)
    if s[0] == 'B' and s[1] == 'M':
        print 'BMP size is %s * %s' %(s[6],s[7])
        print 'BMP color is %s' % s[9]
    else:
        print 'This is not a bmp image'

    f.close()
isBMP('f:/test.bmp')
isBMP('f:/test1.jpg')

"""