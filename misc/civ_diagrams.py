# civ_diagrams.py
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

# ------------------------------ CONSTANTS: Structure Property ------------------------------ #

D_TO_RIGHT_SUPPORT = 550+510

# ------------------------------ Content in Lecture 21 ------------------------------ #

point_loads = []

def reset_loads():
	global point_loads
	point_loads = []
	return point_loads

def add_point_load(point_loads, location, magnitude):
	point_loads.append((location, -1 * magnitude))
	return point_loads
	
def get_reaction_forces(point_loads):
	force = 0
	moment = 0
	for point_load in point_loads:
		moment += point_load[0] * point_load[1]
		force += point_load[1]
	right_reaction = -1 * moment / D_TO_RIGHT_SUPPORT
	left_reaction = -1 * force - right_reaction
	return left_reaction, right_reaction


def generate_sfd(point_loads, reaction_forces):
	point_loads.append((0, reaction_forces[0]))
	point_loads.append((D_TO_RIGHT_SUPPORT, reaction_forces[1]))
	
	forces = sorted(point_loads)

	sfd = [(0,0)]
	sfd.append(forces[0])
	for i in range(1, len(forces)):
		sfd.append((forces[i][0], sfd[-1][1]))
		sfd.append((forces[i][0], forces[i][1] + sfd[-1][1]))

	'''
	plt.plot(*zip(*sfd))
	plt.title("SFD")
	plt.xlabel("Distance from Left Support (mm)")
	plt.ylabel("Shear Force (N)")
	ax = plt.gca()
	ax.grid(True)
	plt.axhline(y=0, c="black")
	plt.xlim(0,1300)
	plt.ylim(-200,200)
	plt.show()
	'''
	return sfd



def generate_bmd(sfd):
	bmd = [(0,0)]
	for i in range(1, len(sfd)):
		start = sfd[i-1]
		end = sfd[i]
		if start[1] == end[1]:
			bmd.append((end[0],bmd[-1][1]+(end[0]-start[0])*end[1]))
	'''
	plt.plot(*zip(*bmd))
	plt.title("BMD")
	plt.xlabel("Distance from Left Support (mm)")
	plt.ylabel("Bending Moment (Nmm)")
	ax = plt.gca()
	ax.grid(True)
	ax.invert_yaxis()
	plt.axhline(y=0, c="black")
	plt.show()
'''
	return bmd

def generate_sfd_with_material_shear(point_loads, reaction_forces, shear_4_1):
	point_loads.append((0, reaction_forces[0]))
	point_loads.append((D_TO_RIGHT_SUPPORT, reaction_forces[1]))
	
	forces = sorted(point_loads)

	sfd = [(0,0)]
	sfd.append(forces[0])
	for i in range(1, len(forces)):
		sfd.append((forces[i][0], sfd[-1][1]))
		sfd.append((forces[i][0], forces[i][1] + sfd[-1][1]))

	
	plt.plot(*zip(*sfd))
	plt.title("SFD")
	plt.xlabel("Distance from Left Support (mm)")
	plt.ylabel("Shear Force (N)")
	ax = plt.gca()
	ax.grid(True)
	plt.axhline(y=0, c="black")
	plt.axhline(y=shear_4_1, c="red")
	plt.axhline(y=-1*shear_4_1, c="red")
	plt.xlim(0,1300)
	#plt.ylim(-200,200)
	plt.show()
	return sfd