# !/usr/bin/env python
# -- encoding:utf-8 --

''' 本文件解决书的习题6-5问题 '''


def compare(str1,str2):
	''' 比较两个字符串,区分大小写 '''
	# 判断是否为字符串
	if type(str1) is not type(str2) or type(str1) is not str: 
		raise TypeError('请输入字符串')
	
	# 判断字符是否相等
	[str1,str2] = [str1.lower(),str2.lower()]
	len1 = len(str1)
	try:
		for i in range(len1):
			if str1[i] != str2[i]:
				return False
	except:
		return False

	return len(str2) == len(str1) # 判断长度是否相等

	

def isPalindrome(str1):
	''' 判断字符串是不是回文 '''
	
	if type(str1) is not str: # 不是字符串类型
		return False
	
	arr = []
	str1 = str1.strip() 
	for char in str1:    # 去除特殊字符 和特殊字符
		if char != '' and char != ',':
			arr.append(char)
		
	def isPalind(str1):
		'''	递归函数	'''
		if len(str1) <= 1: # 递归的基线条件
			return True
		if str1[0] != str1[-1]:  
			return False
		else:
			return isPalindrome(str1[1:-1])  # 递归条件
			
	return isPalind(''.join(arr)) 
	
def mkPalindrome(str1):
	''' 传入一个字符,返回该字符的回文 '''
	if type(str1) is not str or len(str1) != 1:
		raise ValueError('不接受长度为1以外的任何字符串')
	
	return ''.join((str1,str1[::-1]))
	

if __name__ == '__main__':

# 	print compare('','')
# 	print compare('','fsfsdf')
# 	print compare('fsfsdf','')
# 	print compare('fsfsdf','fsfsdf')
# 	print compare('fsfsdf','gfgfdgfdgdfgd')
# 	print compare(312312,'gfgfdgfdgdfgd')
	

# 	print isPalindrome('')
# 	print isPalindrome('a')
# 	print isPalindrome('dfsfdsfd')
# 	print isPalindrome('  123, 321 ')
# 	print isPalindrome([])

# 	print mkPalindrome('')
# 	print mkPalindrome('a')
# 	print mkPalindrome('df')
# 	print isPalindrome([])



	

	
	
	