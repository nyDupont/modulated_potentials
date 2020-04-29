#%%
import matplotlib.pyplot as plt
import os
from utils.phase_space import *
from utils.physics_systems import *
from utils.utils import *

nbImages = 64  # total number of images for the rotation of the phase space
nbDecimals = 3  # max number of kept decimals in figure title.s and file name.s

system = pendulum_amp_phase_mod_adim  # physics system, see utils.physics_system
bool_stroboscopic = True  # boolean for stroboscopic observation
bool_title = True  # boolean to display titles in figure.s
bool_save = True  # boolean to save figure.s
bool_highlight_x0_p0 = True  # boolean to make it easy to follow the IC (x0, p0) (next line)
x0, p0 = 0, 0
highlighted_marker_size = 150

# parameters
g, eps, phi = [1.1869160180292213, 0.2756995577344605, 1.718139099894072]
a, dphi = 1, pi/2
param = g, eps, phi, a, dphi

# x, p sampling boundaries and amount of initial conditions
x_min, x_max = -pi, pi
p_min, p_max = -2, 2
nx, np = 19, 9

# variables to generate time vector
nper, t0 = 1, 0  # nper is the number of periods of modulation for the ratchet to be functional
strob_obs = 1  # the system is stroboscopically monitored every (nper*strob_obs)*ndt
tf, ndt = 100*strob_obs, 100

# space periodicity of the system
xmodulo = 2*pi

# computing phase space
x, p = phase_space(system, param, x_min, x_max, p_min, p_max, nx, np, round(tf), ndt=ndt,
                   xmodulo=xmodulo, sampling='rect')

if bool_highlight_x0_p0:
    vect_t = linspace(t0, t0+nper*2*pi, ndt*nper)
    x2, p2 = resolution(system, (x0, p0), vect_t, param)
    x2 = modulo_zcentered(x2, xmodulo)

#%%
# graphs

a_rounded, dphi_rounded, g_rounded, eps_rounded, phi_rounded = decimals(a, nbDecimals), decimals(dphi/pi, 2),\
                                                               decimals(g, nbDecimals), decimals(eps, nbDecimals),\
                                                               decimals(phi, nbDecimals),

if bool_save:  # we one wants to save, creation of the directory where images will be saved
    directory_parent_path = '../results/phase_spaces/rotating_phase_spaces/'
    ymd = str_yyyymmdd()
    subject = 'SPS_nper{}_a{}_Dphi{}Pi_g{}_eps{}_phi{}_obs{}'.format(nper, a_rounded, dphi_rounded, g_rounded,
                                                                     eps_rounded, phi_rounded, strob_obs).replace('.',
                                                                                                                  'p')
    directory_path = directory_parent_path + ymd + '/' + subject + '/images/'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print('directory:\n \t {}{}/\n\t{}/\nhas been created'.format(directory_parent_path, ymd, subject))

for image in range(nbImages):
    x_strob, p_strob = stroboscopic(x, p, round(nper*strob_obs*ndt), image/nbImages)

    fig = plt.figure()
    if bool_title:
        str_dphi = str(dphi_rounded) + r'\pi'
        plt.title(r"$n_\mathrm{per} = $" + str(nper) + ' ; obs = ' + str(strob_obs)
                  + r' ; $\omega_\mathrm{amp}/\omega_\mathrm{phase}$ = ' +
                  r"{} ; $\Delta \phi = {}$".format(a, str_dphi)
                  + "\n" + r"$\gamma$ = {} ; $\epsilon$ = {} ; $\phi$ = {}"
                  .format(g_rounded, eps_rounded, phi_rounded))

    plt.scatter(x_strob, p_strob, s=0.2, color='k')
    if bool_highlight_x0_p0:
        plt.scatter(x2[round(image/nbImages*nper*ndt)], p2[round(image/nbImages*nper*ndt)], color='C1', marker='+',
                    s=highlighted_marker_size)
    plt.xlim(-pi, pi)
    plt.ylim(-3.75, 5)
    plt.xlabel('x')
    plt.xticks([pi*i/2 for i in range(-2, 3)], [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
    plt.ylabel('p')

    if bool_save:
        plt.savefig('{}/{}_image{}Of{}.png'.format(directory_path, subject, image+1, nbImages))

plt.close('all')
#%%
