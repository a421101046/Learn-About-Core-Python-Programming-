# -- coding: utf-8 --

''' usedecimal.py  Decimal类的使用 '''

from decimal import Decimal

dec1 = Decimal(1)  # 报错  可以用整型  float  bool 以及 这些的字符串形式 初始化
dec2 = Decimal('1.2')
print dec2 + 1   # 只能与整数 或者同类型

