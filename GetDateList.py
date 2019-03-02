# coding=utf8
# 这个文件的作用是生成一段日期的字符串，需要相关的操作可以参考这个demo ，主要使用了datetime模块的功能

import time
print (time.time())
print(time.strftime('%Y-%m-%d',time.localtime(time.time())))

import datetime

class TimeHelper:
    def getTimeList(self,start,end):
        # start = start
        # end = end
        dateList = []
        datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
        dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
        while datestart < dateend:
            datestart += datetime.timedelta(days=1)
            # print(datestart.strftime('%Y-%m-%d'))
            dateList.append(datestart.strftime('%Y-%m-%d'))
        return dateList

if __name__ == '__main__':
    timeHelper = TimeHelper() #都用类来进行封装
    timeHelper.getTimeList("2019-3-1","2019-4-24") #自动按日历获取这期间的所有的日期字符串列表
    print()
