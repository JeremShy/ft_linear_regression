#!/usr/bin/env python

import sys
import csv

def estimatePrice(t0, t1, mileage):
	return (t0 + t1 * mileage)

t0 = 8499.59349202
t1 = -0.0214489050367

try :
	mileage = int(raw_input("mileage : "))
	print "Estimated price: " + str(estimatePrice(t0, t1, mileage))
except :
	print "A problem happened"
