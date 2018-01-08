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
	rez *= 1.0 / len(lst)
	return float(t0) - rez

def get_tmp1(learningRate, t0, t1, lst):
	rez = 0.0
	for x,y in lst.items():
		x = float(x)
		y = float(y)
		rez += (estimatePrice(t0, t1, x) - y) * x
	rez *= learningRate
	rez *= 1.0 / len(lst)
	return float(t1) - rez
#
#
csvfile = open("data.csv", 'rb')

reader = csv.reader(csvfile, delimiter=',')
lst2 = dict()
first = False

for r in reader:

	if (first == False):
		first = True
	else:
		k, v = r
		lst2[float(k)] = float(v)  

maxx = 0
maxy = 0
boole = False

for x, y in lst2.items():
    if (boole == False or maxx < x):
        maxx = x
    if (boole == False or maxy < y):
        maxy = y
        boole = True

max = float(max(maxx, maxy))


p10 = 1
while (max > 10):
    p10 *= 10
    max /= 10

lst = dict()
for x, y in lst2.items():
    lst[x / p10] = lst2[x] / p10

learningRate = 0.01
t0 = 0
t1 = 0

cont = True

previous0 = 0.0
previous1 = 0.0

while cont:
    previous0 = t0
    previous1 = t1
    t0 = get_tmp0(learningRate, t0, t1, lst)
    t1 = get_tmp1(learningRate, t0, t1, lst)
    if (abs(previous0 - t0) < 0.00000000000001 and abs(previous1 - t1) < 0.00000000000001):
        cont = False

t0 *= p10
print ("t0 : " + str(t0))
print ("t1 : " + str(t1))


file = open('first.py', 'r')
filedata = file.read()

filedata = filedata.replace('t0 = 0', 't0 = ' + str(t0))
filedata = filedata.replace('t1 = 0', 't1 = ' + str(t1))

file = open('first.py', 'w')
file.write(filedata)
