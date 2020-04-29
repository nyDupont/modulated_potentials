import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from utils.physics_systems import *
from utils.phase_space import *
from utils.utils import *


# system
system = simple_pendulum
k = 1  # k = sqrt(g/l)

# ########################################################################
# # I- Motion state of the simple pendulum for a first initial condition #
# ########################################################################
#
# # time vector
# tf, ndt = 8.34, 1000
# vect_t = np.linspace(0, tf, round(ndt*tf))
#
# # IC
# x0, p0 = 2, 0
#
# # resolution
# x, p = resolution(system, (x0, p0), vect_t, k)
#
# # graphs
# fontsize = 15
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['font.sans-serif'] = 'Computer Modern'
# fig = plt.figure(1, figsize=(4, 15))
# plt.subplots_adjust(left=.2, right=.99, bottom=.1, top=.99, hspace=0)
#
# xlim = np.pi
# ylim = 2
#
# plt.subplot(411)
# plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--')
# plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--')
# plt.scatter(x[0], p[0])
# plt.xlim(-xlim, xlim)
# plt.ylim(-ylim, ylim)
# plt.xticks([], '', fontsize=int(0.8*fontsize))
# plt.yticks([-1, 0, 1], ['-1', '0', '1'], fontsize=int(0.8*fontsize))
#
# plt.subplot(412)
# plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--')
# plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--')
# plt.plot(x[:int(0.25*tf*ndt):2], p[:int(0.25*tf*ndt):2], '--')
# plt.scatter(x[int(0.25*tf*ndt)], p[int(0.25*tf*ndt)])
# plt.xlim(-xlim, xlim)
# plt.ylim(-ylim, ylim)
# plt.xticks([], '', fontsize=int(0.8*fontsize))
# plt.yticks([-1, 0, 1], ['-1', '0', '1'], fontsize=int(0.8*fontsize))
#
# plt.subplot(413)
# plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--')
# plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--')
# plt.plot(x[:int(0.5*tf*ndt):2], p[:int(0.5*tf*ndt):2], '--')
# plt.scatter(x[int(0.5*tf*ndt)], p[int(0.5*tf*ndt)])
# plt.xlim(-xlim, xlim)
# plt.ylim(-ylim, ylim)
# plt.xticks([], '', fontsize=int(0.8*fontsize))
# plt.yticks([-1, 0, 1], ['-1', '0', '1'], fontsize=int(0.8*fontsize))
#
# plt.subplot(414)
# plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--')
# plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--')
# plt.plot(x[:int(tf*ndt):2], p[:int(tf*ndt):2], '--')
# plt.scatter(x[-1], p[-1])
# plt.xlim(-xlim, xlim)
# plt.ylim(-ylim, ylim)
# plt.xticks(fontsize=int(0.8*fontsize))
# plt.yticks([-1, 0, 1], ['-1', '0', '1'], fontsize=int(0.8*fontsize))
#
#
# plt.text(-4.25, 8.5, 'quantité de mouvement', rotation=90, fontsize=fontsize)
# plt.text(-0.75, -3.25, 'position', fontsize=fontsize)
#
# plt.show()

