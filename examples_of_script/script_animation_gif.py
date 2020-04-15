from numpy import linspace
import matplotlib.pyplot as plt
from utils.physics_systems import *

bool_latex_style = 1  # for the plot to be edited in latex serif
bool_show = 1
bool_complition_percentage = 0
bool_save = 0
path = './results/gif/source_pictures/picture_'
dpi = 80

# system
system = pendulum_amp_phase_mod_adim

# parameters
g, eps, phi = 0.79, 0.27, 2.7  # works for a = 1, dphi = pi/2
a, dphi = 1, pi/2
param = g, eps, phi

xpv_space_frequency = 2  # ploting a position or momentum or potential point every xpv_frame_freq
time_frame_frequency = 8  # idem in time

# time vector
nper = 3
ndt = 1000  # plays here a special role on animation speed
tf = nper*2*pi  # dimensionless final time
vect_t = linspace(0, tf, round(nper*ndt))  # time vector

nb_space_points = 1000  # space sampling to plot the potential
V = zeros((nb_space_points, round(nper*ndt)))  # definition of an array to store the V(x,t)

# solving the DE
x_sol, p_sol = resolution(pendulum_amp_phase_mod_adim, (0, 0), vect_t, param, a=a, dphi=dphi)
x_f = x_sol[-1]
x_sol_translated = [x - x_f/2 for x in x_sol]  # translating the solution for the particle to go through all screen

v_sol_adim = potential_amp_phase_mod_adim(x_sol, vect_t, param)  # potential V(x,t) experienced by the particle
vect_x = linspace(-0.5*x_f, 1.51*x_f, nb_space_points)  # vect_x to plot potentials
vect_x_translated = [x - x_f/2 for x in vect_x]  # translating it as it has been done for x

for i in range(round(nper*ndt)):
    V[:, i] = potential_amp_phase_mod_adim(vect_x, vect_t[i], param)  # evalutaed in vect_x but to be plotted translated

# definition of useful variables for the graphs
x_0, p_0, v_0, v_max = x_sol_translated[0], p_sol[0], v_sol_adim[0], max(V[:, 0])
p_min, p_max = min(p_sol), max(p_sol)  # for scale

# animation
if bool_latex_style:
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.sans-serif'] = 'Computer Modern'

if bool_show:
    plt.ion()
fig = plt.figure(figsize=(5, 3))
plt.subplots_adjust(left=0.06, right=0.94)

axes = fig.add_subplot(121)
l1, = plt.plot(vect_x_translated[::xpv_space_frequency], V[:, 0][::xpv_space_frequency])
p_l_1 = plt.axvline(x=x_0, linestyle='dotted', color=(0.2, 0.6, 0.05))
# p_a_1 = plt.arrow(x_0, v_0, p_0, 0, color=(0.7, 0.05, 0.2))
# p_a_1 = plt.annotate('', xytext=(x_0, v_0), xy=(x_0+d, v_0), arrowprops={'facecolor': 'black'})
p1, = plt.plot(x_0, v_0, marker='o', color=(0.9, 0.4, 0.05))

plt.title('particle in 1-d potential V(x,t)')

plt.xlabel('position')
plt.xticks([])
# plt.ylabel('V [J]')
plt.ylabel('potential')
plt.yticks([])

axes.set_xlim(-x_f/2-pi, x_f/2+pi)  # à vérifier
axes.set_ylim(v_0-0.1*(v_max-v_0), v_max+0.1*(v_max-v_0))

axes2 = fig.add_subplot(122)

for x_line in range(-1, round(nper)+2):
    plt.axvline(x=x_0+(x_line+1/2)*2*pi, linestyle='dotted', color=(0.6, 0.6, 0.6))

plt.axhline(y=0, linestyle='dotted', color=(0.2, 0.2, 0.2))
l2, = plt.plot(x_0, p_0, linestyle='--', color=(0.9, 0.4, 0.05))
# p_l_2_v = plt.axvline(x=x_0, linestyle='dashdot', color=(0.2, 0.6, 0.05))
# p_l_2_h = plt.axhline(y=p_0, linestyle='dashdot', color=(0.7, 0.05, 0.2))
p2, = plt.plot(x_0, p_0, marker='o', color=(0.9, 0.4, 0.05))
plt.title('phase space (x,p)')
plt.xlabel('position')
plt.xticks([])
plt.ylabel('momentum')
plt.yticks([])

axes2.set_xlim(x_0-1.2*2*pi, x_0+(nper+1)*1.05*2*pi)


axes2.set_ylim(p_min-0.35*(p_max-p_min), p_max+0.35*(p_max-p_min))

if bool_save:
    plt.savefig('gif/source_pictures/picture_0', dpi=dpi)
if bool_show:
    fig.canvas.draw()

# x_0 = x_sol_dim_translate[0]
j = 1

for i in range(1, round(nper*ndt) - 1, time_frame_frequency):
    x_i, p_i, v_i = x_sol_translated[i], p_sol[i], v_sol_adim[i]
    v_i_min = min(V[:, i])  # defined to update scale
    # print(p_i, p_max, v_i, v_max)

    p_l_1.set_xdata(x_i)
    # p_l_1.ymax = j/nbre_points_temps*freq_trace_temporel
    # p_a_1.remove()
    # p_a_1 = plt.annotate('', xytext=(x_i, p_i), xy=(x_i+2*10**20*p_i, p_i), arrowprops={'facecolor': 'black'})

    l1.set_ydata(V[:, i][::xpv_space_frequency])
    p1.set_data(x_i, v_i)
    axes.set_ylim(v_i_min - 0.1 * (v_max - v_i_min), v_max + 0.1 * (v_max - v_i_min))

    # p_l_2_v.set_xdata(x_i)
    # p_l_2_h.set_xdata(p_i)
    l2.set_data(x_sol_translated[0:i + 1:xpv_space_frequency], p_sol[0:i + 1:xpv_space_frequency])
    p2.set_data(x_i, p_i)

    if bool_save:
        plt.savefig(path + str(j), dpi=dpi)
    if bool_complition_percentage:
        # stdout.write(str(int(j/nbre_points_temps*10000*freq_trace_temporel)/100) + '%')
        print(str(int(j / nper*ndt * 10000 * time_frame_frequency) / 100) + '%')
    j += 1
    if bool_show:
        fig.canvas.draw()
        fig.canvas.flush_events()
