#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generate_list import Generate_List

class Reorder:
	def __init__(self,n):
		"""
		Initialize the list and all the required variables,
		then reorder the list
		"""
		#generate the list as specified in the problem statement [ '','','','','','','b','a','b','a','b','a']
		self.templist = Generate_List(n).getList()
		#generate another list to perform operations. this list is like ['','b','a','b','a','b','a']
		self.l = self.templist[self.templist.index("b") -1 : ]
		#this list will contain the sequence according to which we have to switch the elements from left side of the list
		self.xchg_left = []
		#this list will contain the sequence according to which we have to switch the elements from right side of the list
		self.xchg_right= []
		
		#initialize other required variables
		self.loop = len(self.l) - 3 
		if n % 2 == 1:
			self.middle = ( (len(self.l) +1  ) / 2 ) 
		else:
			self.middle = ( (len(self.l)  ) / 2 ) 
		self.temp = " "
		#print l
		self.prev = 0
		
		#generate the sequence of elements to switch from left of the list
		for i in range(1,self.loop/2 + 2,2):
			self.xchg_left.append(i)
		#generate the sequence of elements to switch from right of the list
		for i in range(self.middle,len(self.l)-1,2):
			self.xchg_right.append(i)
		self.xchg_right.reverse()

		self.start()


	def exchange(self,src,dest):
		"""
		exchange the given two elements in the list.
		"""
		temp = self.l[dest]
		self.l[dest] = self.l[src]
		self.l[src] = temp
		print str(src) +" to " +str(dest)
		#print str(self.l)

	def start(self):
		"""
		reorder the previously generated list.
		"""
		self.exchange(self.middle , self.prev)#initial switch.
		self.prev= self.middle
		
		#exchange the elements of list l according to the elements in the lists xchg_left and xchg_right
		for i in range(len(self.xchg_right)):
			last_prev = self.prev
			if not self.xchg_left[i] == last_prev :
				self.exchange(self.xchg_left[i] , self.prev )
				self.prev = self.xchg_left[i]
			if not( ( (len(self.l) -1) % 2 ) == 0 and i == len(self.xchg_right) -1):
				if not self.xchg_right[i] == last_prev :
					self.exchange(self.xchg_right[i] ,self.prev )
					self.prev = self.xchg_right[i]
			else:
				pass
		
		#previous loop continues for 0 to len(self.xchg_right) which contains one element less than xchg_left.
		#so exchange the last remaining element in xchg_left.
		if not self.xchg_left[len(self.xchg_left) -1] == self.prev and  self.xchg_right[len(self.xchg_right) -1] == self.prev :
			self.exchange(self.xchg_left[len(self.xchg_left) -1] , self.prev )
			self.prev = self.xchg_left[len(self.xchg_left) -1]
		
		#certain times it is likely that one last "b" is preasent just before the middle of the list.
		#switch it if preasent.
		while self.l.index("b") < self.middle - 1:
			temp = self.l.index("b")
			self.exchange(temp,self.prev)
			self.prev = temp
			if self.prev == temp:
				break

		#final switch between las element of the list (which is "a") to previous place in the list.
		self.exchange(len(self.l)-1 , self.prev )
		#print str(self.l)
	
	
	def getList(self):
		"""
		return the reordered list the list as specified in the problem statement [ '','','','','','a','a','a','b','b','b','']
		"""
		return self.templist[ 0 :len(self.l) -2]   + self.l[0:]


