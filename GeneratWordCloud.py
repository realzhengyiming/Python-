#-*- coding:utf8 -*-
# need to install  wordcloud,PIL,numpy,jieba
# a wordCloud sample here
# 简单的词云生成扔在这儿备用。

from wordcloud import WordCloud
import jieba
import os


class MakeWordCloud:
    def __init__(self,path):
        # print("设置的路径是")
        # print(path)
        if path == "" or path == None:
            print("使用默认路径")
            self.path = "image"
        else:
            print("使用自定义路径")
            self.path = path # 一开始就可以配置默认的路径
        
        # 并且生成路径  多级目录 mkdir()  这个是生成一级目录用的。
        # if not os.path.exists(path):
        #     os.makedirs(path)


    def trans_CN(self,text):
        #中文要进行分词，不像英文自动有空格
        wordlist = jieba.cut(text)
        result = ' '.join(wordlist)
        return result


    def Gen_WordCloud(self,text,fileName):  # 默认保存的文件夹,path ="" 为当前目录下
        # 输入：text文章内容，Newsid文章的id号
        # 输出：image_path对应词云图片的路径
        text = self.trans_CN(text)  # 分词
        # mask = np.array(image.open('./static/images/cloud.png'))#如果要把词云形状弄成特定图形要用该语句
        wordcloud = WordCloud(
            # mask=mask,
            font_path = "C:\Windows\Fonts\simhei.ttf", # 加载中文字体
            background_color='white', # 背景色
            # max_words=2000,#允许最大词汇
            # max_font_size=60 #最大号字体
        ).generate(text)
        
        image_produce = wordcloud.to_image()
        name = str(fileName)+".png" # 构造文件名
        if not os.path.exists(self.path):
            if self.path.find("/") != -1 or self.path.find("\\") != -1:
                os.makedirs(self.path)  # 多级目录的话就使用这种生成多级目录的方式
            else:
                print("使用单个目录")
                print(self.path)
                os.mkdir(self.path)
        save_path =self.path+"/"+name # 保存的完整路径
        wordcloud.to_file(save_path) # 保存词云
        # print("save to :",save_path)
        # image_produce.show()
        # return img_path
        print("生成完成")




if __name__=="__main__":
    # 1.设置生成路径，2.生成词云，输入 文本 和 文件 名即可
    fileName = "test"
    text = '近日，上汽大通官方公布了全新MPV车型G20的最新官图，从此次公布的官图中不难看出，大通G20在外形轮廓上沿用了家族式设计。大灯采用了全LED光源，造型极具科技感。内饰中控区采用了悬浮式设计，营造出了更多的储物空间。据悉，大通G20将在2019上海车展期间正式亮相。从官图细节中可以看出，大通G20的前脸设计相比G10车型焕然一新。不规则形状的大灯和硕大的进气格栅相连接，其大灯内部结构也更加复杂，采用全LED光源。侧面轮廓上，大通G20采用了悬浮式车窗设计。尾灯同样采用全LED光源，两侧尾灯之间采用镀铬条相连，尾部采用字母logo居中的形式，而非图形logo。内饰部分，厂方着重强调了悬浮式中控设计。从官图中可以看出，大通G20采用了旋钮式换挡操作，换挡旋钮四周集成了众多驾驶辅助功能，视觉效果上具备更强的科技感。而悬浮式设计则为底部营造了更大的储物空间，便于放置乘客带上车的手包或其它物品。目前，官方暂未透露新车将会搭载哪款动力总成。根据推测，大通G20有望搭载2.0T汽油发动机和1.9T柴油发动机，预计在2019年上海车展期间正式亮相。'
    makeWordCloud = MakeWordCloud(path=None)  # 使用默认路径
    makeWordCloud.Gen_WordCloud(text,fileName)