#!/usr/bin/env python

import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

def estimatePrice(t0, t1, mileage):
	return (t0 + t1 * mileage)

t0 = 0.0
t1 = -0.99999999999

if (len(sys.argv) != 2):
	print("Usage : ./visu.py filename")
	sys.exit(0)
filename = sys.argv[1]


csvfile = open(filename, 'rb')

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
