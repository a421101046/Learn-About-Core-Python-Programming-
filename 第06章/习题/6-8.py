# !/usr/bin/env python
# -- coding:utf-8 --


def tran2words(num):
	''' 将数字转化成英文文本,返回应为字符串

		如 29 =>  twenty - nine
		1<= num <= 1000
	'''

	# 传入的不是数字,抛出异常
	if type(num) is not int or num > 1000 or num < 0:
		raise ValueError('传入类型或值超出0到1000')
	# 数字为0
	if num == 0:
		return 'Zero'


	# 十位以下的数
	words1 = ['one','two','three','four','five','six','seven','eight','nine']
	
	# 10,20,30,....90
	words2 = ['ten','twenty','thirty','forty','fifty','sixty' ,'seventy','eighty','ninety' ]
	
	# 11 到 19
	words3 = ['eleven','twelve','thirteen','fourteen', 'fifteen','sixteen','seventeen','eighteen','nineteen']
	
	# 10 100 1000
	words4 = ['hundred','thousand']
	
	num = int(num)
	length = len(str(num))	# 数字长度
	arr = []			# 结果集


	# 开始循环数字每一位
	while(True):
		tmp = 10 ** (length - 1)	# 需要整除的数字 如120 tmp为 100, 15 tmp 为 10
		remain = num % tmp   	# 余数
		loc = num / tmp			# 商
		
		# 两位数
		if length == 2:
			if remain == 0: # 数为 10,20 ...90
				arr.append(words2[loc - 1])
				break
			elif loc == 1: # 数为11 到 19
				arr.append(words3[remain - 1])
				break
			else:  # 其它的数字
				arr.append(words2[loc - 1])
				num -= loc * tmp 
		# 一位数	
		elif length == 1: # 只有一位的时候
			arr.append(words1[loc - 1])
			break
		# 两位以上
		else:
			arr.append(words1[loc - 1])
			arr.append(words4[length - 3])
			
			if remain == 0 :		# 可以整除
				break
			else:					# 不能整除
				num -= loc * tmp 	

		length -= 1
	return '-'.join(arr) 	# 返回数组
	
			

if __name__ == '__main__':

	# 以下是测试用例
	print tran2words(0)
	print tran2words(5)
	print tran2words(10)
	print tran2words(19)
	print tran2words(20)
	print tran2words(55)
	print tran2words(99)
	print tran2words(100)
	print tran2words(514)
	print tran2words(1000)
	print tran2words(1001)
	print tran2words('fdsfd')
	print tran2words(0001)

						
			
		
		
		
		