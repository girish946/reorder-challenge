#!/usr/bin/env python
# -*- coding: utf-8 -*-

from reorder.reorder_List import Reorder
"""	
run:
	$python reorder.py
"""
if __name__ == "__main__":
	l = Reorder( int(raw_input("enter the number of pairs ")) ).getList()
	print l
