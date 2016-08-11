# !/usr/bin/env python
# -- coding:utf-8 --
''' 习题7-3 '''

# (a)
dict1 = {'a':2,'z':8,'f':10}
print sorted(dict1)

# (b)
skey = sorted(dict1) 
print skey
print [dict1[key]  for key in  skey]

