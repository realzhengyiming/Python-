# -*- coding: utf-8 -*

# 此处是使用非orm来操作数据库的简单池化操作的代码
# 2018/9/8 修改成使用连接池的方式来进行数据库的链接
# 需要导入如下的依赖库，如果没有，请 安装 pymysql ,DBUtils
# 提取返回数据的全部变成了返回字典类型
# 这个是连接数据库的东西,这次使用数据库连接池把，使用连接池可以避免反复的重新创建新连接

import traceback
from datetime import date, timedelta

import emoji
import pymysql as pymysql
import time
from DBUtils.PooledDB import PooledDB

# 这个是从配置文件（同级目录下）config.py中加载链接数据库的数据
# mysqlInfo 中格式如下放着就可以,也可以直接使用,把__init__函数中需要链接部分直接替换即可
# mysqlInfo = {
#     "host": '127.0.0.1',
#     "user": 'root',
#     "passwd": '123456',
#     "db": 'test',   #改同一个数据库了。
#     "port": 3306,
#     "charset": 'utf8'  #这个是数据库的配置文件
# }

from config import mysqlInfo


class DB:  

    __pool = None   #这个也是静态的属性

    def __init__(self):
        # 构造函数，创建数据库连接、游标，默认创建一个对象就获得一个连接，用完后就关闭就可以了
        self.coon = DB.getmysqlconn()  #这个是默认创建出来的东西
        self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)

    # 数据库连接池连接
    @staticmethod   # 这个是静态的方法可以直接调用的
    def getmysqlconn():  # 从连接池里面获得一个连接
        if DB.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=2, maxcached=20, host=mysqlInfo['host'],
                                  user=mysqlInfo['user'], passwd=mysqlInfo['passwd'], db=mysqlInfo['db'],
                                  port=mysqlInfo['port'], charset=mysqlInfo['charset'])
            # print(__pool)
        return __pool.connection()
        # 释放资源

    def dispose(self): #这儿只能断默认初始化的那个连接
        self.coon.close()
        self.cur.close()


    def ifExists(self,webTitle):
        coon = DB.getmysqlconn()  # 每次都默认获得一个新连接来进行相关的操作
        cur = coon.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "SELECT * FROM tengxun WHERE title='%s'and urlState='True';"
        #因为这儿没有加上try，catch，所以出问题
        try:
            cur.execute(sql%(webTitle))
        except Exception as e:
            print(e)
            print("函数ifExists出问题了，你检查一下")
            print(sql%(webTitle))
        rowNumber = cur.rowcount
        if rowNumber>0:
            return True
        else:
            return False


# ------- 下面可以日常的直接编写操作数据库的代码---------------

    # 
    def __query__(self,sql):  # 自定义查询,返回字典的类型
        coon =DB.getmysqlconn()  # 每次都默认获得一个新连接来进行相关的操作
        cur = coon.cursor(cursor=pymysql.cursors.DictCursor)  # 这儿这个选项是设置返回结果为字典的类型，如果默认的话，那就是列表i
        # ----- 标准的查询模块 ---下面就是执行的部分
        cur.execute(sql)
        URLs = cur.fetchall()   # 返回数据的列表，可以设置返回的是字典
        # -----
        cur.close()
        coon.close()
        return URLs

  
    # 更新部分的例子，sql语句不同而已
    def updateById(self,id):
        coon =DB.getmysqlconn()  # 每次都默认获得一个新连接来进行相关的操作
        cur = coon.cursor(cursor=pymysql.cursors.DictCursor)

        sql = "update tengxun set hadmix='True' where id = %d;" % int(id)   #就只是更新一下相应的url的状态就可以了
        try:  
            cur.execute(sql)
            # 提交
            coon.commit()
        except Exception as e:
            # 错误回滚
            print("更新出错")
            print(e)
            coon.rollback()
        finally:
            coon.commit() #提交这个事务
            cur.close()
            coon.close()
        

    # 插入的例子
    def insert(self,value): #这个是把网址先存到里面去url，这儿的意思是插入tengxun那个表
        coon =DB.getmysqlconn()  # 每次都默认获得一个新连接来进行相关的操作
        cur = coon.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "insert into testtable (value) values(%s)"
        try:
            cur.execute(sql,value)  # 这样来直接把值替换进行就可以,注意类型
            # 提交
            coon.commit()
        except Exception as e:
            # 错误回滚
            print(sql)
            print(e)
            coon.rollback()
        finally:
            coon.commit() #提交这个事务
            cur.close()
            coon.close()


    # 更新的例子
    def updateContent(self,title,name):  #这三个都看成一部分，一次性的存进去好吧
        coon =DB.getmysqlconn()  # 每次都默认获得一个新连接来进行相关的操作
        cur = coon.cursor(cursor=pymysql.cursors.DictCursor)

        Hcontent = str(Hcontent)
        Tcontent = str(Tcontent)
        Acontent = str(Acontent) #beautiful标签转制一下不然就是tag

        # print(url)  之前是这儿的语句错了嘛，还以为哪儿的问题
        sql = "update tengxun set  title='%s' where name='%s'"
        try:
            cur.execute(sql,(title,name))
            # 提交
            coon.commit()
        except Exception as e:
            # 错误回滚
            print("更新失败")
            print(e)
            coon.rollback()
        finally:
            coon.commit() # 提交这个事务
            cur.close()
            coon.close()


if __name__ == "__main__":  # 下面都是用来测试用的。

    chak = DB()
    # chak. 测试用调用

    print("DB finish!")




