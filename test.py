#!/usr/bin/env python3
# coding: utf-8

# import functools
# if elif  else
# day = int(input('day:'))
# if day > 10:
#   print('>10')
# else:
#   print('<10')



# for
# lists = ['a', 2, 'ab', '4', 'fs']
# for list in lists:
#   print(list)

# rans = list(range(100))
# sum=0
# for ran in rans:
#   sum = sum+ran
# print('1到100总和为：%d%s' % (sum, 'aa'))

# peoples = ['ren1', 'ren2', 'ren3']
# for people in peoples:
#   print('hello word %s' % (people))


# dict = {'ren1': 10, 'ren2': 20}
# print(dict['ren2'])

# set1 = set([ 'b', 'a', 'c'])
# set2 = set(['a', 'd', 'c'])
# c = [2,5,23,1,3,76,32]
# a = set1 | set2; b = set1 & set2;  c.sort()
# print(a, b, c)

# 函数
# x = int(input('请输入x：'));

# def myfun(x):
#   if  x>10:
#       print('>10');
#   elif x==10:
#       print('==10');
#   else:
#       print('<10')
# myfun(x)
# def nop():    #定义空函数
#   pass
# def my_abs(x):
#   if not isinstance(x, (int, float)):
#       raise TypeError('输入类型错误')
#   else:
#       print(abs(x))

# my_abs(input('input x:'))

# def power(x, n=4):
#   s = 1
#   while n > 0:
#       n = n-1;
#       s = s*x
#   return s
# print(power(int(input('x:')), int(input('n:'))))

# 切片
# L = ['A', 'B', 'C', 'D']
# print(L[0:3])
# print(L[:3])
# print(L[:-1])
# print(L[-1:])
# L = list(range(100))
# print(L[2:-10:2]) # 2-89 每各2个输出


# 迭代
# dict = {1:'a', 2:'b', 's':'31', 'a':4}
# for key, value in dict.items():
#   print(key, value)


# 列表生成式
# L = []  
# for x in range(1,10):         #普通方法
#   L.append(x*x)
# L = [x*x for x in range(10)]  #高级用法
# L = [x*x for x in range(100) if x % 2 ==0]  #还可以判断再使用
# L = [m + n for m in 'ABC' for n in 'XYZ']   #两个字符串拼接 双层循环
# import os
# L = [d for d in os.listdir()]  # 列出当前文件和目录
# s = ['Hello', 'QiChen']
# L = [s.lower() for s in s]  #转小写

# L = ['Hello', 'World', 18, 'Apple', None]
# L = [s.lower() for s in L if isinstance(s, str)]  在for循环下的s进行处理
# print(L)


# 生成器generator
# L = [x*x for x in range(50) if x % 2 ==0]   #list
# g = (x*x for x in range(50) if x % 2 ==0)   #generator
# for x in g:
#   print(x)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#             print(b)
#             a, b = b, a + b
#             n = n + 1
#     return 'done'

# fib(int(input("x:")))
# 杨辉三角
# def triangles():
#     l = [1]
#     while 1:
#         yield l
#         l = [1] + [l[i]+l[i+1] for i in range(len(l)-1)] +[1]
# #  调用
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

# 高阶函数
# def add(x, y, f):
#     return f(x)+f(y)

# print(add(2, -4, abs))   #将一个abs函数名（也算是变量）传入add方法里


# map()函数
# def  f(x):
#     return x*x
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# r = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])  #转化为字符串
# print(list(r))

# reduce函数（和map类似  第一个参数是函数名，第二个是list，第三个是默任开始的数值）

# def add(x, y):
#     return x+y
# r =  functools.reduce(add, range(100))
# print(r)
# 字符串转数字函数
# def trans(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# def add(x, y):
#     return x*10+y
# r = functools.reduce(add, map(trans, input("str:")))
# # 使用匿名函数简化
# r = functools.reduce(lambda x, y: x*10+y , map(trans, input("str:")))
# print(r)

