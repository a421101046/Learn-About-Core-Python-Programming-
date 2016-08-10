# -- coding:utf-8 --

# 字符串切片索引的小技巧

s = 'abcde'
for i in [None] + range(-1, -len(s), -1):
	print s[:i]



'''  abcde  # 加个None就可以打印abcde
     abcd
     abc
     ab
     a
'''



# in not in 与 find()  index() 的区别

s = '1312332'
print '1' in s      # 返回  True /False  判断一个子串在另一个字符串中是否存在

print s.find('1')   # 返回 第一个子串的第一个字符的位置   ,没找到返回 －1   

print s.index('1')



#   拼接字符串 
s= '1234567'

s = '%sC%s' % (s[0:2], s[3:])  # 第一种

s = ''.join(('31231','fdsfs','fdsfds'))  # 第二种

s = '2312' +  'fsdf'   		  # 第三种




