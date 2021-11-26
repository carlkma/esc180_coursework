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
A_local = [csp.get_A_local(100,1.27),csp.get_A_local(80,1.27),csp.get_A_local(72.46,1.27),csp.get_A_local(72.46,1.27),csp.get_A_local(10,1.27),csp.get_A_local(10,1.27)]
y_global = csp.get_y_global(y_local, A_local)
print("Global centroidal axis at: %g (mm) above base" % y_global)


# ------------------------------ Design 0 - I_global ------------------------------ #


I_local = [csp.get_I_local(100,1.27),csp.get_I_local(80,1.27),csp.get_I_local(72.46,1.27),csp.get_I_local(72.46,1.27),csp.get_I_local(10,1.27),csp.get_I_local(10,1.27)]
I_global = csp.get_I_global(I_local, A_local, y_local, y_global)
print("Second moment of area is: %g (mm^4)" % I_global)


# ------------------------------ Design 0 - Q at the centroidal axis ------------------------------ #

y_local_Q = [1.27,21.4858,21.4858]
A_local_Q = [csp.get_A_local(80,1.27),csp.get_A_local(y_global-1.27,1.27),csp.get_A_local(y_global-1.27,1.27)]
Q_cent = csp.get_Q(A_local_Q,y_local_Q,y_global)
print("First moment of area at the centroidal axis is: %g (mm^3)" % Q_cent)

# ------------------------------ Design 0 - Q at the glue surface ------------------------------ #

y_local_Q_glue = [y_global-1.27/2]
A_local_Q_glue = [csp.get_A_local(100,1.27)]
Q_glue = csp.get_Q(A_local_Q_glue,y_local_Q_glue,y_global)
print("First moment of area at the glue surface is: %g (mm^3)" % Q_glue)

shear_4_1 = sf.get_shear_force(Q_cent, I_global, 1.27*2, sf.get_tau_ultimate("matboard"))
print("4.1: Shear force causing matboard shear failure is: %g (N)" % shear_4_1)


shear_4_2 = sf.get_shear_force(Q_cent, I_global, 10*2, sf.get_tau_ultimate("glue"))
print("4.2: Shear force causing glue shear failure is: %g (N)" % shear_4_2)

point_loads = dg.reset_loads()
dg.add_point_load(point_loads, 550, 185)
dg.add_point_load(point_loads, 1250, 185)
reaction_forces = dg.get_reaction_forces(point_loads)
sfd = dg.generate_sfd(point_loads, reaction_forces)
bmd = dg.generate_bmd(sfd)
print(bmd)
print(msd.get_tangential_deviation_mid(bmd, YOUNG, I_global))
print("done")