# filter 过滤函数 filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 如果返回False 或者0    还是会丢弃该元素的  返回的是Iterator类型  需要用list显示
# def not_empty(x):
#     if  isinstance(x, int):
#         return x
#     # return x and x.strip()      #  and 若所有值均为真，则返回最后一个值，若存在假，返回第一个假值。
# s = list(filter(not_empty, ['', None, '   ', 1, 0, True, False, 'sdf']))
# print(s)

# def huiwen(n):    #所有的回文
#     s = str(n)
#     if s == s[::-1]:   #切片 负号代码从后开始每隔一个输出
#         return True
# print(list(filter(huiwen, range(1000))))

# sorted() 函数  
# sorted([-19, -1, 0, 3, -3, 42, 3, 4]) #默认从小到大
# sorted([-19, -1, 0, 3, -3, 42, 3, 4], key=abs) #按abs() 来排序绝对值大小
# sorted(['bob', 'about', 'Zoo', 'Credit']) #安装ascii大小排序
# sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)  #转化为小写
# sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)  #加上reverse 进行反响排序

# 注意　key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。　并不修改结果　相当于给每个值都加一个key用key来排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     N = []
#     N.append(t[0])  #按照名称排序　换成t[1]就是按照成绩排序
#     return N
# L2 = sorted(L, key = by_name)   
# print(L2)


# 函数作为返回值:  
# def sum(*args):   #这是普通的求和方法  一个星(*)号 代表这可以接受多个参数类型是(tuple)  两个星(*)号也是代表接受多个参数 类型是(dict)
#     s = 1
#     print(type(args))
#     for arg in args:
#         s = s*arg
#     return s
# print(sum(1,2,3,4,5))

# def lazy_sum(*args):
#     def sum():
#         s = 1
#         for arg in args:
#             s = s*arg
#         return s  #注意返回的是函数名 没有括号的
#     return sum
# print(lazy_sum(1,2,3,4,5))  #这个是返回的<function lazy_sum.<locals>.sum at 0x7f254f11f840>类型的
# 而要想调用 就使用 lazy_sum(1,2,3,4,5)()   就可以了


# 闭包   原理上返回函数不能引用任何循环变量
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i*i
#         fs.append(f)  #f(i)  没有立刻执行 当全部循环完 i已经为3了
#     return fs
# f1, f2, f3 = count()    这个调用f1() f2() f3()全部返回9的

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f1, f2, f3 = count()

# 装饰器 decorator
# def log(test):
#     def decorator(func):
#         def warpper(*args, **kw):
#             print('%s: %s' % (test, func.__name__))
#             return func(*args, **kw)
#         return warpper
#     return decorator

# @log('execute')
# def now():
#     print(111)
# now()

# 偏函数
# x = int('100110', base=2) #就可以做N进制的转换：
# f = functools.partial(int, base=2)  #偏函数
# print(f('100111'))

# 第三方模块 (pip install Pillow)
# from PIL import Image
# im = Image.open('./test.png')
# print(im.format, im.size, im.mode)
# im.thumbnail((200, 100))
# im.save('thumb.jpg', 'JPEG')


# 面向对象编程
# 类
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#     def print_info(self):
#         print('姓名 : %s,    分数:%d' % (self.__name, self.__score))
# person = Student('qichen', 100)
# person.print_info()
# print(person.)

# 继承
# class parent(object):
#     def __init__(self):
#         self.name = 'new person'
#         print(__name__)
#     def call(self):
#         print(1)


# class son1(parent):
#     def call(self):
#         print(self.name)

# class son2(parent):
#     def __init__(self):
#         self.name='son2'

# # son1().call()
# # son2()
# # print(type(1))
# import types
# def fn():
#     pass
# type(fn)==types.FunctionType #True
# type(abs) == types.BuiltinFunctionType #True
# type(lambda x: range(10)) == type.LambdaFunctionType #True

