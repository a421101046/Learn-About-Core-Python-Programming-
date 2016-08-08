#!/usr/bin/env python
# --coding:utf-8 --

''' 本文件解决书的习题6-7问题 '''

# 导入string 模块
import string

# 无限循环
while 1:

    # 接受一个只含数字字符串
    num_str = raw_input('Enter a number: ')

    # 捕捉异常代码
    try:
        #  把字符串转成10进制的数字
        num_num = string.atoi(num_str)

        # 退出循环
        break

    #  输入字符串不是数字
    except ValueError:
        print "invalid input... try again"

# 生成一个数字数组
fac_list = range(1, num_num+1)
print "BEFORE:", `fac_list`

# 初始化i
i = 0

# 遍历数组
while i < len(fac_list):

    # 删掉数组中的该数的约数
    if num_num % fac_list[i] == 0:
		del fac_list[i]
		i = i - 1   # 当删除一个数时,i要减1
		continue
		
    # 索引增加
    i = i + 1

# 打印该数字的非约数
print "AFTER:", `fac_list`
