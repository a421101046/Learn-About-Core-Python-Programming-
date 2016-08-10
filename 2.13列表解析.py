# -- coding: utf-8 --
# 对列表的解析


squared = [x ** 2 for x in range(4)]
'''
	print squared
	结果:  [0,1,4,9]
'''

sqdEvens = [x ** 2 for x in range(8) if not x % 2]
'''
	print squared
	结果:  [0, 4, 16, 36]
'''
print sqdEvens
