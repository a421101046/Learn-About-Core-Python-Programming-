# -- coding:utf-8 --

#!/usr/bin/env python   ## 避免python没装在默认的/usr/bin路径下的情况。首先到env设置里找python的安装路径，再调用对应路径下的解释器程序完成操作

'readTextFile.py -- 读取和显示文本文件'

## 获取文件名
fname = raw_input('输入文件名: ')
print

## 尝试着打开或阅读文件
try:
    fobj = open(fname, 'r')
except IOError, e:
    print"*** 文件打开失败:", e
else:
    # 打印内容到界面上
    for eachLine in fobj:
        print eachLine,
    fobj.close()
