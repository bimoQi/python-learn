#!/usr/bin/env python
# coding: utf-8

# 分布式进程  主进程 master
import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

BaseManager.register('get_task_queue', callable=lambda: task_queue)
BaseManager.register('get_result_queue', callable=lambda: result_queue)
manager = BaseManager(address=('', 5000), authkey=b'123abc')
manager.start() #启动queue
task = manager.get_task_queue()
result = manager.get_result_queue()
#放入任务
for i in range(10):
    n = random.randint(0, 10000)
    print('put task %d' % n)
    task.put(n)
#从queue中得到任务
print('Try get results...')
for i in range(10):
    r = result.get(timeout=1000)
    print('Result: %s' % r)

manager.shutdown()
print('master exit')