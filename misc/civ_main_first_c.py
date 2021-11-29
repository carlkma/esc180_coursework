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

import civ_shear_force as sf
import civ_bending_moment as bm
import civ_cross_section_properties as csp
import civ_diagrams as dg
import civ_midspan_deflection as msd


# ------------------------------ CONSTANTS: Material Property ------------------------------ #


T_STRENGTH = 30
C_STRENGTH = 6
SHEAR_STRENGTH = 4
YOUNG = 4000
POISSON = 0.2
CEMENT_SHEAR = 2


# ------------------------------ Design A - PRIMARY INPUTS ------------------------------ #


# CHANGE THIS FOR DIFFERENT DESIGNS
y_local = [36.23,36.23,71.825, 71.825, 75.635, 66.297]
# CHANGE THIS FOR DIFFERENT DESIGNS
b_h_dim = [(1.27,72.46),(1.27,72.46), (10,1.27), (10,1.27), (100,6.35), (77.46,1.27)]
# CHANGE THIS FOR DIFFERENT DESIGNS
bm.set_height(78.81)


# ------------------------------ Design A - y_global ------------------------------ #


A_local = []
for shape in b_h_dim:
	A_local.append(csp.get_A_local(shape[0],shape[1]))

y_global = csp.get_y_global(y_local, A_local)
print("Global centroidal axis at: %g (mm) above base" % y_global)


# ------------------------------ Design A - I_global ------------------------------ #


I_local = []
for shape in b_h_dim:
	I_local.append(csp.get_I_local(shape[0],shape[1]))


I_global = csp.get_I_global(I_local, A_local, y_local, y_global)
print("Second moment of area is: %g (mm^4)" % I_global)



# ------------------------------ Design A - SECONDARY INPUTS ------------------------------ #

# CHANGE THIS FOR DIFFERENT DESIGNS

y_local_Q = [33.43,33.43, 66.297]

A_local_Q = [csp.get_A_local(1.27,66.87),csp.get_A_local(1.27,66.87),csp.get_A_local(77.46,1.27)]

y_local_Q_glue = [75-1.27/2]

A_local_Q_glue = [csp.get_A_local(100,1.27)]

# ------------------------------ Design A - Q at the centroidal axis ------------------------------ #


Q_cent = csp.get_Q(A_local_Q,y_local_Q,y_global)

print("First moment of area at the centroidal axis is: %g (mm^3)" % Q_cent)


# ------------------------------ Design A - Q at the glue surface ------------------------------ #


Q_glue = csp.get_Q(A_local_Q_glue,y_local_Q_glue,y_global)
print("First moment of area at the glue surface is: %g (mm^3)" % Q_glue)


# ------------------------------ Design A - 4.1 ------------------------------ #
print()
# get_shear_force(Q, I, b, tau)
shear_4_1 = [sf.get_shear_force(Q_cent, I_global, 1.27*2, sf.get_tau_ultimate("matboard"))]
print("4.1: Shear force causing matboard shear failure is: %g (N)" % shear_4_1[0])
print()


# ------------------------------ Design A - 4.2 ------------------------------ #
print()
shear_4_2 = [sf.get_shear_force(Q_glue, I_global, 11.27*2, sf.get_tau_ultimate("glue"))]
print("4.2: Shear force causing glue shear failure is: %g (N)" % shear_4_2[0])
print()


# ------------------------------ Design A - 4.3 ------------------------------ #
print()
input_t = 1.27
input_h = 73.73
spacing_vertical_stiffeners = [550,510,190]

shear_4_3 = []

for input_a in spacing_vertical_stiffeners:
	# get_tau_critical(t, h, a)
	tau_critical = sf.get_tau_critical(input_t, input_h, input_a)
	shear_4_3_temp = sf.get_shear_force(Q_cent, I_global, 1.27*2, tau_critical)
	shear_4_3.append(shear_4_3_temp)
	print("4.3 Step %i: Shear force causing matboard shear buckling failure is: %g (N)" % (shear_4_3.index(shear_4_3_temp),shear_4_3_temp))

print("4.3 Conclusion: Shear force causing matboard shear buckling failure is: %g (N)" % min(shear_4_3))
print()


# ------------------------------ Design A - 4.4 ------------------------------ #
print()
moment_4_4 = [] 
for region in ["concave up", "concave down"]:
	moment_4_4_temp = bm.get_bending_moment(y_global, I_global, bm.get_sigma_ultimate("tension"), region)
	moment_4_4.append(moment_4_4_temp)
	print("4.4 Step %i: Bending moment causing matboard tension failure is: %g (N*mm)" % (moment_4_4.index(moment_4_4_temp),moment_4_4_temp))

print("4.4 Conclusion: Bending moment causing matboard tension failure is: %g (N*mm)" % min(moment_4_4))
print()


# ------------------------------ Design A - 4.5 ------------------------------ #

print()
moment_4_5 = [] 
for region in ["concave up", "concave down"]:
	moment_4_5_temp = bm.get_bending_moment(y_global, I_global, bm.get_sigma_ultimate("compression"), region)
	moment_4_5.append(moment_4_5_temp)
	print("4.5 Step %i: Bending moment causing matboard compression failure is: %g (N*mm)" % (moment_4_5.index(moment_4_5_temp),moment_4_5_temp))

