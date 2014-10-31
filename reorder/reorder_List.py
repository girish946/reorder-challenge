#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generate_list import Generate_List

class Reorder:
	def __init__(self,n):
		templist = Generate_List(n).getList()
		self.l = templist[templist.index("b") -1 : ]
		self.xchg_left = []
		self.xchg_right= []
		self.loop = len(self.l) - 3
		if n % 2 == 1:
			self.middle = ( (len(self.l) +1  ) / 2 ) 
		else:
			self.middle = ( (len(self.l)  ) / 2 ) 
		self.temp = " "
		#print l
		self.prev = 0
		
		for i in range(1,self.loop/2 + 2,2):
			self.xchg_left.append(i)
		
		for i in range(self.middle,len(self.l)-1,2):
			self.xchg_right.append(i)
		self.xchg_right.reverse()
		self.start()


	def exchange(self,src,dest):
		temp = self.l[dest]
		self.l[dest] = self.l[src]
		self.l[src] = temp
		print "switching : "+str(src) +" to " +str(dest)

	def start(self):
		self.exchange(self.middle , self.prev)
		self.prev= self.middle

		for i in range(len(self.xchg_right)):
			if not self.xchg_left[i] == self.prev :
				self.exchange(self.xchg_left[i] , self.prev )
				self.prev = self.xchg_left[i]
			if not self.xchg_right[i] == self.prev :
				self.exchange(self.xchg_right[i] ,self.prev )
				self.prev = self.xchg_right[i]
		if not self.xchg_right[len(self.xchg_right) -1] == self.prev and   self.xchg_left[len(self.xchg_left) -1] == self.prev :
			self.exchange(self.xchg_right[len(self.xchg_right) -1] , self.prev )
			self.prev = self.xchg_right[len(self.xchg_right) -1]
		if not self.xchg_left[len(self.xchg_left) -1] == self.prev and  self.xchg_right[len(self.xchg_right) -1] == self.prev :
			self.exchange(self.xchg_left[len(self.xchg_left) -1] , self.prev )
			self.prev = self.xchg_left[len(self.xchg_left) -1]
		while self.l.index("b") < self.middle - 1:
			temp = self.l.index("b")
			self.exchange(temp,self.prev)
			self.prev = temp
			if self.prev == temp:
				temp = self.prev
				break
		self.exchange(len(self.l)-1 , self.prev )
		#print str(self.l)
	def getList(self):
		return self.l 


