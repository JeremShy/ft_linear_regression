#!/usr/bin/env python3

import sys
import csv
import json
from pathlib import Path

def estimatePrice(t0, t1, mileage):
	return (t0 + t1 * mileage)

my_file = Path("coef.py")
if my_file.is_file():
	file = open('coef.py', 'r')
else:
	print("No coef file found!")
	exit()
file = open('coef.py', 'r')
js = file.read()
coef = json.loads(js)
t0 = coef["t0"]
t1 = coef["t1"]
try :
	mileage = int(input("mileage : "))
	print("Estimated price: " + str(estimatePrice(t0, t1, mileage)))
except :
	print("A problem happened")
