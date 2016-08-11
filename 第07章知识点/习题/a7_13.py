# !/usr/bin/env python
# -- coding:utf-8 --

''' 习题7-13 '''

from random import randrange

def randArr():
	''' 返回存放随机数的数组
		从 0 到 9(包括 9)中随机选择,生成 1 到 10 个随机数
	'''
	n = 0
	end = 9  		# 索引
	m = randrange(1,10) # 有几个随机数
	arr = []  # 完整的随机数列表

	while(n <= m):  # 生成N 个元素的由随机数 n 组成的列表
		arr.append(randrange(0,end))
		n += 1		
	return arr
	
	
def compare():
	''' 比较两个随机数组  '''
	A = randArr() # 随机数组A
	B = randArr()  # B	
	print set(A) & set(B)
	print set(A) | set(B)
	
	
if __name__ == '__main__':
	compare()
	


