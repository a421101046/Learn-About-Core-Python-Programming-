# !/usr/bin/env python
# -- coding:utf-8 --

'''  本文件为习题 6-11		'''

def num2ip(num):  # 相当于求 256进制
	'''整数转成ip,返回str类型,格式如WWW.XXX.YYY.ZZZ   
		num为整数
	'''
	# 是否为整数
	try:
		num = int(num)
	except:
		raise Exception("请输入整数")
		
	# 是否小于 2 ** 32 次
	if (num >> 32) > 0:
		raise Exception("请输入 <= 2^32的整数")

	# 整数转ip
	arr = []
	for i in range(4):
		num = num / 256
		arr.append(str(num % 256))
	return '.'.join(arr[::-1])
	
def ip2num(ip):
	'''ip转成整数	,return int 类型
		ip为字符串
	'''
	try:
		nums = ip.split('.')
	except:
		raise ValueError("请传入ip地址")
	else:
		assert len(nums) == 4

		sum = 0
		for i in range(4)[::-1]:
			sum += int(nums[i]) * (256 ** (3 - i))
		return sum
	
if __name__ == '__main__':

# 	print num2ip(-1)
# 	print num2ip(0)
# 	print num2ip(100)
# 	print num2ip(400000)
# 	print num2ip(7777777777777777777)
# 	print num2ip("fdssfd")

	
# 	print ip2num('0.6.26.128')
# 	print ip2num('0.6.26.128.321321')

# 注意  << 运算优先级  低于 -

		
		
	