# !/usr/bin/env python
# -- coding:utf-8 --


''' 习题7-10 '''

def encrypt(string):
	''' rot13加密字符串 '''
	length = len(string)
	arr = []
	
	# 映射的过程
	for i in range(length):
		char = string[i]
		tmp = ord(char.lower())
		if tmp < ord('a') or tmp > ord('z'):
			arr.append(char)
		elif tmp - ord('a') > 12: # 后半部分
			arr.append( chr(ord(char) - 13)) 
		else:  # 前半部分 
			arr.append(chr(ord(char) + 13)) 
	return ''.join(arr)

def showEncrypt():
	''' 让用户选择加密的方式 '''
	
	print '''
		加密:e
		解密:d
		不需要该操作请按q
	'''
	try:
		input = raw_input('>')
	except:
		input = 'q'	
		
	# 判断用户的操作
	if input == 'e':
		input = raw_input('>')
		print "加密后的字符串是%s" %encrypt(input)
	elif input == 'd':
		input = raw_input('>')
		print "解密后的字符串是%s" %encrypt(input)
	else:
		print "你选择了q"
		
if __name__ == '__main__':
# 	print encrypt('aZHp123 ,#Ff')

	showEncrypt()
	
	
	
	
		
			
			
	