#!/usr/bin/env python


import sys
import csv
from math import *

def estimatePrice(t0, t1, mileage):
	return (t0 + t1 * mileage)

def get_tmp0(learningRate, t0, t1, lst):
	rez = 0.0
	for x,y in lst.items():
		x = float(x)
		y = float(y)
		rez += estimatePrice(t0, t1, x) - y
	rez *= learningRate
	rez /= len(lst)
	return t0 - rez

def get_tmp1(learningRate, t0, t1, lst):
	rez = 0.0
	for x,y in lst.items():
		x = float(x)
		y = float(y)
		rez += (estimatePrice(t0, t1, x) - y) * x
	rez *= learningRate
	rez /= len(lst)
	return t1 - rez


if (len(sys.argv) != 2):
	print("Usage : ./second.py filename")
	sys.exit(0)
filename = sys.argv[1]
#
#
try:
	csvfile = open(filename, 'rb')
except:
	print("Error opening " + filename)
	sys.exit(0)

reader = csv.reader(csvfile, delimiter=',')
lst = dict()
first = False
for r in reader:
	if (first == False):
		first = True
	else:
		k, v = r
		lst[float(k)] = float(v)

xs = lst.keys()
ys = lst.values()

if (len(xs) <= 1 or len(ys) != len(ys)):
	print("Error !")
	sys.exit(0)


maxx = max(max(xs), abs(min(xs)))
maxy = max(max(ys), abs(min(ys)))


max = max(maxx, maxy)

if (max == 0):
	print("Error !")
	sys.exit(0)

print ("Max : " + str(max));

print ("maxx : " + str(maxx))
print ("maxy : " + str(maxy))

xs = list(map(lambda x: x / max, xs))
ys = list(map(lambda x: x / max, ys))

lst = dict(zip(xs, ys))

print lst
learningRate = 0.001
t0 = 0.0
t1 = 0.0
cont = True
while cont:
    previous0 = t0
    previous1 = t1
    t0 = get_tmp0(learningRate, previous0, previous1, lst)
    t1 = get_tmp1(learningRate, previous0, previous1, lst)
    if (abs(previous0 - t0) < 0.000000000000001 and abs(previous1 - t1) < 0.00000000000001):
        cont = False
    print("t0 : " + str(previous0))
    print("t1 : " + str(previous1))

t0 = max * t0

print ("t0 : " + str(t0))
print ("t1 : " + str(t1))

file = open('first.py', 'r')
filedata = file.read()
filedata = filedata.replace('t0 = 0', 't0 = ' + str(t0))
filedata = filedata.replace('t1 = 0', 't1 = ' + str(t1))

file2 = open('visu.py', 'r')
filedata2 = file2.read()
filedata2 = filedata2.replace('t0 = 0', 't0 = ' + str(t0))
filedata2 = filedata2.replace('t1 = 0', 't1 = ' + str(t1))

file = open('first.py', 'w')
file2 = open('visu.py', 'w')
file.write(filedata)
file2.write(filedata2)
