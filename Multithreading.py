# -*- coding: utf-8 -*

import datetime
import multiprocessing
import os
import schedule
import time


def worker_1(interval):
    print("work_1 is working ")
    # 用的时候把你要运行的函数放这儿执行
    time.sleep(3)

def worker_2(interval):
    print("work_2 is working ")
    # 用的时候把你要运行的函数放这儿执行
    time.sleep(3)


class AutoRunAtTime:              #这儿应该是三个线程的
    def job(self,name):   #这个是主线程把
        print('这里是进程: %sd   父进程ID：%s' % (os.getpid(), os.getppid()))
        p1 = multiprocessing.Process(target=worker_1, args=(6,))
        p2 = multiprocessing.Process(target=worker_2, args=(3,))
        # p3 = multiprocessing.Process(target=worker_3, args=(4,))

        p1.daemon = True
        p2.daemon = True

        p1.start()
        p2.start()
        # p3.start()
        print("The number of CPU is:" + str(multiprocessing.cpu_count()))
        for p in multiprocessing.active_children():
            print("child   p.name:" + p.name + "\tp.id" + str(p.pid))

        p1.join()
        p2.join()

        print("today work done ND!!!!!!!!!!!!!!!!!")  # 这是是主线程，如何让主线程等待子线程结束后才输出呢


    def startAutoRun(self,timeSet):         # 24小时制的时间输入，传入一个时间的字符串
        name = "hello"
        # schedule.every(10).minutes.do(job, name)
        # schedule.every().hour.do(job, name)
        schedule.every().day.at(timeSet).do(self.job, name)  # 应该也是24小时制的，记得  “输入24小时制的时间字符串
        # schedule.every(5).to(10).days.do(job, name)
        # schedule.every().monday.do(job, name)
        # schedule.every().wednesday.at("13:15").do(job, name)

        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__=="__main__":
    autoRun = AutoRunAtTime()
    print(time.strftime('%Y.%m.%d', time.localtime(time.time())))
    print("现在的时间是")
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    timeSet= input("请输入定时的时间 ，24小时为一个周期，格式为00:00 (时分）")
    autoRun.startAutoRun(timeSet)    # 测试直接这儿写运行时间比较方便，这个是定时多线程的script，每天定时多个线程跑worker_1 worker_2








