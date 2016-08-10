# -- coding:utf-8 --

#!/usr/bin/env python   ## 避免python没装在默认的/usr/bin路径下的情况。首先到env设置里找python的安装路径，再调用对应路径下的解释器程序完成操作

'makeTextFile.py -- 创建文件的脚本'  ## 这里是文档字符串	

import os    ## os.linesep取别名。这样做可以缩短变量名,也能改善访问该变量的性能
ls = os.linesep ## 得到当前平台的行终止符

# 获取文件名
while True:
    fname = raw_input('输入文件名: ')
    if os.path.exists(fname):  ## os.path.exists() 确认一个文件名是否存在
        print"*** 错误: '%s' 文件已经存在" % fname
    else:
        break

# 获取文本的每一行  
all = []
print "\n输入行 (以.号结束输入).\n"

# 当输入.时,退出循环
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# 写入每一行,并加上当前平台的行终止符
fobj = open(fname, 'w')

fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print '结束'


## '#'代表源代码自带的注释,'##'代表这句代码不懂 加上的注释
