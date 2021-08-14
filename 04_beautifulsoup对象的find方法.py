from typing import Iterable
from bs4 import BeautifulSoup

html = '''<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title">
            <b>The Dormouse's story</b>
        </p>
        <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="" class="sister" id="link1">Elsie</a>
            <a href="" class="sister" id="link2">Lacie</a>
            <a href="" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well
        </p>
        <p class="stroy">...</p>
    </body>
</html>
'''

soup = BeautifulSoup(html,'lxml')

#根据标签进行查找
title = soup.find(name="title")
print(title)

a = soup.find(name='a')
print(a)

a_s = soup.find_all('a')
print(a_s)

#根据属性进行查找
link1 = soup.find(id='link1')
print(link1)

link2 = soup.find(attrs={'id':'link2'})
print(link2)

#根据文本进行查找
Tillie = soup.find(text='Tillie')
print(Tillie)

print(type(a))
print("标签所有属性",a.attrs)
print("标签文本内容",a.text)