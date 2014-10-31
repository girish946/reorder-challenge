#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Generate_List:
	def __init__(self,n):
		self.l = []
		for i in range(0,n * 2 ):
			if( i < int(n) ):
				self.l.append("")
				self.l.append("")
			else:
				self.l.append("b")
				self.l.append("a")
		print self.l
	def getList(self):
		return self.l
		#print len(l)

