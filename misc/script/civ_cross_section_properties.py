# civ_cross_section_properties.py
# CIV102 Bridge Project

# Fall 2021
# Group 403
# Group Members:
#  - Carl Ma
#  - Abdullah Fawzy
#  - Albert Zhang


# ------------------------------ CONSTANTS: Material Property ------------------------------ #

T_STRENGTH = 30
C_STRENGTH = 6
SHEAR_STRENGTH = 4
YOUNG = 4000
POISSON = 0.2
CEMENT_SHEAR = 2

# ------------------------------ Area ------------------------------ #

def get_A_local(b,h):
	return b*h

# ------------------------------ Centroidal axis ------------------------------ #


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


# ------------------------------ Second moment of area ------------------------------ #


def get_I_local(b,h):
	return b*h**3/12


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


# ------------------------------ First moment of area ------------------------------ #


def get_Q(A_local,y_local, y_global):
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

	if not ( len(A_local) == len(y_local) ): # check if A_local and y_local have the same length
		print("Error: unequal dimensions")
		return None

	Q = 0

	for i in range(len(y_local)):
		Q += A_local[i] * abs(y_local[i]-y_global)

	return Q