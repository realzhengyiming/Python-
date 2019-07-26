#coding=utf-8
# 此处使用chrome复制的cookie，暂时我也不知道这个东西能用多久，尚未测试。这应该就是基本的cookie池操作的单例版本
import requests
from bs4 import BeautifulSoup
cookie = '''*此处直接粘贴chrome 在各种网站登陆过后调试界面复制出来的cookie 就可以访到登陆过后的页面*'''
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
'Connection': 'keep-alive',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Cookie': cookie}
url = 'https://cart.taobao.com/cart.htm?spm=a21bo.2017.1997525049.1.eec811d9r8X9Op&from=mini&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739'  # 购物车 此处测试的是淘宝的购物车，登陆后的，验证成功 2019-7-26
wbdata = requests.get(url,headers=header).text
print("正在打开请求")
soup = BeautifulSoup(wbdata,'lxml')
print(soup)