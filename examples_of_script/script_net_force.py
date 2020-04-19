from numpy import linspace
import matplotlib.pyplot as plt
from scipy.integrate import simps
from utils.physics_systems import *

bool_title =1
bool_latex_style = 1

# system
system = pendulum_amp_phase_mod_adim

# parameters
# g, eps, phi = 0.79, 0.27, 2.7  # works for a = 1, dphi = pi/2
# a, dphi = 1, pi/2

g, eps, phi = 0.94, 0.19, 2.09  # works for a = 1, dphi = pi/2
a, dphi = 1, pi/2

# g, eps, phi = 1.03, 0.29, 2.15  # works for a = 1, dphi = pi/2
# a, dphi = 2, pi/2

# time vector
nper = 1
ndt = 1000  # plays here a special role on animation speed
tf = nper*2*pi  # dimensionless final time
vect_t = linspace(0, tf, round(nper*ndt))  # time vector

# solving the DE
x, p = resolution(pendulum_amp_phase_mod_adim, (0, 0), vect_t, (g, eps, phi, a, dphi))

# evaluating the force experienced by the particle along trajectory
f = force_pendulum_amp_phas_mod_adim(x, vect_t, (g, eps, phi, a, dphi))
f_averaged = []
for t in range(1, nper*ndt):
    T = linspace(0, vect_t[t], t)
    f_averaged.append(simps(f[:t], T)/(vect_t[t]))
f_max, f_min = max(max(f), max(f_averaged)), min(min(f), min(f_averaged))  # to scale the graph

# plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
if bool_latex_style:
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.sans-serif'] = 'Computer Modern'


fig = plt.figure(1, figsize=(9, 4))
plt.subplots_adjust(top=0.81, wspace=0.37)

axes1 = fig.add_subplot(131)
plt.plot(vect_t, x)
plt.xlabel('time')
plt.ylabel('position')
plt.xticks([pi*i/2 for i in range(4*nper+1)], ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.yticks([pi*i/2 for i in range(4*nper+1)], ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
left, right = plt.xlim()
bottom, top = plt.ylim()
w, h = right-left, top-bottom
plt.text(left+0.05*w, top-0.1*h, 'a', horizontalalignment='left', verticalalignment='baseline', weight='bold')
plt.grid()


axes2 = fig.add_subplot(132)
plt.plot(x, p)
plt.xlabel('position')
plt.xticks([pi*i/2 for i in range(4*nper+1)], ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.ylabel('momentum')
left, right = plt.xlim()
bottom, top = plt.ylim()
w, h = right-left, top-bottom
plt.text(left+0.05*w, top-0.1*h, 'b', horizontalalignment='left', verticalalignment='baseline', weight='bold')
plt.grid()


axes3 = fig.add_subplot(133)
plt.plot(vect_t, f, label=r'$F\left[x(t),t\right]$' + '\n' + r'$= -\partial_x V(x,t) |_{x=x(t)}$')
plt.plot(vect_t[1:], f_averaged, label=r'''$\frac{1}{t}\int_0^t F\left[x(t),t'\right]dt'$''')
plt.xlabel('time')
plt.xticks([pi*i/2 for i in range(4*nper+1)], ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.ylabel('force')
left, right = plt.xlim()
bottom, top = plt.ylim()
w, h = right-left, top-bottom
plt.text(left+0.05*w, top-0.1*h, 'c', horizontalalignment='left', verticalalignment='baseline', weight='bold')
plt.ylim(1.75*bottom, top)
plt.grid()
plt.legend(prop={'size': 9})

if bool_title:
    str_dphi = str(int(10*dphi/pi)/10) + r'\pi'
    g_rounded, eps_rounded, phi_rounded = round(100*g)/100, round(100*eps)/100, round(100*phi)/100
    plt.suptitle(r"$n_{per}$" + r" = {} ; $a$ = {} ; $\Delta \phi = {}$".format(a, nper, str_dphi)
                 + "\n" + r"$\gamma$ = {} ; $\epsilon$ = {} ; $\phi$ = {}"
                 .format(g_rounded, eps_rounded, phi_rounded))

plt.show()
