# !/usr/bin/env python
# -- coding:utf-8 --

''' 	6–12 课后作业'''

def findchr(string, char):
	'''string 中查找字符 char,找到就返回该值的索引,否则返回-1 '''
	
	# 不是字符串或char长度不为1
	if type(string) is not str or type(char) is not str or len(char) != 1 :
		raise ValueError('请传入字符串类型,查找字符的长度为1')
		
	for i in range(len(string)):
		if string[i] == char:
			return i
	return -1


def rfindchr(string, char):
	'''string 中查找字符 char 最后一次出现的位置,没找到返回-1 '''
	
	# 不是字符串或char长度不为1
	if type(string) is not str or type(char) is not str or len(char) != 1 :
		raise ValueError('请传入字符串类型,查找字符的长度为1')
		
	for i in range(len(string))[::-1]:
		if string[i] == char:
			return i
	return -1
	
def subchr(string, origchar, newchar):
	'''如果找到匹配的字符就用新的字符替换原先字符 '''
	
	# 不是字符串或char长度不为1
	if type(string) is not str or type(origchar) is not str or  \
	len(origchar) != 1 or len(newchar) != 1 or  type(newchar) is not str:
		raise ValueError('请传入字符串类型,查找字符的长度为1')
	
	tmp = []
	for i in range(len(string)):
		if string[i] == origchar:
			tmp.append(newchar)
		else:
			tmp.append(string[i])
	return ''.join(tmp)

		


if __name__ == '__main__':
# 	print findchr('1321','c')
# 	print findchr('1321','1')	
# 	print findchr('1321','')	
# 	print findchr('1321',[])
# 

# 	print rfindchr('1321','c')
# 	print rfindchr('1321','1')	
# 	print rfindchr('1321','')	
# 	print rfindchr('1321',[])


# 	print subchr('1321','c','1')
# 	print subchr('1321','1','a')
# 	print subchr('1321','1','')
# 	print subchr('1321','','1')

	