# class Student(object):
#     name = 'Student'  #类属性名

# stu = Student()

# def addMethod(self, x):
#     return x**x
# from types import MethodType

# stu.addMethod = MethodType(addMethod, stu)  # 给实例stu绑定方法
# Student.addMethod = MethodType(addMethod, stu)  # 给类本身Student绑定方法
# print(stu.addMethod(10))


# __slots__
# class Student(object):
#     __slots__ = ('name')  # 用tuple定义允许绑定的属性名称

# stu = Student()
# stu.name = 'qichen'
# # stu.age = 100   # 绑定属性'age' 出错 AttributeError: 'Student' object has no attribute 'age'
# print(stu.name)


# #  @property
# class Screen(object):
#     # __slots__ = ('width', 'height', 'resolution')
#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self, value):
#         self._width = value

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self, value):
#         self._height = value

#     @property
#     def resolution(self):
#         return self._width*self._height

# sc = Screen()
# sc.width = 10
# sc.height = 20
# print(sc.resolution)

# 定制类  __str__ , __repr__
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def __str__(self): # 专门用于print的方法
#         return 'the Student object of %s' % self.name
#     __repr__ = __str__   #专门用于程序开发者的方法
# print(Student('xuesheng'))


# 操作文件和目录
# import os
# print(os.name) #linux is posix

# while 1:
#     file = open('a.html', 'a')
#     file.write('1fads')
#     file.close()
    
# 异常模式  使用try except模式
# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except Exception as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# 使用调试器pdb  命令行输入python -m pdb test.py   然后一直按n  他会一步一步执行 有错会爆出来 
# s = '0'
# n = int(s)
# print(10 / n)

# 文档测试
# class Dict(dict):
#     '''
#     Simple dict but also support access as x.y style.

#     >>> d1 = Dict()
#     >>> d1['x'] = 100
#     >>> d1.x
#     100
#     >>> d1.y = 200
#     >>> d1['y']
#     200
#     >>> d2 = Dict(a=1, b=2, c='3')
#     >>> d2.c
#     '3'
#     >>> d2['empty']
#     Traceback (most recent call last):
#         ...
#     KeyError: 'empty'
#     >>> d2.empty
#     Traceback (most recent call last):
#         ...
#     AttributeError: 'Dict' object has no attribute 'empty'
#     '''
#     def __init__(self, **kw):
#         super(Dict, self).__init__(**kw)

#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

#     def __setattr__(self, key, value):
#         self[key] = value

# if __name__=='__main__':
#     import doctest
#     doctest.testmod()


# 操作文件和目录
# import os

# os.name #操作系统类型
# os.uname() #详细的系统信息

# mypath = os.path.abspath('.')  #当前目录的绝对路径

# new_dir = os.path.join('.', 'testdir')  #得出 /tmp/test/testdir  不用字符串拼接  使用这个函数可以正确处理不同操作系统中的分隔符
# os.mkdir(new_dir)
# os.rmdir(new_dir)
# split_dir = os.path.split(new_dir)
# print(split_dir) # 得到('.', 'testdir')
# ext = os.path.splitext(os.path.abspath('.')+'/a.txt') #获取文件后缀
# print(ext)  #得到('/mydata/var/www/python/a', '.txt')
# os.mknod('test.txt') #创建文件
# os.rename('test1.png', 'test.png')
# os.remove('test1.txt')
# import shutil
# shutil.copyfile('test.txt', 'text.php')  #os模块是没有cp文件的方法  shutil相当于os的扩展
# a = [x for x in os.listdir('.') if os.path.isdir(x)]  #列出当前目录下所有的文件夹
# a = [x for x in os.listdir('./spider') if os.path.isfile(os.path.abspath('./spider')+'/'+x) and os.path.splitext(x)[1] == '.py'] #列出目录下所有的py文件

