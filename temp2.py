# !/usr/bin/env python
# -- coding:utf-8 --

# 计算中文的个数


s = 'ffss中文'
print (len(s) - len(s.decode('utf-8'))) / 2


