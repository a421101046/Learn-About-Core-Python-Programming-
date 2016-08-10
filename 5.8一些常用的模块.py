# 数字科学计算应用的常用的包
    # http://numeric.scipy.org/
    # http://scipy.org/
    
# 数字类型相关的模块
	decimal
	array math/cmath标准C库数学运算函数。常规数学运算在match模块,复数运算在cmath模块
	operator 数字运算符的函数实现。比如 tor.sub(m,n)等价于m-n
	random 多种伪随机数生成器
	
# random模块

	randrange()和 range()函数参数一样 # 返回一组随机数
	
	uniform(n,m) # 返回n到m的随机数
	
	random() # 相当于uniform(0,1)