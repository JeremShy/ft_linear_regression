#!/usr/bin/env python

import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

def estimatePrice(t0, t1, mileage):
	return (t0 + t1 * mileage)

t0 = 0.0
t1 = -0.99999999999

try :
	mileage = int(raw_input("mileage : "))
	print "Estimated price: " + str(estimatePrice(t0, t1, mileage))
except :
	print "A problem happened"

csvfile = open("data.csv", 'rb')
