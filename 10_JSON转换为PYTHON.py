import json
#JSON字符串
json_str = '''[{"provinceName":"美国","cityName":"","currentConfirmedCount":3424215,"confirmedCount":5494239},
 {"provinceName":"英国","cityName":"","currentConfirmedCount":279163,"confirmedCount":321098}]'''
rs = json.loads(json_str)
print(rs)
print(type(rs))
print(type(rs[0]))
#JSON文件
with open('data\\test.json',encoding='utf-8') as fp:
    python_list = json.load(fp)
    print(python_list)