# import pickle  #序列化

# d = dict(name = 'qichen', age = 23)
# pi = pickle.dumps(d)  #
# f = open('test.txt', 'wb')
# # f.write(pi)  #和下面哪个写的数据一样
# pickle.dump(d, f)  #意对象序列化成一个byte   然后存入文件
# f.close()

# f = open('test.txt', 'rb')
# d = pickle.load(f)   #反序列化
# print(d)

# json 序列化
# import json
# d = dict(name = 'abc', id = 222, ss = 3)
# js = json.dumps(d)  # '{"id": 222, "name": "abc", "ss": 3}'
# json.loads(js) # {'id': 222, 'name': 'abc', 'ss': 3}

# # json序列化对象
# class A(object):
#     def __init__(self, name = 'na', age = 10):
#         self.name = name
#         self.age = age

# def classdict(obj):
#     return {
#         'name': obj.name,
#         'age': obj.age
#     }

# a = A('qichen', 23)

# j = json.dumps(a, default=classdict) #序列化对象成json

# def dictclass(json):
#     return A(json['name'], json['age'])

# print(json.loads(j, object_hook=dictclass)) #返回对象


# 多进程多线程
# import os
# print('process %d start' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('我是子进程%d 父进程是%d' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 使用multiprocessing 创建进程
# import multiprocessing, os
# #子进程运行时执行的方法
# def runfun(name):
#     print('the process (%s) is run pid is (%d)' % (name, os.getpid()))

# if __name__ == '__main__':
#     print('Parent process %s' % os.getpid())
#     p = multiprocessing.Process(target = runfun, args=('test',))
#     p.start()
#     p.join()
#     print('child process is close')

# 启动大量进程 Pool
# from multiprocessing import Pool
# import os, time, random

# def task_run_time(name):
#     print('Run task %s (%d)' % (name, os.getpid()))
#     start_time = time.time()
#     time.sleep(random.random()*3)
#     end_time = time.time()
#     print('the process %d run time is %0.2f' % (name, end_time-start_time))

# if __name__ == '__main__':
#     print('Parent process pid is %d' % os.getpid())
#     p = Pool(4)  #同时跑4个进程  如果不传参数默认就是电脑cpu的内核数
#     for i in range(5):
#         p.apply_async(task_run_time, args=(i,)) #第5个进程会延迟执行的
#     print('waiting for all subprocess done')
#     p.close()
#     p.join()  #调用join等待所有子进程执行完毕 调用join之前必须执行close
#     print('All process done')


import subprocess  #subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出

# print('$ nslookup www.baidu.com')
# r = subprocess.call(['nslookup', 'www.baidu.com'])
# print(r)  #返回结果代码  0 代表正确 非0错误

# print('$ mysql -uroot -p123')
# p = subprocess.Popen(['mysql', '-uroot', '-p123'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  #标准输入、输出、错误句柄
# output, err = p.communicate(b'show databases;\nexit\n')  #交互式运行  communicate方法阻塞父进程 等待子进程
# print(output.decode('utf-8'))
# print(err.decode('utf-8'))
# print('Exit Code', p.returncode)

p = subprocess.Popen(["ssh -o 'StrictHostKeyChecking no'  root@bimoxx.com "], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)  #标准输入、输出、错误句柄
output, err = p.communicate(b"php5 ~/EdusohoBackup.php '/var/www/edusoho' 'http://operation-rpc:7000/event.php?time=1500707388&token=2c5ab0fd489fa61f3fea7f4a4a3257bc' '191155' '648'")  #交互式运行  communicate方法阻塞父进程 等待子进程
print('标准输出: ',output.decode('utf-8'))
print('标准错误: ',err.decode('utf-8'))
print('Exit Code', p.returncode)
print('子进程执行的cmd:', p.cmd)

# # 进程间通信
# from multiprocessing import Process, Queue
# import os, time, random

