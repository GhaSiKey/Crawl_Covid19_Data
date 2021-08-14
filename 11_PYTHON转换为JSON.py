import json

from bs4.dammit import encoding_res

json_str = '''[{"provinceName":"美国","cityName":"","currentConfirmedCount":3424215,"confirmedCount":5494239},
 {"provinceName":"英国","cityName":"","currentConfirmedCount":279163,"confirmedCount":321098}]'''
rs = json.loads(json_str)

#把PYTHON转换为JSON字符串
json_str = json.dumps(rs,ensure_ascii=False)
print(json_str)

#把PYTHON储存到JSON文件
with open("data\\test1.json",'w', encoding='utf-8') as fp:
    json.dump(rs, fp, ensure_ascii=False)
    