#%%
from numpy import pi
import matplotlib.pyplot as plt
from utils.physics_systems import *
from utils.utils import *
from utils.math_functions import *


system = pendulum_amp_phase_mod_adim
g, eps, phi = 0.26, 0.51, 2.97
a, dphi = 1, pi/2

nper, ndt = 20, 1000
t0 = 0
vect_t = linspace(t0, t0 + nper*2*pi, nper*ndt)

# graph parameters
ylim2_min, ylim2_max = 0, 2.3
xlim_min, xlim_max = 0, nper*2*pi
freq_xticks = 4
n_yticks = 5

xticks = [freq_xticks*i*2*pi for i in range(int(nper/freq_xticks)+1)]
xticks_label = [str(freq_xticks*i) for i in range(int(nper/freq_xticks)+1)]

f = plt.figure()
f.subplots_adjust(wspace=0.06, hspace=0.06)


# ###############
# x0, p0 = 0, 0.5
# x, _ = resolution(system, (x0, p0), vect_t, (g, eps, phi, a, dphi))
# x_noPot = affine(vect_t, p0, x0)
# x_noMod, _ = resolution(system, (x0, p0), vect_t, (g, 0, 0, 0, 0))
#
# furthest_pos_site = int(0.5*max(max(x), max(x_noPot), max(x_noMod))/pi) + 1
# furthest_neg_site = int(0.5*min(min(x), min(x_noPot), min(x_noMod))/pi)
# visited_sites = furthest_pos_site - furthest_neg_site
#
# yticks = [i*2*pi for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]
# yticks_label = [str(i) for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]
#
# r = x/array(x_noPot)

# graphs

