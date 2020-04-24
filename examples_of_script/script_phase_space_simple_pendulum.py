import numpy as np
import matplotlib.pyplot as plt
from utils.physics_systems import *
from utils.phase_space import *
from utils.utils import *


# system
system = simple_pendulum
k = 1  # k = sqrt(g/l)

########################################################################
# I- Motion state of the simple pendulum for a first initial condition #
########################################################################

# time vector
tf, ndt = 8.34, 1000
vect_t = np.linspace(0, tf, round(ndt*tf))

# IC
x0, p0 = 2, 0

# resolution
x, p = resolution(system, (x0, p0), vect_t, k)

# graphs
fontsize = 15
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.sans-serif'] = 'Computer Modern'
fig = plt.figure(1, figsize=(4, 15))
plt.subplots_adjust(left=.2, right=.99, bottom=.1, top=.99, hspace=0)

xlim = np.pi
ylim = 2

plt.subplot(411)
plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--')
plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--')
plt.scatter(x[0], p[0])
plt.xlim(-xlim, xlim)
plt.ylim(-ylim, ylim)
plt.xticks([], '', fontsize=int(0.8*fontsize))
plt.yticks([-1, 0, 1], ['-1', '0', '1'], fontsize=int(0.8*fontsize))

plt.subplot(412)
plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--')
plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--')
plt.plot(x[:int(0.25*tf*ndt):2], p[:int(0.25*tf*ndt):2], '--')
plt.scatter(x[int(0.25*tf*ndt)], p[int(0.25*tf*ndt)])
plt.xlim(-xlim, xlim)
plt.ylim(-ylim, ylim)
plt.xticks([], '', fontsize=int(0.8*fontsize))
plt.yticks([-1, 0, 1], ['-1', '0', '1'], fontsize=int(0.8*fontsize))

plt.subplot(413)
plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--')
plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--')
plt.plot(x[:int(0.5*tf*ndt):2], p[:int(0.5*tf*ndt):2], '--')
plt.scatter(x[int(0.5*tf*ndt)], p[int(0.5*tf*ndt)])
plt.xlim(-xlim, xlim)
plt.ylim(-ylim, ylim)
plt.xticks([], '', fontsize=int(0.8*fontsize))
plt.yticks([-1, 0, 1], ['-1', '0', '1'], fontsize=int(0.8*fontsize))

plt.subplot(414)
plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--')
plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--')
plt.plot(x[:int(tf*ndt):2], p[:int(tf*ndt):2], '--')
plt.scatter(x[-1], p[-1])
plt.xlim(-xlim, xlim)
plt.ylim(-ylim, ylim)
plt.xticks(fontsize=int(0.8*fontsize))
plt.yticks([-1, 0, 1], ['-1', '0', '1'], fontsize=int(0.8*fontsize))


plt.text(-4.25, 8.5, 'quantité de mouvement', rotation=90, fontsize=fontsize)
plt.text(-0.75, -3.25, 'position', fontsize=fontsize)

plt.show()

#############################
# II- The whole phase space #
#############################

# # time vector parameters
# tf, ndt = 10, 200
#
# # phase space parameters
# xmax, pmax = pi, 2
# nx, np = 21, 21
# xmodulo = 2*pi
# frac = 3/5
#
# # computing the phase space
# x, p = phase_space(system, k, -xmax, xmax, -pmax, pmax, nx, np, tf, ndt=ndt, xmodulo=xmodulo, sampling='diag')
#
# # graph
# fontsize = 15
# xlim, ylim = pi, 3
# plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--', zorder=0)
# plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--', zorder=1)
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['font.sans-serif'] = 'Computer Modern'
# fig = plt.figure(1, figsize=(6, 6))
# plt.scatter(x, p, s=2, zorder=2)
# plt.xlim(-xlim, xlim)
# plt.ylim(-ylim, ylim)
# plt.xlabel('position', fontsize=fontsize)
# plt.ylabel('quantité de mouvement', fontsize=fontsize)
# plt.xticks([i/2*pi for i in range (-2, 3)], [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'],
#            fontsize=int(0.8*fontsize))
# plt.yticks(fontsize=int(0.8*fontsize))
#
# plt.show()
