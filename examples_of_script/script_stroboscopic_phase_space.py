#%%

from numpy import pi
import matplotlib.pyplot as plt
from utils.phase_space import *
from utils.physics_systems import *

system = pendulum_amp_phase_mod_adim  # physics system, see utils.physics_system
bool_stroboscopic = True
bool_title = True

# parameters
g, eps, phi = 0.26, 0.51, 2.97

a, dphi = 1, pi/2
param = g, eps, phi, a, dphi

# x, p sampling boundaries and amount of initial conditions
x_min, x_max = -pi, pi
p_min, p_max = -2, 2
nx, np = 19, 9

# variables to generate time vector
nper, t0 = 1, 0
tf, ndt = 100, 100
vect_t = linspace(t0, t0+tf*2*pi, tf*ndt)

# space periodicity of the system
xmodulo = 2*pi

# sampling the phase space
vect_ic = rect_sampling(x_min, x_max, p_min, p_max, nx, np)

# computing phase space
x, p = phase_space(system, (g, eps, phi, a, dphi), vect_ic, vect_t, xmodulo=xmodulo)

#%%

# graphs
fig = plt.figure()
if bool_title:
    str_dphi = str(int(10*dphi/pi)/10) + r'\pi'
    g_rounded, eps_rounded, phi_rounded = round(100*g)/100, round(100*eps)/100, round(100*phi)/100
    plt.title(r"$n_\mathrm{per} = $" + str(nper) + r' ; $\omega_\mathrm{amp}/\omega_\mathrm{phase}$ = ' +
              r"{} ; $\Delta \phi = {}$".format(a, str_dphi)
              + "\n" + r"$\gamma$ = {} ; $\epsilon$ = {} ; $\phi$ = {}"
              .format(g_rounded, eps_rounded, phi_rounded))
if bool_stroboscopic:
    x_strob, p_strob = stroboscopic(x, p, ndt, 0.5 * t0 / pi)
    plt.scatter(x_strob, p_strob, s=0.2, color='k')
else:
    plt.scatter(x, p, s=0.2, color='k')
plt.xlim(-pi, pi)
# ylim(-5, 6.1)
plt.xlabel('x')
plt.xticks([pi*i/2 for i in range(-2, 3)], [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
plt.ylabel('p')
plt.hlines(1, 1.1*x_min, 1.1*x_max, color=(0.6, 0.1, 0.1), linestyle='--')
plt.hlines(2, 1.1*x_min, 1.1*x_max, color=(0.6, 0.1, 0.1), linestyle='--')
plt.hlines(3, 1.1*x_min, 1.1*x_max, color=(0.6, 0.1, 0.1), linestyle='--')
plt.hlines(4, 1.1*x_min, 1.1*x_max, color=(0.6, 0.1, 0.1), linestyle='--')
plt.hlines(-1, 1.1*x_min, 1.1*x_max, color=(0.6, 0.1, 0.1), linestyle='--')
plt.hlines(-2, 1.1*x_min, 1.1*x_max, color=(0.6, 0.1, 0.1), linestyle='--')
plt.hlines(-3, 1.1*x_min, 1.1*x_max, color=(0.6, 0.1, 0.1), linestyle='--')

plt.show()
