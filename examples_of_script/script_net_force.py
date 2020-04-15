from numpy import linspace
import matplotlib.pyplot as plt
from scipy.integrate import simps
from utils.physics_systems import *

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
param = g, eps, phi

# time vector
nper = 1
ndt = 1000  # plays here a special role on animation speed
tf = nper*2*pi  # dimensionless final time
vect_t = linspace(0, tf, round(nper*ndt))  # time vector

# solving the DE
x, p = resolution(pendulum_amp_phase_mod_adim, (0, 0), vect_t, param, a=a, dphi=dphi)
f = force_pendulum_amp_phas_mod_adim(x, vect_t, param, a=a, dphi=dphi)
f_averaged = []
for t in range(1, nper*ndt):
    T = linspace(0, vect_t[t], t)
    f_averaged.append(simps(f[:t], T)/(vect_t[t]))

# plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{nicefrac}')
if bool_latex_style:
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.sans-serif'] = 'Computer Modern'

plt.plot(vect_t, f, label=r'$F(x,t) = - \partial_x V(x,t)$')
plt.plot(vect_t[1:], f_averaged, label=r"$\frac{1}{t}\int_0^t F(x,t')dt'$")  # label=r'$\left\langle F(x,t) \right\rangle$')
plt.xlabel(r'time $t$')
plt.xticks([pi*i/2 for i in range(4*nper+1)], ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.ylabel(r'force $F$')
plt.grid()
plt.legend()
plt.show()
