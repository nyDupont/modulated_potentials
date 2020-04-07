from numpy import linspace
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from utils.energy_minimization import *

bool_latex_style = 1  # for the plot to be edited in latex serif
bool_titre = 1  # to display a figure title with parameters
# bool_puits_nper = 0  # to be fixed

minimization_method = 'nelder-mead'

# parameters for the minimization algorithm
# g, eps, phi = 0.3, 0.6, 2  # initial guess
g, eps, phi = 0.7, 0.2, 2.5
# fixed parameters
a, dphi = 1, pi/2

# time vector
nper, ndt = 1, 200
vect_t = linspace(0, nper*2*pi, nper*ndt)


# mechanical energy minimization # (see utils.utils.py)
# doc : https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
param_i = array([g, eps, phi])  # packing initial parameters for minimization
res = minimize(mechanical_energy_pendulum_amp_phase_mod_adim, param_i, args=(vect_t, a, dphi), method=minimization_method,
               options={'xtol': 1e-8, 'disp': True})  # computing the minimizatoin
g_res, eps_res, phi_res = res.x  # un packing results parameters
print(list(res.x))

# solving the system with obtained parameters
x, p = resolution(pendulum_amp_phase_mod_adim, (0, 0), vect_t, res.x, a=a, dphi=dphi)  # rk4 solving
E = hamiltonian_amp_phase_mod_adim((x, p), vect_t, res.x)  # computing mechanical along the resulting trajectory

E_0 = E[0]
DE = [energy-E_0 for energy in E]  # value of interest : increase of the mechanical energy during simulation

delta_x = x[-1] - x[0]  # final position minus initial position
delta_p = p[-1] - p[0]  # final momentum minus initial momentum
delta_E = E[-1] - E[0]  # final energy minus initial energy

# CREATION D'UN FICHIER TXT ET ECRITURE DES RESULTATS #
# save_energy_minimization_as_txt(param_i, res.x, delta_x, delta_p, delta_E)

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
plt.plot(vect_t, x)
plt.xlabel('t')
plt.ylabel('x')

axes2 = fig.add_subplot(132)
plt.plot(x, p)
plt.xlabel('x')
plt.ylabel('p')

axes3 = fig.add_subplot(133)
plt.plot(vect_t, DE)
plt.xlabel('t')
plt.ylabel('Energie')
if bool_titre:
    g_res_arrondi, eps_res_arrondi, phi_res_arrondi = int(100*g_res)/100, int(100*eps_res)/100, int(100*phi_res)/100
    plt.suptitle(r"$a$ = {} ; n_per = {}".format(a, nper)
                 + "\n" + r"$\gamma$ = {} ; $\epsilon$ = {} ; $\phi$ = {}"
                 .format(g_res_arrondi, eps_res_arrondi, phi_res_arrondi))

# save_energy_minimization_as_png(g_res_arrondi, eps_res_arrondi, phi_res_arrondi)
plt.show()
