from numpy import linspace, pi
import matplotlib.pyplot as plt
from scipy.integrate import simps
from utils.physics_systems import *
from utils.utils import *

bool_latex_style = 1  # for the plot to be edited in latex serif
bool_title = 1  # to display a figure title with parameters
# bool_puits_nper = 0  # to be fixed

# system
system = pendulum_amp_phase_mod_adim

# parameters
g, eps, phi = 0.26, 0.51, 2.97
a, dphi = 1, pi/2

# initial conditions (IC)
x0, p0 = 0, 0

# time vector
t0 = 0
nper = 2
ndt = 1000
tf = nper*2*pi  # dimensionless final time
vect_t = linspace(t0, t0+tf, nper*ndt)  # time vector

# solving the DE
x, p = resolution(system, (x0, p0), vect_t, (g, eps, phi, a, dphi))
E = hamiltonian_amp_phase_mod_adim((x, p), vect_t, (g, eps, phi, a, dphi))

x_min, x_max = min(x), max(x)

E_0 = E[0]
DE = [energie-E_0 for energie in E]

# evaluating the force experienced by the particle along trajectory
f = force_pendulum_amp_phas_mod_adim(x, vect_t, (g, eps, phi, a, dphi))
f_averaged = []
for t in range(1, nper*ndt):
    T = linspace(0, vect_t[t], t)
    f_averaged.append(simps(f[:t], T)/(vect_t[t]))
f_max, f_min = max(max(f), max(f_averaged)), min(min(f), min(f_averaged))  # to scale the graph

# GRAPHES #
fig = plt.figure(1, figsize=(9, 4))
if bool_title:
    plt.subplots_adjust(left=0.05, right=0.97, top=0.84, wspace=0.43)
else:
    plt.subplots_adjust(left=.07, bottom=.14, right=0.96, top=0.9, wspace=0.4)

if bool_latex_style:
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.sans-serif'] = 'Computer Modern'

axes1 = fig.add_subplot(141)
plt.xlabel('time')
if nper == 1:
    plt.xticks([pi*i/2*nper for i in range(4+1)], ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
if nper == 2:
    plt.xticks([pi*i/2*nper for i in range(4+1)], ['0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$'])
plt.ylabel('position')
plt.yticks([pi*i/2 for i in range(4*nper+1)], ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.plot(vect_t, x)
# if bool_puits_nper:
#     for i in range(int(x_min/pi)-2, int(x_max/pi)+2):
#         plt.plot(vect_t, pi/2*(2*i+1)+phi*cos(a*vect_t)+dphi, color=[.5, .5, .5])
left, right = plt.xlim()
bottom, top = plt.ylim()
w, h = right-left, top-bottom
plt.text(left+0.05*w, top-0.1*h, 'a', horizontalalignment='left', verticalalignment='baseline', weight='bold')
plt.grid()

axes2 = fig.add_subplot(142)
plt.plot(x, p)
plt.xlabel('position')
plt.xticks([pi*i/2 for i in range(5)], ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.ylabel('momentum')
left, right = plt.xlim()
bottom, top = plt.ylim()
w, h = right-left, top-bottom
plt.text(left+0.05*w, top-0.1*h, 'b', horizontalalignment='left', verticalalignment='baseline', weight='bold')
plt.grid()

axes3 = fig.add_subplot(143)
plt.plot(vect_t, DE)
plt.xlabel('time')
if nper == 1:
    plt.xticks([pi*i/2*nper for i in range(4+1)], ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
if nper == 2:
    plt.xticks([pi*i/2*nper for i in range(4+1)], ['0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$'])
plt.ylabel('mechanical energy')
left, right = plt.xlim()
bottom, top = plt.ylim()
w, h = right-left, top-bottom
plt.text(left+0.05*w, top-0.1*h, 'c', horizontalalignment='left', verticalalignment='baseline', weight='bold')
plt.grid()

axes4 = fig.add_subplot(144)
plt.plot(vect_t, f, label=r'$F\left[x(t),t\right]$' + '\n' + r'$= -\partial_x V(x,t) |_{x=x(t)}$')
plt.plot(vect_t[1:], f_averaged, label=r'''$\frac{1}{t}\int_0^t F\left[x(t),t'\right]dt'$''')
plt.xlabel('time')
if nper == 1:
    plt.xticks([pi*i/2*nper for i in range(4+1)], ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
if nper == 2:
    plt.xticks([pi*i/2*nper for i in range(4+1)], ['0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$'])
plt.ylabel('force')
bottom, top = plt.ylim()
plt.ylim(1.75*bottom, top)
left, right = plt.xlim()
bottom, top = plt.ylim()
w, h = right-left, top-bottom
plt.text(left+0.05*w, top-0.1*h, 'd', horizontalalignment='left', verticalalignment='baseline', weight='bold')
plt.grid()
plt.legend(prop={'size': 9})

if bool_title:
    str_dphi = str(int(10*dphi/pi)/10) + r'\pi'
    g_rounded, eps_rounded, phi_rounded = round(100*g)/100, round(100*eps)/100, round(100*phi)/100
    plt.suptitle(r"$n_\mathrm{per} = $" + str(nper) + r' ; $\omega_\mathrm{amp}/\omega_\mathrm{phase}$ = ' +
                 r"{} ; $\Delta \phi = {}$".format(a, str_dphi)
                 + "\n" + r"$\gamma$ = {} ; $\epsilon$ = {} ; $\phi$ = {}"
                 .format(g_rounded, eps_rounded, phi_rounded))

plt.show()
