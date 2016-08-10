# !usr/bin/env python
# -- coding: utf-8 --

import string 
import keyword

# 导入模块 并且取了别名
letters = string.ascii_letters + '_'   
digits = string.digits
keylist = keyword.kwlist

print '欢迎来到标识符检查函数'
print '被测试的标识符必须1个字符以及以上'

input = raw_input('>')

if len(input) < 1:
	exit("长度小于1")

# 检查首字母
if input[0] in digits:
	exit("首字母不为数字")

# 检查字符串是否由 字母 数字 _组成
inputs = input[1:]
for char in inputs:	# 用inputs来替代input[1:]:  ,可以让inputs数组只被计算一次
	if char not in letters +  digits :
		exit("标识符包含非法字母")
		break
# 检查字符串是否为关键字
for key in keylist:
	if key.find(input) != -1:
		exit("标识符包含关键字")
		break

	
print "恭喜你,通过检查"
	
	
	
