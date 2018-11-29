#/usr/bin/env  python3
# -*- coding: utf-8 -*-

import hashlib

# 作用对一字符串进行加密，防止被串改 摘要算法
# 计算结果通常是一个 32位的16进制字符串表示
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 分块进行调用
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

########################################################
#实操

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encod('utf-8'))
    pass
















