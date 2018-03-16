#!/usr/bin/env python
# coding: utf-8

# 分布式进程  任务进程 worker
import time, sys, queue
from multiprocessing.managers import BaseManager

BaseManager.register('get_task_queue')
BaseManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('connect server addr %s' % server_addr)
m = BaseManager(address=(server_addr, 5000), authkey=b'123abc')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d*%d' % (n,n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Exception as e:
        print('Exception is %s' % e) 
print('worker exit.')
