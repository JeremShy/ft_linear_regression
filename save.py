#!/usr/bin/env python

import sys

def estimatePrice(t0, t1, mileage):
	return (t0 + t1 * mileage)

t0 = 0
t1 = 0

if (len(sys.argv) != 2):
	print sys.argv[0] + ":\n\tUsage: " + sys.argv[0] + " mileage"
	sys.exit(0)

mileage = int(sys.argv[1])
print "Estimated price: " + str(estimatePrice(t0, t1, mileage))
