# -- coding:utf-8 --

'''
	__init__()它并不创建实例,它仅仅是你的对象创建后执行的第一个方法。
	
'''

class Book(object):
	book_num = 0  # 初始化类的变量
	def __init__(self,name,price):
		self.name = name
		self.price = price
		Book.book_num += 1  # 改变类变量
	def showBook(self):
		print self.__class__.__name__  # 相当于 self.name
		print self.__class__  #  类的名字
		print "这本书的价格是:" + str(self.price) + " 这本书的id是 " +  str(Book.book_num)


book = Book('leetcode',80)
book1 = Book('TCP/IP详解',67)

book.showBook()
book1.showBook()
