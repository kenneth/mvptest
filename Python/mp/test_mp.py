#!/usr/bin/env python
#coding=utf-8
#CPU密集型程序会充分利用服务器的CPU资源

from multiprocessing import Process
import time,os,sys,math

def f(name):
	print 'hello ',name
	print os.getppid() #取得父进程ID
	print os.getpid()  #取得进程ID
	sys.stdout.flush()
	for i in xrange(10000000):
		math.sqrt(i**2)
	print name,'ok'
	sys.stdout.flush()

def main():
	process_list = []
	for i in range(10):
		p = Process(target=f,args=(i,))
		p.start()
		process_list.append(p)
	for j in process_list:
		j.join()

if __name__ == '__main__':
	main()