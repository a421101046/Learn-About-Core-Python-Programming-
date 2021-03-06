# 其它的内建类型
'''    
    类型
    Null对象 (None)   
    文件
    集合/固定集合
    函数/方法
    模块  类
'''

# 类型
	'''
	对象的一系列固有行为和特性(比如支持哪些运算,具有哪些方法)必须事先定义好
	类型就是保存这些信息的方式
	'''
print type(type(42))  # <type 'type'> type是所有类型的根,类型的默认元类


# NULL对象
	NoneType类型的值是None
	'''
	
	1.布尔值是False的对象:
	
		None
   	 	False (布尔类型)
    	所有的值为零的数:0, 0.0, 0L, 0.0+0.0j, "", [], (), {}
    	
    2.上面没列出的对象的值都是True
    
    3.如果自定义的类  重写了 def __nonzero__() def __len__(),在函数中return 0
    那么它们的布尔值就是 False。
    
    4.标准类型的同类型对象可以比较大小

	'''
	
# 内部类型
	
	代码,帧,跟踪记录,切片,省略对象,XRange对象
	详细见文档
	

	