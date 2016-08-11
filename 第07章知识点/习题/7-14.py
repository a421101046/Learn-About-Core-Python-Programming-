# !/usr/bin/env python
# -- coding:utf-8 --

''' 习题7-14 '''  

from a7_13 import randArr  

def Int2Str(nums):
	''' 传入一个int的整型数组 '''
	arr = []
	for i in range(len(nums)):
		arr.append(str(nums[i]))
	return arr

def checkRs():
	''' 任务:比较两个随机数组
		检查用户是否答案是否正确,给予用户三次机会
	'''
	A = randArr()
	B = randArr()
	ATemp = Int2Str(A) # 随机数组A
	BTemp = Int2Str(B)  # B	
	
	isOK = False
	count = 0
	while(not isOK):
		count += 1   # 回答次数增加
		print "请你分别输入A=%s,B=%s 的并集 交集数字之间不加任何间隔符," %(str(A),str(B))
			
		try:
			input1 = set(raw_input('并集>'))
			input2 = set(raw_input('交集>'))
		except:
			print "你选择了结束回答"
			isOK = True
			continue
		# 判断答案是否正确
		if input1 == (set(ATemp) & set(BTemp)) and input2 == (set(ATemp) | set(BTemp)):
			isOK = True
			print "回答正确"
		else:
			print "回答错误请继续\n"
		if count >= 3:
			isOK = True
			print "回答次数已用完,谢谢参与"
		

		
		
if __name__ == '__main__':
	checkRs()
	



