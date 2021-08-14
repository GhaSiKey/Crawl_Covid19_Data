
#导入模块
import requests

#发送请求获取响应
response = requests.get('http://www.baidu.com')

#获取相应数据
#response.encoding = 'utf-8'
#print(response.text)
print(response.content.decode())