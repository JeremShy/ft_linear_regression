#!/usr/bin/env python

import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

def estimatePrice(t0, t1, mileage):
	return (t0 + t1 * mileage)

t0 = 8499.59695301
t1 = -0.021448937947


# try :
# 	mileage = int(raw_input("mileage : "))
# 	print "Estimated price: " + str(estimatePrice(t0, t1, mileage))
# except :
# 	print "A problem happened"

csvfile = open("data.csv", 'rb')

reader = csv.reader(csvfile, delimiter=',')
data = dict()
first = False

for r in reader:
	if (first == False):
		first = True
	else:
		k, v = r
		data[float(k)] = float(v)  

p1 = [0, 300000];
p2 = [t0, t0 + t1 * 300000]
plt.plot(p1, p2, marker = 'o')
plt.plot(data.keys(), data.values(), 'ro')
plt.show()