# # ######################### #
# # II- The whole phase space #
# # ######################### #
#
# # time vector parameters
# t0, tf, ndt = 0, 25, 2000
# vect_t = linspace(t0, t0+tf, ndt)
#
# # phase space parameters
# xmodulo = 2*pi
#
#
# # initial conditions (IC) :
# x_ext = pi
# p_ext = 2
# n_orbits = 8
#
# x_ic_bounded = list(linspace(-1.01*x_ext, 0, n_orbits))
# p_ic_bounded = [0 for _ in range(n_orbits)]
#
# x_ic_unbounded = [-pi for _ in range(n_orbits)]
# p_ic_unbounded = list(linspace(-p_ext, 0, int(n_orbits/2) + 1)[:-1]) + list(linspace(0, p_ext, int(n_orbits/2) + 1)[1:])
#
# vect_ic_b = [(x_ic_bounded[i], p_ic_bounded[i]) for i in range(len(x_ic_bounded))]
# vect_ic_unb = [(x_ic_unbounded[i], p_ic_unbounded[i]) for i in range(len(x_ic_unbounded))]
#
# # computing the phase space
# x_b, p_b = phase_space(system, k, vect_ic_b, vect_t, xmodulo=xmodulo)
# x_unb, p_unb = phase_space(system, k, vect_ic_unb, vect_t, xmodulo=xmodulo)
#
# # graph
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['font.sans-serif'] = 'Computer Modern'
# fontsize = 15
# xlim, ylim = pi, 3
# plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--', zorder=0)
# plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--', zorder=1)
# fig = plt.figure(1, figsize=(6, 6))
# plt.scatter(x_b, p_b, s=2,  c=[(0.12, 0.47, 0.71),],  zorder=2)
# plt.scatter(x_unb, p_unb, s=2, c=[(0.06, 0.23, 0.35),],  zorder=2)
# plt.xlim(-xlim, xlim)
# plt.ylim(-ylim, ylim)
# plt.xlabel('position', fontsize=fontsize)
# plt.ylabel('quantité de mouvement', fontsize=fontsize)
# plt.xticks([i/2*pi for i in range(-2, 3)], [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'],
#            fontsize=int(0.8*fontsize))
# plt.yticks(fontsize=int(0.8*fontsize))
#
# plt.show()


# ################################# #
# III- Unbounded-states explication #
# ################################# #

# time vector parameters
t0, tf, ndt = 0, 2, 500
vect_t = linspace(t0, t0+tf, ndt)

x0, p0 = 0, 2.25
xlim, ylim = pi, 3
fontsize = 15
n_yticks = 5

x, p = resolution(system, (x0, p0), vect_t, k)

# graph
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.sans-serif'] = 'Computer Modern'

fig = plt.figure(1, figsize=(4, 15))
plt.subplots_adjust(left=.2, right=.99, bottom=.1, top=.99, hspace=0)
plt.subplot(311)
plt.scatter(x[0], p[0], zorder=2)
plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--', zorder=0)
plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--', zorder=1)
plt.xlim(-xlim, xlim)
plt.ylim(-ylim, ylim)
plt.xticks()
plt.yticks([i for i in range(-int(n_yticks/2), int(n_yticks/2)+1)], fontsize=int(0.8*fontsize))

plt.subplot(312)
plt.plot(x, p, color='C0', linestyle='--')
plt.scatter(x[-20], p[-20], zorder=2)
plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--', zorder=0)
plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--', zorder=1)
plt.xlim(-xlim, xlim)
plt.ylim(-ylim, ylim)
plt.xticks()
plt.yticks([i for i in range(-int(n_yticks/2), int(n_yticks/2)+1)], fontsize=int(0.8*fontsize))

plt.subplot(313)
plt.plot(x, p, color='C0', linestyle='--')
plt.scatter(x[-20], -p[-20], zorder=2)
plt.hlines(0, -1.1*xlim, 1.1*xlim, color='gray', linestyle='--', zorder=0)
plt.vlines(0, -1.1*ylim, 1.1*ylim, color='gray', linestyle='--', zorder=1)
plt.xlim(-xlim, xlim)
plt.ylim(-ylim, ylim)
plt.xticks([i/2*pi for i in range(-2, 3)], [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'],
           fontsize=int(0.8*fontsize))
plt.yticks([i for i in range(-int(n_yticks/2), int(n_yticks/2)+1)], fontsize=int(0.8*fontsize))

plt.text(-4.3, 9.3, 'quantité de mouvement', rotation=90, fontsize=fontsize)
plt.text(-0.75, -4.4, 'position', fontsize=fontsize)


plt.show()
