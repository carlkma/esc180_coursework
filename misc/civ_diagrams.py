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
import math

# ------------------------------ CONSTANTS: Structure Property ------------------------------ #


D_TO_RIGHT_SUPPORT = 550+510
# ------------------------------ Content in Lecture 21 ------------------------------ #
point_loads = []

def reset_loads():
	global point_loads
	point_loads = []

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


add_point_load(point_loads, 550, 185)
add_point_load(point_loads, 1250, 185)
reaction_forces = get_reaction_forces(point_loads)


def generate_sfd(point_loads):
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
	plt.xlim(0,1300)
	plt.ylim(-200,200)
	plt.show()
	return sfd

sfd = generate_sfd(point_loads)

def generate_bmd(sfd):
	bmd = [(0,0)]
	for i in range(1, len(sfd)):
		start = sfd[i-1]
		end = sfd[i]
		if start[1] == end[1]:
			bmd.append((end[0],bmd[-1][1]+(end[0]-start[0])*end[1]))
	plt.plot(*zip(*bmd))
	plt.title("BMD")
	plt.xlabel("Distance from Left Support (mm)")
	plt.ylabel("Bending Moment (Nmm)")
	ax = plt.gca()
	ax.grid(True)
	ax.invert_yaxis()
	plt.axhline(y=0, c="black")
	plt.show()
	return bmd

bmd = generate_bmd(sfd)



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