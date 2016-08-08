# ! /usr/bin/env python
# -- coding:utf-8 --

''' 本文件解决书的习题6-3问题 '''


def sortNums(string):
	'''	用于给一串数字排序	
		string 传入字符串
	'''
	try:
		int(string)
	except ValueError,error:
		raise ValueError('请传入数字')
	else:
		arr = list(string)
		arr.sort(None,None,True)  
		return ''.join(arr) 



if __name__ == '__main__':
	print sortNums('43232534636464')
	
'''
	代码不足:
		1.把arr.sort()当成有返回值的
		2.如何分割字符串 (无间隔符)
		3. sort(cmp=None, key=None, reverse=False)
'''