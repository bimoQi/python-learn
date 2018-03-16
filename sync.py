#!/usr/bin/env python3
# coding: utf-8

import pymysql

try:
    conn = pymysql.connect(
    host='localhost', user='root', passwd='123', database="study-online", charset='utf8')
except Exception as e:
    print('mysql conn error: ', e.args[1])

cursor = conn.cursor()
stat = cursor.execute('select id,target from testpaper where name="fa"')
for testpaper in cursor.fetchall():
	testpaperId = testpaper[0]
	courseId = int(testpaper[1].split('-')[1])
	print('testpaperId:%d     courseId:%d' % (testpaperId,courseId))
	courseId = "1 or 1=1"
	# a = cursor.execute("update course_lesson set mediaId=%d where courseId=%d AND title='中级经济基础第九章'" % (testpaperId,courseId))
	a = cursor.execute("SELECT * FROM course_lesson WHERE status='unpublished' AND courseId=%s" , courseId)
	print(a,"\n")
conn.commit()
cursor.close()
conn.close()
