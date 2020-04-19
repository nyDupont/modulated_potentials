import matplotlib.pyplot as plt
from phase_space.phase_space import *

system = pendulum_amp_mod_adim  # physics system, see utils.physics_system
bool_stroboscopic = True

# parameters
g, eps = 0.25, 0.15

# x, p sampling boundaries and amount of initial conditions
x_min, x_max = -pi, pi
p_min, p_max = -2, 2
nx, np = 50, 50

# variables to generate time vector
tf, ndt = 100, 100

# space regularity of the system
xmodulo = 2*pi

# computing phase space
x, p = phase_space(system, (g, eps), x_min, x_max, p_min, p_max, nx, np, tf, ndt=ndt, stroboscopic=bool_stroboscopic,
                   xmodulo=xmodulo, sampling='diag')

# graphs
plt.scatter(x, p, s=0.2, color='k')
plt.xlim(-pi, pi)
# ylim(-5, 6.1)
plt.xlabel('x')
plt.ylabel('p')

plt.show()

