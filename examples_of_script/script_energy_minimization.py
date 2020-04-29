from numpy import linspace, pi, array
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from utils.energy_minimization import *
from utils.utils import *

bool_latex_style = 1  # for the plot to be edited in latex serif
bool_title = 1  # to display a figure title with parameters
# bool_puits_nper = 0  # to be fixed

minimization_method = 'nelder-mead'

# parameters for the minimization algorithm
# g, eps, phi = 0.3, 0.6, 2  # initial guess
g, eps, phi = 1, 0.4, 4
# fixed parameters
a, dphi = 1, pi/2

# time vector
nper, ndt = 1, 500
t0 = 0
vect_t = linspace(t0, t0 + nper*2*pi, nper*ndt)


# mechanical energy minimization # (see utils.utils.py)
# doc : https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
param_i = array([g, eps, phi])  # packing initial parameters for minimization
res = minimize(mechanical_energy_pendulum_amp_phase_mod_adim, param_i, args=(vect_t, a, dphi),
               method=minimization_method, options={'xtol': 1e-8, 'disp': True})  # computing the minimizatoin
g_res, eps_res, phi_res, = res.x  # un packing results parameters
print(list(res.x))

# solving the system with obtained parameters
x, p = resolution(pendulum_amp_phase_mod_adim, (0, 0), vect_t, (g_res, eps_res, phi_res, a, dphi))  # rk4 solving
E = hamiltonian_amp_phase_mod_adim((x, p), vect_t, (g_res, eps_res, phi_res, a, dphi))  # computing mechanical along the
# resulting trajectory

E_0 = E[0]
DE = [energy-E_0 for energy in E]  # value of interest : increase of the mechanical energy during simulation

delta_x = x[-1] - x[0]  # final position minus initial position
delta_p = p[-1] - p[0]  # final momentum minus initial momentum
delta_E = E[-1] - E[0]  # final energy minus initial energy

# CREATION D'UN FICHIER TXT ET ECRITURE DES RESULTATS #
# save_energy_minimization_as_txt(param_i, res.x, delta_x, delta_p, delta_E)

# GRAPHES #
fig = plt.figure(1, figsize=(9, 4))
if bool_title:
    plt.subplots_adjust(top=0.81, wspace=0.37)
else:
    plt.subplots_adjust(left=.07, bottom=.14, right=0.96, top=0.9, wspace=0.4)

if bool_latex_style:
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.sans-serif'] = 'Computer Modern'

axes1 = fig.add_subplot(131)
plt.plot(vect_t, x)
plt.xlabel('t')
plt.ylabel('x')
left, right = plt.xlim()
bottom, top = plt.ylim()
w, h = right-left, top-bottom
plt.text(left+0.05*w, top-0.1*h, 'a', horizontalalignment='left', verticalalignment='baseline', weight='bold')
plt.grid()

axes2 = fig.add_subplot(132)
plt.plot(x, p)
plt.xlabel('x')
plt.ylabel('p')
left, right = plt.xlim()
bottom, top = plt.ylim()
w, h = right-left, top-bottom
plt.text(left+0.05*w, top-0.1*h, 'b', horizontalalignment='left', verticalalignment='baseline', weight='bold')
plt.grid()

axes3 = fig.add_subplot(133)
plt.plot(vect_t, DE)
plt.xlabel('t')
plt.ylabel('mechanical energy')
left, right = plt.xlim()
bottom, top = plt.ylim()
w, h = right-left, top-bottom
plt.text(left+0.05*w, top-0.1*h, 'c', horizontalalignment='left', verticalalignment='baseline', weight='bold')
plt.grid()


if bool_title:
    str_dphi = str(int(10*dphi/pi)/10) + r'\pi'
    g_rounded, eps_rounded, phi_rounded = round(1000*g_res)/1000, round(1000*eps_res)/1000, round(1000*phi_res)/1000
    plt.suptitle(r"$n_{per}$" + r" = {} ; $a$ = {} ; $\Delta \phi = {}$".format(nper, a, str_dphi)
                 + "\n" + r"$\gamma$ = {} ; $\epsilon$ = {} ; $\phi$ = {}"
                 .format(g_rounded, eps_rounded, phi_rounded))

# save_energy_minimization_as_png(g_res_arrondi, eps_res_arrondi, phi_res_arrondi)
plt.show()
