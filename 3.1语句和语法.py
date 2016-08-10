# -- coding:utf-8 -- 

# 反斜线 ( \ ) 继续上一行
first = 1
second = 0
if (first == 1) and \
	(second == 0):
	print "符合要求"
        
# 同一行书写多个语句(;) 要用逗号分隔开
import sys; x = 'foo';print "陈文华"

# python中赋值语句的没有返回值
x = 1
#y = (x = x + 1)	# 结果:  SyntaxError: invalid syntax

# 链式赋值没问题
y = x = x + 1 

# 多元赋值
(x,y,z) = 1,2,'1321312'
print z

(x,y) = (y,x) # 可以对x,y进行交换 很实用
