#!/usr/bin/env python

import sys

def estimatePrice(t0, t1, mileage):
	return (t0 + t1 * mileage)

t0 = 0
t1 = 0


try :
	mileage = int(raw_input("mileage : "))
	print "Estimated price: " + str(estimatePrice(t0, t1, mileage))
except :
	print "A problem happened"
