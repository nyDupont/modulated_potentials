import numpy as np
import matplotlib.pyplot as plt
from utils.physics_systems import *
from utils.utils import *


# system
system = simple_pendulum
k = 1  # k = sqrt(g/l)

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
# plt.subplot(131)
# plt.plot(vect_t, x)
# plt.xlabel('temps')
# plt.ylabel('position')
#
# plt.subplot(132)
# plt.plot(vect_t, p)
# plt.xlabel('temps')
# plt.ylabel('quantité de mouvement')

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
