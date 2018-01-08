#!/usr/bin/env python

import csv
from math import *
from numpy import *

#
# def estimatePrice(t0, t1, mileage):
# 	return (t0 + t1 * mileage)
#
# def get_tmp0(learningRate, t0, t1, lst):
# 	rez = 0.0
# 	for m,p in lst.items():
# 		m = float(m)
# 		p = float(p)
# 		rez += estimatePrice(t0, t1, m) - p
# 	rez *= learningRate
# 	rez *= 1.0 / len(lst)
# 	return rez
#
# def get_tmp1(learningRate, t0, t1, lst):
# 	rez = 0.0
# 	for m,p in lst.items():
# 		m = float(m)
# 		p = float(p)
# 		rez += (estimatePrice(t0, t1, m) - p) * m
# 	rez *= learningRate
# 	rez *= 1.0 / len(lst)
# 	return rez
#
#
# csvfile = open("data.csv", 'rb')
#
# reader = csv.reader(csvfile, delimiter=',')
#
# lst = dict()
# first = False
# for r in reader:
# 	if (first == False):
# 		first = True
# 	else:
# 		k, v = r
# 		lst[k] = v
#
# t0 = 0
# t1 = 1
# while True:
# 	 t0 = get_tmp0(.1, t0, t1, lst)
# 	 t1 = get_tmp1(..1, t0, t1, lst)
# 	 print ("t0 : " + str(t0))
# 	 print ("t1 : " + str(t1))
# 	 print ""


# y = mx + b
# m is slope, b is y-intercept
def compute_error_for_line_given_points(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
	print m_gradient
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def run():
    points = genfromtxt("data.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 0 # initial y-intercept guess
    initial_m = 0 # initial slope guess
    num_iterations = 1000
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points))
    print "Running..."
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points))

if __name__ == '__main__':
    run()
