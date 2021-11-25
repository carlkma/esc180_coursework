# civ.py
# CIV102 Bridge Project

# Fall 2021
# Group 403
# Group Members:
#  - Carl Ma
#  - Abdullah Fawzy
#  - Albert Zhang


# ------------------------------ IMPORT MODULES ------------------------------ #
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------ CONSTANTS: Material Property ------------------------------ #

DIM = [813,1016,1.27]
T_STRENGTH = 30
C_STRENGTH = 6
SHEAR_STRENGTH = 4
YOUNG = 4000
POISSON = 0.2
CEMENT_SHEAR = 2


# ------------------------------ Content in Lecture 21 ------------------------------ #
def get_I_local(b,h):
	return b*h**3/12


def get_A_local(b,h):
	return b*h


def get_y_global(y_local,A_local):
	'''
	INPUT:
	y_local - a list of vertical distances from local centroid to base
		i.e. [y1, y2, y3]
		units in mm

	A_local - a list of areas of individual shapes
		i.e. [A1, A2, A3]
		units in mm^2

	OUTPUT:
	y_global - a float of the vertical distance from global centroidal axis to base
		i.e. 10.88
		units in mm
	'''

	if len(y_local) != len(A_local): # check if y_local and a_local have the same length
		print("Error: unequal dimensions")
		return None

	sum_y_local_A_local = 0 # numerator of y_global formula

	for i in range(len(y_local)):
		sum_y_local_A_local += y_local[i] * A_local[i]

	y_global = sum_y_local_A_local / sum(A_local) # y_global formula
	return y_global

def get_I_global(I_local, A_local, y_local, y_global):
	'''
	INPUT:
	I_local - a list of second moments of area of individual shapes
		i.e. [I1, I2, I3]
		units in mm^4

	y_local - a list of vertical distances from local centroid to base
		i.e. [y1, y2, y3]
		units in mm

	A_local - a list of areas of individual shapes
		i.e. [A1, A2, A3]
		units in mm^2

	y_global - a float of the vertical distance from global centroidal axis to base
		i.e. 10.88
		units in mm

	OUTPUT:
	I_global - a float of the global second moment of area
		i.e. 10.88
		units in mm
	'''
	if not ( len(I_local) == len(A_local) == len(y_local) ): # check if I_local, y_local, and A_local have the same length
		print("Error: unequal dimensions")
		return None
	I_global = 0
	for i in range(len(y_local)):
		I_global += I_local[i] + A_local[i] * (y_local[i]-y_global)**2 # I_global formula
	return I_global





# ------------------------------ Content in Lecture 21 ------------------------------ #

def get_plate_buckling_stress(t, b, k):
	
	return (k * math.pi**2 * YOUNG) / (12 * (1 - POISSON**2)) * (t/b)**2 # plate buckling stress equation
	# unit in MPa

#print(get_plate_buckling_stress(2.54, 78.73, 4))
#print(get_plate_buckling_stress(2.54, 20, 0.425))

y_local = [0.635,37.5,73.095,74.365,37.5,74.365]
A_local = [get_A_local(80,1.27),get_A_local(1.27,72.46),get_A_local(10,1.27),get_A_local(100,1.27),get_A_local(1.27,72.46),get_A_local(10,1.27)]
#y_global = get_y_global(y_local,A_local)
#print(y_global)

'''
Shape dimensions provided by Albert
y_global = 41.70
I_local = [get_I_local(80,1.27),get_I_local(2.54,71.19),get_I_local(22.54,1.27),get_I_local(100,1.27)]
A_local = [get_A_local(80,1.27),get_A_local(2.54,71.19),get_A_local(22.54,1.27),get_A_local(100,1.27)]
y_local = [0.635,36.865,73.095,74.265]
print(get_I_global(I_local, A_local, y_local, y_global))
'''


#Shape dimensions provided by Abdullah
y_global = 41.70
I_local = [get_I_local(80,1.27),get_I_local(1.27,72.46),get_I_local(1.27,72.46),get_I_local(10,1.27),get_I_local(10,1.27),get_I_local(100,1.27)]
A_local = [get_A_local(80,1.27),get_A_local(1.27,72.46),get_A_local(1.27,72.46),get_A_local(10,1.27),get_A_local(10,1.27),get_A_local(100,1.27)]
y_local = [0.635, 37.5, 37.5, 73.095, 73.095, 74.365]
I_global = get_I_global(I_local, A_local, y_local, y_global)



# ------------------------------ Content in Lecture 21 ------------------------------ #

def get_d_local(y_local, y_global):
	return abs(y_local-y_global)


def get_Q(A_local,d_local):
	'''
	INPUT:
	A_local - a list of areas of individual shapes
		i.e. [A1, A2, A3]
		units in mm^2

	d_local - a list of vertical distances from local centroid to base
		i.e. [y1, y2, y3]
		units in mm

	OUTPUT:
	Q - a float of the first moment of area
		i.e. 10.88
		units in mm^3
	'''
	if len(A_local) != len(d_local): # check if y_local and a_local have the same length
		print("Error: unequal dimensions")
		return None

	Q = 0 # numerator of Q formula

	for i in range(len(A_local)):
		Q += A_local[i] * d_local[i]

	return Q

def get_shear_force(Q, I, b):
	return I*b*SHEAR_STRENGTH/Q

y_global = 41.70
A_local = [get_A_local(1.27,41.7),get_A_local(1.27,41.7),get_A_local(1.27,77.46)]
d_local = [get_d_local(41.7/2, y_global),get_d_local(41.7/2, y_global),get_d_local(0.635, y_global)]
Q = get_Q(A_local,d_local)
print(Q)

print(get_shear_force(Q, I_global, 2.54))








# ------------------------------ LICENSE ------------------------------ #
'''
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''