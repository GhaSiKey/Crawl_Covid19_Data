#导入正则模块
import re

#字符匹配
rs = re.findall('abc','asdawsdvabcasdfasdfzxcv')
rs = re.findall('a.c',"a#c")
rs = re.findall('a\.c',"a.c")
rs = re.findall('a[bd]c',"abc")

#预定义的字符集
rs = re.findall('\d',"123")
print(rs)
rs = re.findall('\w',"azw_中文%￥")
print(rs)

#数量词
rs = re.findall('\d*',"123")
print(rs)
rs = re.findall('a\d{2}',"a123")
print(rs)