# -- coding:utf-8 --    ＃这句子 要写在最前面
# !/usr/bin/env python


# 数据的集合
arr = []


def append():
	''' 添加字符串 '''
	string = raw_input('请输入字符串>')
	print "添加成功"
	arr.append(string)

def pop():
	''' 删除第一个字符串  '''
	if(length() == 0):
		print "队列已经为空请重新选择"
		return 
	temp = arr.pop(0)
	print "被删除的元素是 %s "   %temp
	
def look():
	''' 查阅队列 '''
	print  str(arr)
	
def length():
	'''  返回队列长度 '''
	return len(arr)

def quit():
	''' 停止 '''
	print "你已经选择了q,程序已经推出"
	return True	
	


def showMenu():
	# 请求的集合
	request = {"a":append,"d":pop,"v":look,"q":quit}

	isQuit = False
	while(not isQuit):  # 判断有没有停止
		print ''' 
		请输入以下指令对队列进行操作:
		q:退出程序
		a:添加元素
		d:删除元素
		v:查看元素
		'''
		# 获取按键,处理按键错误情况
		try:
			req = raw_input('>')[0]
			val = request[req]
		except KeyError,IndexError:
			print "没有这个操作,请重新选择"
			continue
		except KeyboardInterrupt:
			print "你选择了 q按键"
			isQuit = request['q']
			continue
		
		# 判断请求 选择操作
		if req == 'a' or req == 'v' or req == 'd':
			 val()
		else:
			isQuit = val()

if __name__ == '__main__':
      showMenu()  
      
'''
	注意点:尽量把功能代码写进函数里
		  尽量不要用tab缩进
		  写代码前先写 伪代码
'''

''' 
	1. 如果模块是被导入,__name__的值为模块名字  
	2. 如果模块是被直接执行,__name__的值为'__main__'
	
	3.可以在if __name__ == '__main__':   放一些调试的代码
'''
	
		
	