print("4.5 Conclusion: Bending moment causing matboard compression failure is: %g (N*mm)" % min(moment_4_5))
print()

# ------------------------------ Design A - 4.6 ------------------------------ #
print()
sigma_critical_1 = -1* bm.get_sigma_critical(0.425, 6.35, 1.27)
moment_4_6a = bm.get_bending_moment(y_global, I_global, sigma_critical_1, "concave up")
print("4.6a: Bending moment causing matboard flexural buckling failure is: %g (N*mm)" % moment_4_6a)

sigma_critical_2 = -1* bm.get_sigma_critical(4, 6.35, 94.92)
moment_4_6b = bm.get_bending_moment(y_global, I_global, sigma_critical_2, "concave up")
print("4.6b: Bending moment causing matboard flexural buckling failure is: %g (N*mm)" % moment_4_6b)

sigma_critical_3 = -1* bm.get_sigma_critical(6, 1.27, 5.59)
moment_4_6c = bm.get_bending_moment(y_global, I_global, sigma_critical_3, "concave up")
print("4.6c: Bending moment causing matboard flexural buckling failure is: %g (N*mm)" % moment_4_6c)

sigma_critical_4 = -1* bm.get_sigma_critical(6, 1.27, 40.43)
moment_4_6d = bm.get_bending_moment(y_global, I_global, sigma_critical_4, "concave down")
print("4.6d: Bending moment causing matboard flexural buckling failure is: %g (N*mm)" % moment_4_6d)

sigma_critical_5 = -1* bm.get_sigma_critical(4, 1.27, 77.46)
moment_4_6e = bm.get_bending_moment(y_global, I_global, sigma_critical_5, "concave down")
print("4.6e: Bending moment causing matboard flexural buckling failure is: %g (N*mm)" % moment_4_6e)

moment_4_6 = [moment_4_6a,moment_4_6b,moment_4_6c,moment_4_6d,moment_4_6e]
print("4.6 Conclusion: Bending moment causing matboard tension failure is: %g (N*mm)" % max(moment_4_6))
print()


# ------------------------------ Design A - PLOT ------------------------------ #
# ------------------------------ Design A - PLOT ------------------------------ #
# ------------------------------ Design A - PLOT ------------------------------ #


'''
# Point Load
point_loads = dg.reset_loads()
dg.add_point_load(point_loads, 550, 185)
dg.add_point_load(point_loads, 1250, 185)
'''


'''
# Train Case 1
point_loads = dg.reset_loads()
dg.add_point_load(point_loads, 102, 200/3)
dg.add_point_load(point_loads, 278, 200/3)
dg.add_point_load(point_loads, 442, 200/3)
dg.add_point_load(point_loads, 618, 200/3)
dg.add_point_load(point_loads, 782, 200/3)
dg.add_point_load(point_loads, 958, 200/3)
'''


# Train Case 2
point_loads = dg.reset_loads()
dg.add_point_load(point_loads, 342, 200/3)
dg.add_point_load(point_loads, 518, 200/3)
dg.add_point_load(point_loads, 682, 200/3)
dg.add_point_load(point_loads, 858, 200/3)
dg.add_point_load(point_loads, 1022, 200/3)
dg.add_point_load(point_loads, 1198, 200/3)




reaction_forces = dg.get_reaction_forces(point_loads)
sfd = dg.generate_sfd(point_loads, reaction_forces)
bmd = dg.generate_bmd(sfd)

dg.plot_all(sfd, bmd, spacing_vertical_stiffeners, shear_4_1, shear_4_2, shear_4_3, moment_4_4, moment_4_5, moment_4_6)




'''
# Train Case Variable

sfd = []
bmd = []
for i in range(0, 1250, 25):
	point_loads = dg.reset_loads()
	if i <= 1250:
		dg.add_point_load(point_loads, i, 200/3)
	if i+176 <= 1250:
		dg.add_point_load(point_loads, i+176, 200/3)
	if i+340 <= 1250:
		dg.add_point_load(point_loads, i+340, 200/3)
	if i+516 <= 1250:
		dg.add_point_load(point_loads, i+516, 200/3)
	if i+680 <= 1250:
		dg.add_point_load(point_loads, i+680, 200/3)
	if i+856 <= 1250:
		dg.add_point_load(point_loads, i+856, 200/3)
		
	reaction_forces = dg.get_reaction_forces(point_loads)
	sfd.append(dg.generate_sfd(point_loads, reaction_forces))
	for i in sfd:
		bmd.append(dg.generate_bmd(i))
	
plt.subplot(1, 2, 1)
plt.title("SFD")
plt.xlabel("Distance from Left Support (mm)")
plt.ylabel("Shear Force (N)")
ax = plt.gca()
ax.grid(True)
plt.axhline(y=0, c="black")
plt.xlim(0,1300)
for i in sfd:
    plt.plot(*zip(*i))

plt.subplot(1, 2, 2)
plt.title("BMD")
plt.xlabel("Distance from Left Support (mm)")
plt.ylabel("Bending Moment (Nmm)")
ax = plt.gca()
ax.grid(True)
ax.invert_yaxis()
plt.axhline(y=0, c="black")
plt.xlim(0,1300)
for i in bmd:
    plt.plot(*zip(*i))
	
plt.show()

'''