# -- coding:utf-8 -- 

# !/usr/bin/env python

'typechk.py  --用来判断对象的类型 '

from types import IntType  

def typechk(num):
	'''	传入一个对象,判断类型是否存在	'''
	if type(num) is IntType:
		print "存在整型"
	elif type(num) is str:
		print "存在字符型"
	else:
		print "不存在"
		
		
arr = [1,2,2.4,2L,'fdsfdss']
for item in arr:
	typechk(item)
		
		