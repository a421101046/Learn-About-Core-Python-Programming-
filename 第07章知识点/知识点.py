# !/usr/bin/env  python
# -- coding:utf-8 ---

# sorted(dict1) 相当于 sorted(dict1.keys())


# 有一些可变的变量是可以hash 如实现了__hash__() 特殊方法的类

# set集合
	# frozenset是不可变的set,当做字典的key
	# set是可变的,			可以添加和删除元素
	# 可变集合(set)不是可哈希的,因此既不能用做字典的键也不能做其他集合中的元素
	
s = set('chen')  		# set(['c', 'e', 'h', 'n'])  返回去重排序的内容
s = frozenset('bookshop') # frozenset(['b', 'h', 'k', 'o', 'p', 's'])

add('z')  # 添加  使用的是原对象
update('pypi')  # 更新  使用的是原对象
remove('z')		# 删除  使用的是原对象
s -= set('pypi') 



# time模块
	time()获取时间  int类型
	asctime(localtime(time()))  # 打印英文格式化后的时间


# 利用sys模块 打印异常
    返回 (type, value, traceback). type为异常类型, value为异常的参数(通常为异常错误的信息), traceback为跟踪回溯的对象.
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print "*** print sys.exc_info:"
    print 'exc_type is: %s, exc_value is: %s, exc_traceback is: %s' % (exc_type, exc_value, exc_traceback)


	
	
# ''[:]  返回的还是错误
# 在写异常之前  先要分析有什么异常
	
# 模块名的命名规则和 变量命名一致

# .join() 只拼接字符串 
# set(字符串)  =>  set('a','b'.....)