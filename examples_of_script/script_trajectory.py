from numpy import linspace
import matplotlib.pyplot as plt
from utils.physics_systems import *

bool_latex_style = 1  # for the plot to be edited in latex serif
bool_titre = 1  # to display a figure title with parameters
# bool_puits_nper = 0  # to be fixed

# system
system = pendulum_amp_phase_mod_adim

# parameters
g, eps, phi = 0.79, 0.27, 2.7  # works for a = 1, dphi = pi/2
a, dphi = 1, pi/2

# initial conditions (IC)
x0, p0 = 0, 0

# time vector
nper = 1
ndt = 1000
tf = nper*2*pi  # dimensionless final time
vect_t = linspace(0, tf, nper*ndt)  # time vector

# solving the DE
x_sol, p_sol = resolution(system, (x0, p0), vect_t, (g, eps, phi), a=a, dphi=dphi)
E = hamiltonian_amp_phase_mod_adim((x_sol, p_sol), vect_t, (g, eps, phi))

x_min, x_max = min(x_sol), max(x_sol)

E_0 = E[0]
DE = [energie-E_0 for energie in E]

# GRAPHES #
fig = plt.figure(1, figsize=(9, 4))
if bool_titre:
    plt.subplots_adjust(top=0.81, wspace=0.4)
else:
    plt.subplots_adjust(left=.07, bottom=.14, right=0.96, top=0.9, wspace=0.4)

if bool_latex_style:
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.sans-serif'] = 'Computer Modern'

axes1 = fig.add_subplot(131)
plt.title('a')
plt.xlabel('time')
plt.ylabel('position')

# if bool_puits_nper:
#     for i in range(int(x_min/pi)-2, int(x_max/pi)+2):
#         plt.plot(vect_t, pi/2*(2*i+1)+phi*cos(a*vect_t)+dphi, color=[.5, .5, .5])
plt.plot(vect_t, x_sol)

axes2 = fig.add_subplot(132)
plt.title('b')
plt.plot(x_sol, p_sol)
plt.xlabel('position')
plt.ylabel('momentum')

axes3 = fig.add_subplot(133)
plt.title('c')
plt.plot(vect_t, DE)
plt.xlabel('time')
plt.ylabel('mechanical energy')

if bool_titre:
    g_res_arrondi, eps_res_arrondi, phi_res_arrondi = int(100*g)/100, int(100*eps)/100, int(100*phi)/100
    plt.suptitle(r"$a$ = {} ; nper = {}".format(a, nper)
                 + "\n" + r"$\gamma$ = {} ; $\epsilon$ = {} ; $\phi$ = {}"
                 .format(g_res_arrondi, eps_res_arrondi, phi_res_arrondi))

plt.show()
