#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class generate_list:
	def __init__(self,n):
		l = []
		for i in range(0,n * 2 ):
			if( i < int(n) ):
				l.append("")
				l.append("")
			else:
				l.append("b")
				l.append("a")
		print l
		#print len(l)

if __name__ == "__main__":
	generate_list(int(sys.argv[1]))


