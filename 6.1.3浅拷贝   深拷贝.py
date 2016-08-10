# -- coding: utf-8 --

# 浅拷贝   深拷贝


person = ['name',['saving',100]]
person1 = person[:]
person2 = list(person)

person[1][0] = 'having'
person[0] = 'age'
person2[0] = 'sex'

print person,person1,person2 
 # ['age', ['having', 100]] ['name', ['having', 100]] ['sex', ['having', 100]]

'''序列类型对象默认是浅拷贝
	以下操作会导致浅拷贝
	(1)完全切片操作[:]
	(2) 利用工厂函数,比如 list(),dict()等
	(3)使用 copy 模块的 copy 函数.
	
	浅拷贝对list集合中可变的类型才有影响
'''

# copy.deepcopy() 可以进行深拷贝