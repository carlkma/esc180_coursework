# civ_midspan_deflection.py
# CIV102 Bridge Project

# Fall 2021
# Group 403
# Group Members:
#  - Carl Ma
#  - Abdullah Fawzy
#  - Albert Zhang


# ------------------------------ IMPORT MODULES ------------------------------ #

import math
import numpy as np

# ------------------------------ CONSTANTS: Material Property ------------------------------ #

DIM = [813,1016,1.27]
T_STRENGTH = 30
C_STRENGTH = 6
SHEAR_STRENGTH = 4
YOUNG = 4000
POISSON = 0.2
CEMENT_SHEAR = 2

LENGTH = 1250

# ------------------------------ 4.1-4.3 Shear force ------------------------------ #
# 4.1 Shear force causing matboard shear failure
# 4.2 Shear force causing glue shear failure
# 4.3 Shear force causing matboard shear buckling failure

def bmd_to_curvature(bmd, E, I):
	x_cord, y_cord = zip(*bmd)
	x_cord_curvature = list(x_cord)
	y_cord_curvature = list(y_cord)

	for i in range(len(y_cord_curvature)):
		y_cord_curvature[i] /= (E*I)

	return x_cord_curvature, y_cord_curvature


def get_tangential_deviation_right(x_cord_curvature, y_cord_curvature):
	return np.trapz(y_cord,x_cord)


def get_tangential_deviation_mid(x_cord_curvature, y_cord_curvature):

	new_x_cord = [0]
	new_y_cord = [0]

	for i in range(1, len(x_cord)):
		start = x_cord[i-1]
		end = x_cord[i]
		if start < LENGTH/2 and end >= LENGTH/2:
			break_x = LENGTH/2
			slope = (y_cord[i] - y_cord[i-1]) / (end - start)
			constant = y_cord[i] - slope * end
			break_y = slope * break_x + constant
			new_x_cord.append(break_x)
			new_y_cord.append(break_y)
			break

		new_x_cord.append(x_cord[i])
		new_y_cord.append(y_cord[i])

	return np.trapz(new_y_cord,new_x_cord)

def get_midspan_deflection(delta_right, delta_mid):
	return delta_right * 0.5 - delta_mid


# Sample Call
# 1.374
