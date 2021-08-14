from bs4 import BeautifulSoup

soup = BeautifulSoup("<html>data<html>",'lxml')

print(soup)