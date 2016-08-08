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