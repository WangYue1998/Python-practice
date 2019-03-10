#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 17:30:17 2017

@author: wy
"""

# set the price, number in a bundle, and discount factor 
2	PRICE = 4.95
3	NUM_IN_BUNDLE = 150
4	DISC_FACTOR = .9
5	
6	# initialize the widgets that remain to be purchased
7	widgets = int(input("How many widgets?"))
8	
9	# calculate the bundles to purchase 
10	bundles = widgets // NUM_IN_BUNDLE
11	
12	# update the widgets that remain to be purchased
13	widgets = widgets % NUM_IN_BUNDLE
14	
15	# calculate the total cost
16	bundle_price = NUM_IN_BUNDLE * PRICE * DISC_FACTOR 
17	cost = bundle_price * bundles + PRICE * widgets
18	
19	#partc
20	print("For", widgets, "widgets,", "purchase", bundles,"bundles","and", widgets,"individual widgets. ")
21	
22	print("Total cost:", cost)