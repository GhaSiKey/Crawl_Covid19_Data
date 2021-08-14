import re

#返回匹配的结果列表
rs = re.findall('\d+',"chuan123suo1234")
print(rs)

#flag参数的作用,匹配所有字符包括换行符
rs = re.findall('a.bc',"a\nbc")
print(rs)
rs = re.findall('a.bc',"a\nbc",flags=re.DOTALL)
print(rs)
rs = re.findall('a.bc',"a\nbc",flags=re.S)
print(rs)

#分组，定位,只返回括号中的内容
rs = re.findall('a(.+)bc',"a\nbc",flags=re.DOTALL)
print(rs)