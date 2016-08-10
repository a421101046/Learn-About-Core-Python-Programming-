# !/usr/bin/env python
# -- coding:utf-8 --

def uplowChange(string):
	''' 字符串大小写互转 输入如:"Mr.Ed"返回"mR.eD" '''
	# 不是str
	if type(string) is not str:
		raise ValueError('请输入字符串')
	
	length = len(string)
	arr = []
	for i in range(length):
		tmp = string[i]
		if tmp.isupper():
			tmp = tmp.lower()
		else:
			tmp = tmp.upper()
		arr.append(tmp)
	return ''.join(arr)
	

if __name__ == '__main__':
	print uplowChange('Mr.Ed')
	print uplowChange('sdfSdsfs')
	print  uplowChange('')
	print  uplowChange([])

		
