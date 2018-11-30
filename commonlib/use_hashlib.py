#/usr/bin/env  python3
# -*- coding: utf-8 -*-

import hashlib

# # 作用对一字符串进行加密，防止被串改 摘要算法
# # 计算结果通常是一个 32位的16进制字符串表示
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
#
# # 分块进行调用，update
# md5 = hashlib.md5()
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
#
# # 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
# # SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
# sha1 = hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())

########################################################
# #实操 1 输入口令进行验证
# # -*- coding: utf-8 -*-
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
# def calc_md5(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode("utf-8"))
#     password_md5 = md5.hexdigest()
#     return password_md5
# pas_md5=calc_md5('123qw')
# def login(user,password):
#     if db[user] == calc_md5(password):
#         return True
#     else:
#         return False
#
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')



###########################################################
# 计算更安全的MD5
#chr(random.randint(48,122))  随机成数字，通过chr()  转换成对应的字符
#a1 = ''.join([chr(random.randint(48,122)) for i in range(20) ])
# -*- coding:utf-8 -*-
import hashlib,random
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48,122)) for i in range(20) ])
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username,password):
    user =  db[username]
    print (get_md5(password))
    return user.password == get_md5(password)










