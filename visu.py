#!/usr/bin/env python

import sys
import csv
import matplotlib.pyplot as plt

def estimatePrice(t0, t1, mileage):
	return (t0 + t1 * mileage)

t0 = 0
t1 = 0

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
		try:
			k, v = r
			data[float(k)] = float(v)
		except :
			pass

xmin = min(data.keys());
xmax = max(data.keys());

diff = (xmax - xmin) / 4
xmin -= diff;
xmax += diff;

p1 = [xmin, xmax];
p2 = [t0 + t1 * xmin, t0 + t1 * xmax]

fig, ax1 = plt.subplots()

plt.plot(data.keys(), data.values(), 'ro')
plt.plot(p1, p2, marker = 'o', scalex=False, scaley=False)

plt.show()
