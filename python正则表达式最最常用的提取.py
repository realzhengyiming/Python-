import re

# 这个是提取出两个符号之间的正则表达式
# "(?<=\\().*?(?=\\)"  这个是匹配 （）小括号内的内容
text = "{'isLogin': False, 'isMobile': True, 'product': {'productId': 10674966, 'verifyStatus': 5, 'hostId': 248132382, 'gisId': 1254269, 'price': 10000, 'discountPrice': 9000, 'discountActiveId': 88, 'discountShow': '首单专享每晚9折,2019.06.27-2020.12.31期间入住可用', 'rentType': 1, 'productType': 1, 'title': '【小时光 公寓】朦胧灰北欧风,极简艺术,适合情侣,风情浪漫,近地铁200米,广州塔,琶洲会展中心'"
discountprice = re.findall("(?<=discountPrice\\'\\:).*?(?=\\,)",text)  # 返回找到的所有字符串的列表，非常好用
print(discountprice)

# 非常容易 提取   