# def write(q):
#     print('Process %d to write' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('put %s into queue' % value)
#         q.put(value)
#         time.sleep(random.random())

# def read(q):
#     print('Process %d to read' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s  from queue' % value)

# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()  #pr里的是死循环   只能强制终止

# 多线程
# import time, threading

# def loop():
#     print('thread %s is running' % threading.current_thread().name)
#     for n in range(5):
#         print('thread %s >>> %d' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s is ended' % threading.current_thread().name)

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='myLoopThread') # 如果没有name参数 python会自动设置为Thread-1  Thread-2等
# t.start()
# t.join()
# print('thread %s is ended' % threading.current_thread().name)

# import threading, multiprocessing

# def loop():
#     x = 0
#     while True:
#         x = x ^ 1

# for i in range(multiprocessing.cpu_count()):  #跑慢cpu  但是cup只有102%左右 只用了1核
#     t = threading.Thread(target=loop)
#     t.start()


# ThreadLocal  使用这个可以避免线程之间数据共享导致数据调用混乱  不用管理锁的问题
# import threading
# local_school = threading.local()   #就是一个ThreadLocal对象,每个Thread对它都可以读写student属性，但互不影响。
# # 这个避免了 线程中函数相互调用导致数据传递起来相当麻烦 的问题
# def thread_student(name):
#     local_school.name = name  #local_schoole.name 相当于每个线程的局部变量
#     print('this student name is %s in thread(%s)' % (local_school.name, threading.current_thread().name))

# th1 = threading.Thread(target=thread_student, args=('zhangsan',), name='Thread-1')
# th2 = threading.Thread(target=thread_student, args=('lisi',), name='Thread-2')
# th1.start()
# th2.start()
# th1.join()
# th2.join()

# 线程和进程对比
# import multiprocessing, threading

# def run_process(x):
#     while(1):
#         x = x
# #  开启2个进程  命令行ps axf 可以看出来一个主进程下有两个子进程  top 可以看出来有两个python进程
# # p1 = multiprocessing.Process(target=run_process, args=('1',))
# # p2 = multiprocessing.Process(target=run_process, args=('1',))
# # p1.start()
# # p2.start()
# # p1.join()
# # p2.join()
# # 开启两个线程 命令行ps 只有一个python进程  top也只有一个进程 但其实有两个线程
# p1 = threading.Thread(target=run_process, args=('1',))
# p2 = threading.Thread(target=run_process, args=('1',))
# p1.start()
# p2.start()
# p1.join()
# p2.join()

# 分布式进程


# 正则表达式 re
# import re
# re.match('aa\\bb', 'aa\\bb')  #匹配失败 \本身要转化的  所以要匹配的就是aa\bb  
# re.match(r'aa\\bb', 'aa\\bb') #使用r 就不会转化\了  r只对双斜杠有用 单斜杠没用

# re.split(r'[\,\s\;]+', 'a,b,    c;; d')  #可以将abcd匹配出来为list

# m = re.match('^(\d{3})-(\d{5})$', '123-43142')
# m.group(0)  #全部的
# m.group(1)  #第一个括号中的
# m.group(2)  #第二个括号中的
# m.groups()  #tuple类型

# 常用模块
# import datetime, time
# print(datetime.datetime.now())  #2017-04-13 17:37:10.673879
# print(time.time())  #1492076230.6739163
# print(datetime.datetime(2017, 4, 13, 17, 36, 59))  #2017-04-13 17:36:59
# print(datetime.datetime.now().timestamp())  #1492076314.932349
# print(datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp())) #2017-04-13 17:43:03.381189
# print(datetime.datetime.utcfromtimestamp(datetime.datetime.now().timestamp())) #2017-04-13 09:44:51.416522 utc的标准时间
# # str转换datetime
# print(datetime.datetime.strptime('2017-4-13 17:47:58', '%Y-%m-%y %H:%M:%S'))


