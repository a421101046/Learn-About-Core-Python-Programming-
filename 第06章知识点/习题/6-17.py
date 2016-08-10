# !/usr/bin/env python
# -- coding:utf-8 --

def myPop(aList):
	''' 用一个list作为输入,移除列表的最新一个元素,并返回list '''
	assert type(aList) is list  ,'请输入一个list'
	assert len(aList) != 0  ,'列表已经为空'
	del aList[len(aList) -1]
	
	return aList
	
	
	
if __name__ == '__main__':
	print myPop([1,2])
	print myPop([])

	print myPop('fdsfsd')
		
		
# 熟悉 assert用法