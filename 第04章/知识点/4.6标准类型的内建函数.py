# -- coding:utf-8 --

# str() 与repr()的区别

import datetime

birthday = datetime.date(1994,12,23) 

print str(birthday)   # 1994-12-23   

print repr(birthday)  # datetime.date(1994, 12, 23)  
					  # repr()返回的通常可以用来重新获得该对象,有些情况不可以
eval(repr(birthday))  # 1994-12-23  