# ax1 = plt.subplot2grid((3, 2), (0, 0))
# ax1.plot(vect_t, x, label='$x(t)$')
# ax1.plot(vect_t, x_noMod, c='C2',  label=r'$x_\mathrm{noMod}(t)$')
# ax1.plot(vect_t, x_noPot, c='C1', linestyle='--', label=r'$x_\mathrm{noPot}(t)$')
# plt.xticks(xticks, [])
# plt.legend(bbox_to_anchor=(1.4, 1.35), ncol=3)
# plt.yticks(yticks, yticks_label)
# plt.xlim(xlim_min, xlim_max)
# ax1.grid()
# xmin, xmax = plt.xlim()
# ymin, ymax = plt.ylim()
# w, h = abs(xmax-xmin), abs(ymax-ymin)
# ax1.text(xmin+0.03*w, ymin+0.8*h, 'a', horizontalalignment='left', verticalalignment='baseline', weight='bold')
#
# ax2 = plt.subplot2grid((3, 2), (0, 1))
# ax2.plot(vect_t, r, c=(0.7, 0.05, 0.5), label=r'$x(t)/x_\mathrm{noPot}(t)$')
# plt.legend(bbox_to_anchor=(1, 1.35))
# plt.xticks(xticks, [])
# plt.ylim(ylim2_min, ylim2_max)
# plt.xlim(xlim_min, xlim_max)
# ax2.grid()
# ax2.yaxis.tick_right()
#
# for tic in ax1.xaxis.get_major_ticks():
#     tic.tick1On = tic.tick2On = False
# for tic in ax2.xaxis.get_major_ticks():
#     tic.tick1On = tic.tick2On = False
# #######################
#
# ###############
# x0, p0 = 1, 0.89
# x, _ = resolution(system, (x0, p0), vect_t, (g, eps, phi, a, dphi))
# x_noPot = affine(vect_t, p0, x0)
# x_noMod, _ = resolution(system, (x0, p0), vect_t, (g, 0, 0, 0, 0))
#
# furthest_pos_site = int(0.5*max(max(x), max(x_noPot), max(x_noMod))/pi) + 1
# furthest_neg_site = int(0.5*min(min(x), min(x_noPot), min(x_noMod))/pi)
# visited_sites = furthest_pos_site - furthest_neg_site
#
# yticks = [i*2*pi for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]
# yticks_label = [str(i) for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]
#
# r = x/array(x_noPot)
#
# # graphs
#
# ax1 = plt.subplot2grid((3, 2), (1, 0))
# ax1.plot(vect_t, x)
# ax1.plot(vect_t, x_noMod, c='C2')
# ax1.plot(vect_t, x_noPot, c='C1', linestyle='--')
# plt.xticks(xticks, [])
# plt.yticks(yticks, yticks_label)
# plt.xlim(xlim_min, xlim_max)
# ax1.grid()
# xmin, xmax = plt.xlim()
# ymin, ymax = plt.ylim()
# w, h = abs(xmax-xmin), abs(ymax-ymin)
# ax1.text(xmin+0.03*w, ymin+0.8*h, 'b', horizontalalignment='left', verticalalignment='baseline', weight='bold')
#
# ax2 = plt.subplot2grid((3, 2), (1, 1))
# ax2.plot(vect_t, r, c=(0.7, 0.05, 0.5))
# plt.xticks(xticks, [])
# plt.ylim(ylim2_min, ylim2_max)
# plt.xlim(xlim_min, xlim_max)
# ax2.grid()
# ax2.yaxis.tick_right()
#
# for tic in ax1.xaxis.get_major_ticks():
#     tic.tick1On = tic.tick2On = False
# for tic in ax2.xaxis.get_major_ticks():
#     tic.tick1On = tic.tick2On = False
# #######################
#
# ###############
# x0, p0 = 1, 1.92
# x, _ = resolution(system, (x0, p0), vect_t, (g, eps, phi, a, dphi))
# x_noPot = affine(vect_t, p0, x0)
# x_noMod, _ = resolution(system, (x0, p0), vect_t, (g, 0, 0, 0, 0))
#
# furthest_pos_site = int(0.5*max(max(x), max(x_noPot), max(x_noMod))/pi) + 1
# furthest_neg_site = int(0.5*min(min(x), min(x_noPot), min(x_noMod))/pi)
# visited_sites = furthest_pos_site - furthest_neg_site
#
# yticks = [i*2*pi for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]
# yticks_label = [str(i) for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]
#
# r = x/array(x_noPot)
#
# # graphs
#
# ax1 = plt.subplot2grid((3, 2), (2, 0))
# ax1.plot(vect_t, x)
# ax1.plot(vect_t, x_noMod, c='C2')
# ax1.plot(vect_t, x_noPot, c='C1', linestyle='--')
# plt.xticks(xticks, xticks_label)
# plt.yticks(yticks, yticks_label)
# plt.xlim(xlim_min, xlim_max)
# ax1.grid()
# xmin, xmax = plt.xlim()
# ymin, ymax = plt.ylim()
# w, h = abs(xmax-xmin), abs(ymax-ymin)
# ax1.text(xmin+0.03*w, ymin+0.8*h, 'c', horizontalalignment='left', verticalalignment='baseline', weight='bold')
#
# ax2 = plt.subplot2grid((3, 2), (2, 1))
# ax2.plot(vect_t, r, c=(0.7, 0.05, 0.5))
# plt.xticks(xticks, xticks_label)
# plt.ylim(ylim2_min, ylim2_max)
# plt.xlim(xlim_min, xlim_max)
# ax2.grid()
# ax2.yaxis.tick_right()

#######################

###############
x0, p0 = 3, 0.3
x, _ = resolution(system, (x0, p0), vect_t, (g, eps, phi, a, dphi))
x_noPot = affine(vect_t, p0, x0)
x_noMod, _ = resolution(system, (x0, p0), vect_t, (g, 0, 0, 0, 0))

furthest_pos_site = int(0.5*max(max(x), max(x_noPot), max(x_noMod))/pi) + 1
furthest_neg_site = int(0.5*min(min(x), min(x_noPot), min(x_noMod))/pi)
visited_sites = furthest_pos_site - furthest_neg_site

yticks = [i*2*pi for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]
yticks_label = [str(i) for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]

r = x/array(x_noPot)

#%%
# graphs

ax1 = plt.subplot2grid((3, 2), (0, 0))
ax1.plot(vect_t, x, label='$x(t)$')
ax1.plot(vect_t, x_noMod, c='C2',  label=r'$x_\mathrm{noMod}(t)$')
ax1.plot(vect_t, x_noPot, c='C1', linestyle='--', label=r'$x_\mathrm{noPot}(t)$')
plt.xticks(xticks, [])
plt.legend(bbox_to_anchor=(1.4, 1.35), ncol=3)
plt.yticks(yticks, yticks_label)
plt.xlim(xlim_min, xlim_max)
ax1.grid()
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
w, h = abs(xmax-xmin), abs(ymax-ymin)
ax1.text(xmin+0.03*w, ymin+0.8*h, 'd', horizontalalignment='left', verticalalignment='baseline', weight='bold')

