#导入模块
import requests

#发送请求，获取响应
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')

#从响应中，获取数据
print(response.content.decode())