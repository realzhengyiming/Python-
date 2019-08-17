# -*- coding: utf-8 -*

# 下载到的一个路径中去，把图片下载下来，并且把新闻里面的
import os
import time
import traceback
import requests ##导入requests
import hashlib
# from config import downloadPath
from config import downloadPath   # 这个是自己定义好的配置文件，一般可以放在相同目录下，可以直接访问。


class Download:
    def __init__(self,path): # 先设置好下载的路径
        if(path==None):
            self.path=downloadPath['path']  # 默认使用配置文件的地址
            print("是 None")
        else:
            self.path = path

    def makeMd5(self,url):
        obj = hashlib.md5()
        obj.update(bytes(url,encoding="utf-8"))
        return obj.hexdigest()

    def downloadImg(self,img_url,imgName,referer,now_date,**args):   
        '''
        img_url,  图片的下载链接
        imgName,  下载的图片的名字
        referer,  这个参数是请求的时候防止加了referer参数的反反爬虫用的。
        now_date  图片下载到 指定路径下的什么文件夹内，这儿是使用 日期字段  作为文件夹 测试可以随意修改
        proxies ，可选参数，不加就默认无代理，如果添加，需要带上 proxies="ip:port" 结构
        '''

        # 增加断言
        assert img_url!=None , "下载请输入下载链接后调用！"
        assert img_url!="", "下载请输入下载链接后调用！" 
        # assertIsNotNone(now_date , "请输入下载到目录下哪个文件夹中（没有会自动创建）！")
        # assertIsNotNone(img_url , "请输入下载链接后调用！")
        # assertIsNotNone(img_url , "请输入下载链接后调用！")

        # 这里可以加一个断言。这样才比价好一点，防止不可以使用的来适用
        if args.get("proxies")!=None:  
            print("使用的代理ip为 ： {}".format(args.get("proxies")))
        else:
            print("没有使用代理")

        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        'Referer':referer}   ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
        try:
            # int(shit)    # todo 图片可以不下载了
            img = requests.get(img_url, headers=headers,proxies={"http":args.get("proxies")})
            # print(img)
            # print(self.path)
            if(False==os.path.exists(os.path.join(self.path ,now_date))):  # 不存在这个目录的话
                os.makedirs(self.path + '/'+now_date)

            if imgName==None:
                imgName = self.makeMd5(url)  # 如果未给定图片的名字则默认使用url来做的md5作为文件名
            dPath = os.path.join(self.path ,now_date, imgName+'.jpg')  # imgName传进来不需要带时间
            # print(dPath)
            print("图片的文件名 "+dPath)
            f = open(dPath, 'ab')
            f.write(img.content)
            f.close()
            # print("下载成功")
            return dPath
        except Exception as e:
            print(e)
            traceback.print_exc()

if __name__=="__main__":
    # 局部测试代码
    # 1.没有代理版本，
    imgUrl = "http://inews.gtimg.com/newsapp_match/0/5403685404/0"
    downloadTool  = Download(None)  # todo 这儿有一个问题就是，这个图片的下载地址网页部分是带地址的，所以，最好的是网页部分不需要要再加上地址的文件夹，统一使用
    downloadTool. downloadImg (
        img_url="http://inews.gtimg.com/newsapp_match/0/8158252661/0",
        imgName="zhangfei",
        referer=None,
        now_date="20190309")

    # 2.也可以增加多参数，使用代理的版本
    downloadTool. downloadImg (
        img_url="http://inews.gtimg.com/newsapp_match/0/8158252661/0",
        imgName="zhangfei",
        referer=None,
        now_date="20190309",
        proxies="127.0.0.0:8888")