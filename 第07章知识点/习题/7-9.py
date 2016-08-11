# !/usr/bin/env python
# -- coding:utf-8 --


''' 习题7-9 '''

def tr(srcstr, dststr, string,case=False):
	''' 一个字符翻译程序 功能类似于 Unix 中的 tr 命令 '''
	assert len(srcstr) == len(dststr) ,'srcstr length must be equal to dststr'
	
	# 替换字符串
	arr = list(string)
	length = len(arr)
	if case:
		srcstr = srcstr.lower()
	for i in range(length):
		try:
			tmp = arr[i]
			if case: # 区分大小写
				tmp = tmp.lower()
				
			j =  srcstr.index(tmp)
			arr[i] = dststr[j]
		except:	# 当字符不存在于 原来的字符串的时候 ,继续循环
			continue
	return ''.join(arr)
	


if __name__ == '__main__':
	print tr('12','23','1231231342')
	print tr('','','1231231342')
	print tr('123','1','1231231342')
	print tr('12','23','1231231342')
	print tr('Ab','cC','abdcd',True)