# collections 集合模块
# import collections   #略过

# class A(object):
#     def __init__(self):
#         self.item = {}
#         print('A')

# class myClass(A):
#     """docstring for myClass"""
#     def __init__(self, arg):
#         super(myClass, self).__init__()  #相当于 A.__init__(self) 调用父级类的init   继承
#         print('B')

#     def __getitem__(self, key):    #相当于m.item[key]
#         print(self.item.get(key))

#     def __setitem__(self, key, value):
#         self.item.set[key] =  value


# m = myClass('a')
# m.item[1] = '11111'
# print(m.item, m.item.get(2))

# import hashlib   #加密数据  md5 sha1
# md5 = hashlib.md5()
# md5.update('i am a student'.encode('utf-8'))
# print(md5.hexdigest())

# import itertools   #无限迭代器
# # cs = itertools.cycle('ABC')
# # for n in cs:
# #     print(n)   #会循环输出A, B, C

# # num = itertools.count(1)  #从1开始
# # for n in num:
# #     print(n)

# # ns = itertools.repeat('6', 10) #重复字符6  限定重复次数10次
# # for n in ns:
# #     print(n)

# nsl = itertools.count(5)
# ns = itertools.takewhile(lambda x :  x < 10, nsl)
# print(list(ns))


# import contextlib #用于管理上下文
# from urllib.request import urlopen
# @contextlib.contextmanager
# def tag(name):
#     print('<%s>' % name)
#     yield
#     print('</%s>' % name)

# with tag('h1'):    #with语句首先执行yield之前的语句，因此打印出<h1>；
#     print('hello')   #yield调用会执行with语句内部的所有语句，因此打印出hello和world；
#     print('world')  #最后执行yield之后的语句，打印出</h1>。

# with urlopen('http://www.baidu.com') as f:
#     for i in f:
#         print(i)


# mysql操作数据库
# mysql 防止注入必须使用逗号隔开
# import pymysql
# conn = pymysql.connect(host = 'localhost', user='root', passwd='123', db='edusoho', charset='utf8')
# cursor = conn.cursor()
# stat = cursor.execute('select * from user limit 3')   #print(stat)  出现3   
# result = cursor.fetchall()
# print(result)
# cursor.close()
# conn.close()


# WSGI接口  Web Server Gateway Interface。  模拟nginx apache
# 这个方法是应用程序接口  进行响应处理的 
# def application(environ, start_response):
#     # start_response('200 OK', [('Content-Type', 'text/html')])
#     # return [b'<h1>hello! web!!!!</h1>']
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     print(environ['PATH_INFO'])
#     body = '<h1>hello! %s' % (environ['PATH_INFO'][1:] or 'web')  #读取环境变量里的path_info
#     return [body.encode('utf-8')]

# # 启动WSGI服务器  导入
# import wsgiref.simple_server

# httpd = wsgiref.simple_server.make_server('', 8001, application)
# print('Serving HTTP on port 8001')
# httpd.serve_forever()



# 协程   python 是通过generator  生成器实现的  
# import time
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('consumer  exec %s' % n)
#         time.sleep(1)
#         r = '200 OK'

# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n+1
#         print('produce producing %s' % n)
#         r = c.send(n)
#         print('consumer return %s' % r)
#     c.close()

# c = consumer()
# produce(c)

# 异步io
# import asyncio
# @asyncio.coroutine
# def hello():
#     print('hello world!')
#     r = yield from asyncio.sleep(1)
#     print('hello again!')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


# import subprocess

# p = subprocess.Popen(['ssh root@bimoxx.com'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
# out, err = p.communicate(b'ps axf | wc -l')
# print(out)
# print(err)

# 装饰器
# def a(arg):
#     def fun(arg):
#         print('this arg is %s' % arg)
#     return fun

# @a
# def b(arg):
#     print(b)
    
# b(1)

#         