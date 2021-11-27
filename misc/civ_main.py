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

DIM = [813,1016,1.27]
T_STRENGTH = 30
C_STRENGTH = 6
SHEAR_STRENGTH = 4
YOUNG = 4000
POISSON = 0.2
CEMENT_SHEAR = 2


# ------------------------------ Design 0 CROSS SECTION PROPERTIES ------------------------------ #


# ------------------------------ Design 0 - y_global ------------------------------ #


# [top_horizontal, bottom_horizontal, left_vertical, right_vertical, left_glue, right_glue]
y_local = [74.365,0.635,37.5,37.5,73.095,73.095]
A_local = [csp.get_A_local(100,1.27),csp.get_A_local(80,1.27),csp.get_A_local(1.27,72.46),csp.get_A_local(1.27,72.46),csp.get_A_local(10,1.27),csp.get_A_local(10,1.27)]
y_global = csp.get_y_global(y_local, A_local)
print("Global centroidal axis at: %g (mm) above base" % y_global)


# ------------------------------ Design 0 - I_global ------------------------------ #


I_local = [csp.get_I_local(100,1.27),csp.get_I_local(80,1.27),csp.get_I_local(1.27,72.46),csp.get_I_local(1.27,72.46),csp.get_I_local(10,1.27),csp.get_I_local(10,1.27)]
I_global = csp.get_I_global(I_local, A_local, y_local, y_global)
print("Second moment of area is: %g (mm^4)" % I_global)


# ------------------------------ Design 0 - Q at the centroidal axis ------------------------------ #

y_local_Q = [1.27/2,(y_global-1.27)/2+1.27,(y_global-1.27)/2+1.27]
A_local_Q = [csp.get_A_local(80,1.27),csp.get_A_local(y_global-1.27,1.27),csp.get_A_local(y_global-1.27,1.27)]
Q_cent = csp.get_Q(A_local_Q,y_local_Q,y_global)
print("First moment of area at the centroidal axis is: %g (mm^3)" % Q_cent)

# ------------------------------ Design 0 - Q at the glue surface ------------------------------ #

y_local_Q_glue = [75-1.27/2]
A_local_Q_glue = [csp.get_A_local(100,1.27)]
Q_glue = csp.get_Q(A_local_Q_glue,y_local_Q_glue,y_global)
print("First moment of area at the glue surface is: %g (mm^3)" % Q_glue)

shear_4_1 = sf.get_shear_force(Q_cent, I_global, 1.27*2, sf.get_tau_ultimate("matboard"))
print("4.1: Shear force causing matboard shear failure is: %g (N)" % shear_4_1)


shear_4_2 = sf.get_shear_force(Q_glue, I_global, 11.27*2, sf.get_tau_ultimate("glue"))
print("4.2: Shear force causing glue shear failure is: %g (N)" % shear_4_2)

tau_critical_sec1 = sf.get_tau_critical(1.27, 73.73, 550)
shear_4_3a = sf.get_shear_force(Q_cent, I_global, 1.27*2, tau_critical_sec1)
print("4.3a: Shear force causing matboard shear buckling failure is: %g (N)" % shear_4_3a)

tau_critical_sec2 = sf.get_tau_critical(1.27, 73.73, 510)
shear_4_3b = sf.get_shear_force(Q_cent, I_global, 1.27*2, tau_critical_sec2)
print("4.3b: Shear force causing matboard shear buckling failure is: %g (N)" % shear_4_3b)


tau_critical_sec3 = sf.get_tau_critical(1.27, 73.73, 190)
shear_4_3c = sf.get_shear_force(Q_cent, I_global, 1.27*2, tau_critical_sec3)
print("4.3c: Shear force causing matboard shear buckling failure is: %g (N)" % shear_4_3c)

shear_4_3 = min(shear_4_3a,shear_4_3b,shear_4_3c)
print("4.3 Conclusion: Shear force causing matboard shear buckling failure is: %g (N)" % shear_4_3)



moment_4_4a = bm.get_bending_moment(y_global, I_global, bm.get_sigma_ultimate("tension"), "concave up")
print("4.4a: Bending moment causing matboard tension failure is: %g (N*mm)" % moment_4_4a)
moment_4_4b = bm.get_bending_moment(y_global, I_global, bm.get_sigma_ultimate("tension"), "concave down")
print("4.4b: Bending moment causing matboard tension failure is: %g (N*mm)" % moment_4_4b)
moment_4_4 = min(moment_4_4a,moment_4_4b)
print("4.4 Conclusion: Bending moment causing matboard tension failure is: %g (N*mm)" % moment_4_4)


