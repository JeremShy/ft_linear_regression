#!/usr/bin/env python

import csv

def estimatePrice(t0, t1, mileage):
	return (t0 + t1 * mileage)

def get_tmp0(learningRate, t0, t1, lst):
	rez = 0.0
	for m,p in lst.items():
		m = float(m)
		p = float(p)
		rez += estimatePrice(t0, t1, m) - p
	rez *= learningRate
	rez *= 1.0 / len(lst)
	return rez

def get_tmp1(learningRate, t0, t1, lst):
	rez = 0.0
	for m,p in lst.items():
		m = float(m)
		p = float(p)
		rez += (estimatePrice(t0, t1, m) - p) * m
	rez *= learningRate
	rez *= 1.0 / len(lst)
	return rez


csvfile = open("data.csv", 'rb')

reader = csv.reader(csvfile, delimiter=',')

lst = dict()
first = False
for r in reader:
	if (first == False):
		first = True
	else:
		k, v = r
		lst[k] = v

t0 = 0
t1 = 1
while True:
	 t0 = get_tmp0(.1, t0, t1, lst)
	 t1 = get_tmp1(.1, t0, t1, lst)
	 print ("t0 : " + str(t0))
	 print ("t1 : " + str(t1))
	 print ""
