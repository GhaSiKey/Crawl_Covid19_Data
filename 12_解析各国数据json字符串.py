import requests
from bs4 import BeautifulSoup
import re, json

#发送请求，获取内容
Response = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")
homepage = Response.content.decode()

#使用beautifulsoup提取疫情数据
soup = BeautifulSoup(homepage, 'lxml')
script = soup.find(id="getListByCountryTypeService2true")
text = script.string

#使用正则表达式提取json
json_str = re.findall(r'\[.+\]',text)[0]

#把json字符串转换为python类型数据
last_day_corona_virus = json.loads(json_str)
print(last_day_corona_virus)