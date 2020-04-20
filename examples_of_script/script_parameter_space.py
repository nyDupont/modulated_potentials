from numpy import zeros, pi, linspace
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from utils.physics_systems import *
from utils.utils import *

system = pendulum_amp_phase_mod_adim

epsilon_initial, epsilon_final, nbre_epsilon = 0, 1, 15
phi_initial, phi_final, nbre_phi = 0, 2*pi, 15
g = 0.5
a, dphi = 1, pi/2

# time vector
nper, ndt = 2, 200
t0 = 0
vect_t = linspace(t0, t0 + nper*2*pi, nper*ndt)

freq_xticks, freq_yticks = 4, 4
bool_title = 1

vect_epsilon = linspace(epsilon_initial, epsilon_final, nbre_epsilon)
vect_phi = linspace(phi_initial, phi_final, nbre_phi)

tableau_resultat = zeros((nbre_epsilon, nbre_phi))

i = 0
for e in vect_epsilon:
    j = 0
    for p in vect_phi:
        x_sol, p_sol = resolution(system, (0, 0), vect_t, (g, e, p, a, dphi))

        tableau_resultat[i, j] = x_sol[-1]
        j += 1
    i += 1
    print(str(int(i/nbre_epsilon*100)) + '%')

# GRAPHES #
plt.figure(1, figsize=(5, 5))
# plt.subplots_adjust(top=0.81, wspace=0.4)

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.sans-serif'] = 'Computer Modern'

ax = plt.gca()
plt.imshow(tableau_resultat, origin='lower')

str_dphi = str(int(10*dphi/pi)/10) + r'\pi'
if bool_title: plt.title(r'${}$'.format(str_dphi), size=15)
plt.xlabel(r'$\epsilon$', size=15)
plt.xticks(range(0, nbre_epsilon, freq_xticks), [str(int(10*i)/10) for i in vect_epsilon][::freq_xticks])
plt.ylabel(r'$\varphi$', size=15)
plt.yticks(range(0, nbre_phi, freq_yticks), [str(int(10*j)/10) for j in vect_phi][::freq_yticks])
# plt.annotate('a)', (0, 8), color='white', size=15)
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(cax=cax)

plt.show()
