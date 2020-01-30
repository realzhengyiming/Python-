# 根据python的特点，这儿把列表当成数组，把引用当成指针

def LNode:
    def __new__(self,x): # 比__init__更先创造的，在创建类的对象时最先创造的方法
        self.data = x  # 存数据
        self.next = None # 指向下一个链表节点

