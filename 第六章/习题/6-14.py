# !/usr/bin/env python
# -- coding:utf-8 --

''' 	6–14 课后作业'''

def Rochambeau():
	'''  剪刀石头布'''
	
	# 所有胜负情况
	r = [(1,3),(2,1),(3,2),(1,2),(2,3),(3,1),(1,1),(2,2),(3,3)]
	isFinish = False
	
	# 主程序循环
	while(not isFinish):
		print '''请输入你的选择
			1:剪刀
			2:石头
			3:布
		'''
		try:
			input1,input2 = int(raw_input('>')),int(raw_input('>'))	
		except ValueError:
			print "请输入数字"
			continue
			
		if input1 > 3 or input1 < 1 or input2 > 3 or input2 < 1:
			print "输入错误"
			continue
			
		# 查找胜负
		i = r.index((input1,input2))
		if i <= 2:	print "第一个输入者赢"	
		elif i > 5: print "平局"	
		else :		print "第二个输入者赢"			

if __name__ == '__main__':
	Rochambeau()