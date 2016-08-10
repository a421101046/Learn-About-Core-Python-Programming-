# !/usr/bin/env python
# -- coding:utf-8 --

def matrixAdd(matrix1,matrix2):
	''' 矩阵加法 '''	
	length = len(matrix1)
	for i in range(length):
		for j in range(length):
			matrix1[i][j] += matrix2[i][j]
	return matrix1
	
def matrixMup(matrix1,matrix2):
	''' 矩阵乘法 '''	
	length = len(matrix1)
	for i in range(length):
		for j in range(length):
			matrix1[i][j] *= matrix2[i][j]
	return matrix1
		
def matrixCmp(matrix1,matrix2,operator):
	''' 对两个矩阵做 + * 操作 '''
	# 判断矩阵的异常
	try:
		if len(matrix1) != len(matrix2) or \
		len(matrix1[0]) != len(matrix2[0]):
			raise Exception()
	except:
		raise Exception( "矩阵必须长宽相同")
	
	# 判断操作符
	if operator == '+':		
		print matrixAdd(matrix1,matrix2)
	elif operator == '*':
		print matrixMup(matrix1,matrix2)
	else:
		print "只支持加法和乘法"
		
	
if __name__ == '__main__':
	matrixCmp([[1,2],[1,2]],[[2,3],[4,5]],'+')
	matrixCmp([[1,2],[1,2]],[[2,3],[4,5]],'*')
	matrixCmp([[1,2],[1,2]],[[2,3],[4,5]],'-')
	matrixCmp([],[[2,3],[4,5]],'-')
