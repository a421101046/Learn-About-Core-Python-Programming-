# --coding:utf-8 --

# Example1:将错误的信息输出到文件中
file = open('demo.txt','a')	

''' 若open('demo.text') 
抛出Bad file descriptor,因为下面对文件进行了写操作 '''

print >> file ,'fdsfsdFatal error'
file.close()
print "aaaa", # 加 ,  可以指定不要换行符 可以用  'aaaa'.strip()代替
print "aaa" # 自带一个换行符 如单纯一个print 就是打印换行


# Example2:逗号
str = "dog is so density /n   haahhahah"
file = open('demo.txt')
text = file.read()

for char in  text:
	print char,  # 逗号可以让文本的每输出一行,换行一次
file.close()

