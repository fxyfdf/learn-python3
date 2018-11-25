#!/use/bin/env python3
# -*- coding: utf-8 -*-

# from collections import namedtuple
#
# Point = namedtuple('Point',['x','y'])
# p = Point(1,3)
# print ('Point:',p.x,p.y)
# print (p)
# print (type(p))

# from collections import deque
# #队列什么时候使用
# q = deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print (q)

# from collections import defaultdict
# #栈
# dd = defaultdict(lambda:'N/A')
# dd['key1'] = 'abc'
# print ('dd[\'key1\']=',dd['key1'])
# print ('dd[\'key2\']=',dd['key2'])

from collections import Counter
c = Counter()
for ch in 'programming':
    print (ch)
    print (c[ch])
    c[ch] = c[ch] +1
print (c)




