#导入模块
import requests
from bs4 import BeautifulSoup
from requests.models import Response

#发送请求，获取内容
Response = requests.get("https://ncov.dxy.cn/ncovh5/view/pneumonia")
homepage = Response.content.decode()

#使用beautifulsoup提取疫情数据
soup = BeautifulSoup(homepage, 'lxml')
script = soup.find(id="getListByCountryTypeService2true")

print(script.string)

