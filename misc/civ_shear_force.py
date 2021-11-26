# civ_shear_force.py
# CIV102 Bridge Project

# Fall 2021
# Group 403
# Group Members:
#  - Carl Ma
#  - Abdullah Fawzy
#  - Albert Zhang


# ------------------------------ IMPORT MODULES ------------------------------ #

import math

# ------------------------------ CONSTANTS: Material Property ------------------------------ #

DIM = [813,1016,1.27]
T_STRENGTH = 30
C_STRENGTH = 6
SHEAR_STRENGTH = 4
YOUNG = 4000
POISSON = 0.2
CEMENT_SHEAR = 2

# ------------------------------ 4.1-4.3 Shear force ------------------------------ #
# 4.1 Shear force causing matboard shear failure
# 4.2 Shear force causing glue shear failure
# 4.3 Shear force causing matboard shear buckling failure

def get_shear_force(Q, I, b, tau):
	return I*b*tau/Q

def get_tau_ultimate(material):
	if material == "matboard":
		return SHEAR_STRENGTH
	if material == "glue":
		return CEMENT_SHEAR

def get_tau_critical(t, h, a):
	return 5 * (math.pi)**2 * YOUNG / 12 / (1-POISSON**2) * ((t/h)**2+(t/a)**2)