ax2 = plt.subplot2grid((3, 2), (0, 1))
ax2.plot(vect_t, r, c=(0.7, 0.05, 0.5), label=r'$x(t)/x_\mathrm{noPot}(t)$')
plt.legend(bbox_to_anchor=(1, 1.35))
plt.xticks(xticks, [])
plt.ylim(ylim2_min, ylim2_max)
plt.xlim(xlim_min, xlim_max)
ax2.grid()
ax2.yaxis.tick_right()

for tic in ax1.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False
for tic in ax2.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False
#######################

###############
x0, p0 = 3, -1
x, _ = resolution(system, (x0, p0), vect_t, (g, eps, phi, a, dphi))
x_noPot = affine(vect_t, p0, x0)
x_noMod, _ = resolution(system, (x0, p0), vect_t, (g, 0, 0, 0, 0))

furthest_pos_site = int(0.5*max(max(x), max(x_noPot), max(x_noMod))/pi) + 1
furthest_neg_site = int(0.5*min(min(x), min(x_noPot), min(x_noMod))/pi)
visited_sites = furthest_pos_site - furthest_neg_site

yticks = [i*2*pi for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]
yticks_label = [str(i) for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]

# r = true_div(x, x_noPot)
r = x/array(x_noPot)

# graphs

ax1 = plt.subplot2grid((3, 2), (1, 0))
ax1.plot(vect_t, x)
ax1.plot(vect_t, x_noMod, c='C2')
ax1.plot(vect_t, x_noPot, c='C1', linestyle='--')
plt.xticks(xticks, [])
plt.yticks(yticks, yticks_label)
plt.xlim(xlim_min, xlim_max)
ax1.grid()
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
w, h = abs(xmax-xmin), abs(ymax-ymin)
ax1.text(xmin+0.03*w, ymin+0.8*h, 'e', horizontalalignment='left', verticalalignment='baseline', weight='bold')

ax2 = plt.subplot2grid((3, 2), (1, 1))
ax2.plot(vect_t, r, c=(0.7, 0.05, 0.5))
plt.xticks(xticks, [])
plt.ylim(ylim2_min, ylim2_max)
plt.xlim(xlim_min, xlim_max)
ax2.grid()
ax2.yaxis.tick_right()

for tic in ax1.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False
for tic in ax2.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False
#######################

###############
x0, p0 = 0, -2
x, _ = resolution(system, (x0, p0), vect_t, (g, eps, phi, a, dphi))
x_noPot = affine(vect_t, p0, x0)
x_noMod, _ = resolution(system, (x0, p0), vect_t, (g, 0, 0, 0, 0))

furthest_pos_site = int(0.5*max(max(x), max(x_noPot), max(x_noMod))/pi) + 1
furthest_neg_site = int(0.5*min(min(x), min(x_noPot), min(x_noMod))/pi)
visited_sites = furthest_pos_site - furthest_neg_site

yticks = [i*2*pi for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]
yticks_label = [str(i) for i in range(furthest_neg_site, furthest_pos_site+1, int(visited_sites/n_yticks))]

r = x/array(x_noPot)

# graphs

ax1 = plt.subplot2grid((3, 2), (2, 0))
ax1.plot(vect_t, x)
ax1.plot(vect_t, x_noMod, c='C2')
ax1.plot(vect_t, x_noPot, c='C1', linestyle='--')
plt.xticks(xticks, xticks_label)
plt.yticks(yticks, yticks_label)
plt.xlim(xlim_min, xlim_max)
ax1.grid()
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
w, h = abs(xmax-xmin), abs(ymax-ymin)
ax1.text(xmin+0.03*w, ymin+0.8*h, 'f', horizontalalignment='left', verticalalignment='baseline', weight='bold')

ax2 = plt.subplot2grid((3, 2), (2, 1))
ax2.plot(vect_t, r, c=(0.7, 0.05, 0.5))
plt.xticks(xticks, xticks_label)
plt.ylim(ylim2_min, ylim2_max)
plt.xlim(xlim_min, xlim_max)
ax2.grid()
ax2.yaxis.tick_right()


plt.show()
