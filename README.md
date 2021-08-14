# -
Python+Requests库+BeautifulSoup库爬取丁香园网站全球疫情数据

网络爬虫的概念
1.网络爬虫与浏览器的区别：浏览器是展示数据的，而网络爬虫是采集数据的
2.定义：模拟客户端发送请求相应数据，按照一定规则，自动从万维网上获取信息的程序
3.作用：从万维网上，获取我们需要的信息

Requests请求库
1.requests作用：发送请求，获取响应数据
2.发送get请求：response = requests.get(url)

Beautiful Soup解析库
1.Beautiful Soup可以从HTML或XML中提取数据
2.Beautiful Soup对象的创建：soup = BeautifulSoup(html, ‘lxml’)
3.BeautifulSoup对象的find方法
(1)根据标签名查找：soup.find(‘a’)
(2)根据属性查找：soup.find(‘id=’link1’)或soup.find(atrrs={‘id’:’link1’}
(3)根据文本内容查找：soup.find(text=’Elsie’)
4.Tag对象
(1)Tag对象对英语原始文档中的XML或HTML标签
(2)Tag对象常用属性：name, attrs, text

正则表达式概念与常见语法
1.概念：正则表达式是一种字符串匹配的模式（pattern）
2.作用：从某个字符串中提取符合某种条件的字串
3.语法
(1). 匹配除换行符（\n）以外的所有字符
(2)\d 匹配[0-9]的数字
(3)\w 匹配字母数字_和中文
(4)* 前面的一个匹配模式出现0次或多次
(5)+ 前面的一个匹配模式出现1次或多次
(6)？前面的一个匹配模式出现0或1次

re.findall()方法
1.API
(1)re.findall(pattern, string, flags=0)
(2)作用：扫描整个String字符串，返回所有与pattern匹配的列表
(3)参数：
①Pattern：正则表达式
②String：从这个字符串中查找
③Flags：匹配模式
(4)返回
①返回String中于pattern匹配的结果的列表
2.特点
(1)如果正则表达式中没有()则返回与整个正则匹配的列表
(2)如果正则表达式中有()，则返回()中匹配的内容列表，小括号两边东西都是负责确定提取数据所在位置
3.R原串
(1)正则中使用r原始字符串，能够忽略转移符号带来的影响
(2)待匹配的字符串有多少个\，r原串正则中就添加多少个\即可

Json模块
1.JSON转换为Python： json.loads(s)  json.load(fp)
2.Python转换为JSON:  json.dumps(obj)   json.dump(obj, fp)

采集最近一日世界各国疫情数据
1.发送请求，获取疫情首页
2.从疫情首页中提取最近一日各国疫情字符串
3.从最近一日疫情字符串中，提取json格式字符串
4.把json格式字符串转换为python类型
5.把python类型的数据，以json格式存入文件中

采集从1月23日以来的世界各国疫情数据
1.加载最近一个各国疫情数据
2.遍历各国疫情数据，获取从1月23日以来的各个国家疫情的数据统计URL
3.发送请求，获取从1月23日以来各个国家疫情的json字符串
4.解析各个国家疫情的json字符串，添加到列表
5.以json格式保存数据

采集最近一日全国各省疫情数据
1.发送请求，获取疫情首页内容
2.解析疫情首页内容，获取最近一日各省疫情信息id="getAreaStat"
3.以json格式保存信息

采集从1月22以来全国各省疫情数据
1.加载最近一日全国疫情信息
2.遍历最近一日全国疫情信息，获取各省疫情URL
3.发送请求，获取各省疫情json字符串
4.解析各省疫情json字符串，并添加列表中
5.以json格式保存疫情信息
