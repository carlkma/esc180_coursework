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
	return sfd

def generate_bmd(sfd):
	bmd = [(0,0)]
	for i in range(1, len(sfd)):
		start = sfd[i-1]
		end = sfd[i]
		if start[1] == end[1]:
			bmd.append((end[0],bmd[-1][1]+(end[0]-start[0])*end[1]))
	return bmd

def get_bmd_x_intercept(bmd):
	all_x_int = []
	for i in range(1, len(bmd)):
		start = bmd[i-1]
		end = bmd[i]
		if start[1] * end[1] <= 0:
			slope = (end[1] - start[1]) / (end[0] - start[0])
			constant = end[1] - slope * end[0]
			one_x_int = -1*constant / slope
			if not int(one_x_int) in [x[0] for x in bmd]:
				all_x_int.append(one_x_int)
	return all_x_int

def plot_all(sfd, bmd, spacing_vertical_stiffeners, shear_4_1, shear_4_2, shear_4_3, moment_4_4, moment_4_5, moment_4_6):

	plt.subplot(2, 3, 1)


	plt.title("SFD")
	plt.xlabel("Distance from Left Support (mm)")
	plt.ylabel("Shear Force (N)")
	ax = plt.gca()
	ax.grid(True)
	plt.axhline(y=0, c="black")
	plt.xlim(0,1290)
	plt.plot(*zip(*sfd))
	#plt.savefig('1.png', bbox_inches="tight")
	#plt.show()


	plt.subplot(2, 3, 2)
	plt.title("SFD")
	plt.xlabel("Distance from Left Support (mm)")
	plt.ylabel("Shear Force (N)")
	ax = plt.gca()
	ax.grid(True)
	plt.axhline(y=0, c="black")
	plt.axhline(y=shear_4_1[0], c="red",label='4.1 Mat Shear Fail (+)')
	plt.axhline(y=-1*shear_4_1[0], c="green",label='4.1 Mat Shear Fail (-)')
	plt.xlim(0,1290)
	plt.legend(loc='best')
	plt.plot(*zip(*sfd))
	#plt.savefig('2.png', bbox_inches="tight")
	#plt.show()


	plt.subplot(2, 3, 3)
	plt.title("SFD")
	plt.xlabel("Distance from Left Support (mm)")
	plt.ylabel("Shear Force (N)")
	ax = plt.gca()
	ax.grid(True)
	plt.axhline(y=0, c="black")
	spacing_vertical_stiffeners = [0] + spacing_vertical_stiffeners
	for i in range(len(shear_4_3)):
	
		ax.vlines(x=sum(spacing_vertical_stiffeners[:i+1]),ymin=shear_4_3[i-1],ymax=shear_4_3[i],color="red") # note index problem
		l1= ax.hlines(y=shear_4_3[i], xmin=sum(spacing_vertical_stiffeners[:i+1]), xmax=sum(spacing_vertical_stiffeners[:i+2]),color="red",label='Matb Shear (T) buckling fail')
		l2 = ax.vlines(x=sum(spacing_vertical_stiffeners[:i+1]),ymin=-1*shear_4_3[i-1],ymax=-1*shear_4_3[i],color="green") # note index problem
		ax.hlines(y=-1*shear_4_3[i], xmin=sum(spacing_vertical_stiffeners[:i+1]), xmax=sum(spacing_vertical_stiffeners[:i+2]),color="green",label='Matb Shear (C) buckling fail')
	plt.xlim(0,1290)
	plt.legend([l1,l2],["Mat Shear Buckling Fail (+)", "Mat Shear Buckling Fail (-)"],loc='best')
	plt.plot(*zip(*sfd))
	#plt.savefig('3.png', bbox_inches="tight")
	#plt.show()

	plt.subplot(2, 3, 4)
	plt.title("BMD")
	plt.xlabel("Distance from Left Support (mm)")
	plt.ylabel("Bending Moment (Nmm)")
	ax = plt.gca()
	ax.grid(True)
	ax.invert_yaxis()
	plt.axhline(y=0, c="black")
	plt.xlim(0,1290)
	plt.plot(*zip(*bmd))
	#plt.savefig('4.png', bbox_inches="tight")
	#plt.show()
	x_int = get_bmd_x_intercept(bmd)
	if len(x_int) > 0:
		x_int = x_int[0]
	else:
		x_int = 1250



	plt.subplot(2, 3, 5)
	plt.title("BMD")
	plt.xlabel("Distance from Left Support (mm)")
	plt.ylabel("Bending Moment (Nmm)")
	ax = plt.gca()
	ax.grid(True)
	ax.invert_yaxis()
	plt.axhline(y=0, c="black")
	ax.hlines(y=moment_4_4[0], xmin=0, xmax=x_int, color="red")
	ax.vlines(x=x_int,ymin=min(moment_4_4[0],-1*moment_4_4[1]),ymax=max(moment_4_4[0],-1*moment_4_4[1]),color="red", label="Mat T Fail") # note index problem
	ax.hlines(y=-1*moment_4_4[1], xmin=x_int, xmax=1250,color="red")
	ax.hlines(y=-1*moment_4_5[0], xmin=0, xmax=x_int,color="green")
	ax.vlines(x=x_int,ymin=min(-1*moment_4_5[0],moment_4_5[1]),ymax=max(-1*moment_4_5[0],moment_4_5[1]),color="green", label="Mat C Fail") # note index problem
	ax.hlines(y=moment_4_5[1], xmin=x_int, xmax=1250,color="green")
	plt.xlim(0,1290)
	plt.legend(loc="best")
	plt.plot(*zip(*bmd))
	#plt.savefig('5.png', bbox_inches="tight")
	#plt.show()


	plt.subplot(2, 3, 6)
	plt.title("BMD")
	plt.xlabel("Distance from Left Support (mm)")
	plt.ylabel("Bending Moment (Nmm)")
	ax = plt.gca()
	ax.grid(True)
	ax.invert_yaxis()
	plt.axhline(y=0, c="black")
	ax.hlines(y=moment_4_6[0], xmin=0, xmax=x_int,color="yellow",label="Side Flange Buckling")
	ax.hlines(y=moment_4_6[1], xmin=0, xmax=x_int,color="green", label="Mid Flange Buckling")
	ax.hlines(y=moment_4_6[2], xmin=0, xmax=x_int,color="red", label="Web Compression Buckling")
	ax.hlines(y=moment_4_6[3], xmin=x_int, xmax=1250,color="yellow")
	ax.hlines(y=moment_4_6[4], xmin=x_int, xmax=1250,color="green")
	#ax.hlines(y=moment_4_6[5], xmin=x_int, xmax=1250,color="red")
	ax.vlines(x=x_int,ymin=min(moment_4_6),ymax=max(moment_4_6),color="red") # note index problem
	plt.xlim(0,1290)
	plt.legend(loc='best')
	plt.plot(*zip(*bmd))
	#plt.savefig('6.png', bbox_inches="tight")


	plt.show()