moment_4_5a = bm.get_bending_moment(y_global, I_global, bm.get_sigma_ultimate("compression"), "concave up")
print("4.5a: Bending moment causing matboard compression failure is: %g (N*mm)" % moment_4_5a)
moment_4_5b = bm.get_bending_moment(y_global, I_global, bm.get_sigma_ultimate("compression"), "concave down")
print("4.5b: Bending moment causing matboard compression failure is: %g (N*mm)" % moment_4_5b)

moment_4_5 = max(moment_4_5a,moment_4_5b)
print("4.5 Conclusion: Bending moment causing matboard tension failure is: %g (N*mm)" % moment_4_5)



sigma_critical_1 = -1* bm.get_sigma_critical(0.425, 1.27, 10)
moment_4_6a = bm.get_bending_moment(y_global, I_global, sigma_critical_1, "concave up")
print("4.6a: Bending moment causing matboard flexural buckling failure is: %g (N*mm)" % moment_4_6a)

sigma_critical_2 = -1* bm.get_sigma_critical(4, 1.27, 77.46)
moment_4_6b = bm.get_bending_moment(y_global, I_global, sigma_critical_2, "concave up")
print("4.6b: Bending moment causing matboard flexural buckling failure is: %g (N*mm)" % moment_4_6b)

sigma_critical_3 = -1* bm.get_sigma_critical(6, 1.27, 32.028)
moment_4_6c = bm.get_bending_moment(y_global, I_global, sigma_critical_3, "concave up")
print("4.6c: Bending moment causing matboard flexural buckling failure is: %g (N*mm)" % moment_4_6c)

sigma_critical_4 = -1* bm.get_sigma_critical(6, 1.27, 40.43)
moment_4_6d = bm.get_bending_moment(y_global, I_global, sigma_critical_4, "concave down")
print("4.6d: Bending moment causing matboard flexural buckling failure is: %g (N*mm)" % moment_4_6d)

sigma_critical_5 = -1* bm.get_sigma_critical(4, 1.27, 77.46)
moment_4_6e = bm.get_bending_moment(y_global, I_global, sigma_critical_5, "concave down")
print("4.6e: Bending moment causing matboard flexural buckling failure is: %g (N*mm)" % moment_4_6e)

moment_4_6 = max(moment_4_6a,moment_4_6b,moment_4_6c,moment_4_6d,moment_4_6e)
print("4.6 Conclusion: Bending moment causing matboard tension failure is: %g (N*mm)" % moment_4_6)

'''
point_loads = dg.reset_loads()
dg.add_point_load(point_loads, 550, 185)
dg.add_point_load(point_loads, 1250, 185)
reaction_forces = dg.get_reaction_forces(point_loads)
#sfd = dg.generate_sfd(point_loads, reaction_forces)
sfd_with_material_shear = dg.generate_sfd_with_material_shear(point_loads, reaction_forces, shear_4_1)
#bmd = dg.generate_bmd(sfd)
#print(bmd)
'''
point_loads = dg.reset_loads()
dg.add_point_load(point_loads, 102, 200/3)
dg.add_point_load(point_loads, 278, 200/3)
dg.add_point_load(point_loads, 442, 200/3)
dg.add_point_load(point_loads, 618, 200/3)
dg.add_point_load(point_loads, 782, 200/3)
dg.add_point_load(point_loads, 958, 200/3)

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
for i in bmd:
    plt.plot(*zip(*i))
	
   

    #plt.ylim(-200,200)
plt.show()
plt.show()
'''point_loads = dg.reset_loads()
dg.add_point_load(point_loads, 342, 200/3)
dg.add_point_load(point_loads, 518, 200/3)
dg.add_point_load(point_loads, 682, 200/3)
dg.add_point_load(point_loads, 858, 200/3)
dg.add_point_load(point_loads, 1022, 200/3)
dg.add_point_load(point_loads, 1198, 200/3)
'''
reaction_forces = dg.get_reaction_forces(point_loads)
sfd = dg.generate_sfd(point_loads, reaction_forces)
bmd = dg.generate_bmd(sfd)
