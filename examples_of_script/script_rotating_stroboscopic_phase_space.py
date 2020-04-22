#%%
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
nx, np = 23, 13

# variables to generate time vector
nbImages = 64
nper, t0 = 2, 0  # nper is the number of periods of modulation for the ratchet to be functional
strob_obs = 1  # the system is stroboscopically monitored every (nper*strob_obs)*ndt
tf, ndt = 200, 100

# space regularity of the system
xmodulo = 2*pi

# computing phase space
x, p = phase_space(system, param, x_min, x_max, p_min, p_max, nx, np, tf, ndt=ndt,
                   xmodulo=xmodulo, sampling='rect')

#%%
for image in range(nbImages):
    x_strob, p_strob = stroboscopic(x, p, round(nper*strob_obs*ndt), image/nbImages)

    fig = plt.figure()
    if bool_title:
        str_dphi = str(int(10*dphi/pi)/10) + r'\pi'
        g_rounded, eps_rounded, phi_rounded = round(100*g)/100, round(100*eps)/100, round(100*phi)/100
        plt.title(r"$n_\mathrm{per} = $" + str(nper) + ' ; obs = ' + str(strob_obs)
                  + r' ; $\omega_\mathrm{amp}/\omega_\mathrm{phase}$ = ' +
                  r"{} ; $\Delta \phi = {}$".format(a, str_dphi)
                  + "\n" + r"$\gamma$ = {} ; $\epsilon$ = {} ; $\phi$ = {}"
                  .format(g_rounded, eps_rounded, phi_rounded))
    plt.scatter(x_strob, p_strob, s=0.2, color='k')
    plt.xlim(-pi, pi)
    plt.ylim(-3.75, 5)
    plt.xlabel('x')
    plt.xticks([pi*i/2 for i in range(-2, 3)], [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
    plt.ylabel('p')
    plt.savefig('results/phase_spaces/rotating_phase_space/20200422/' +
                'SPS_nper2_a1_Dphi0p5Pi_g0p32_eps0p22_phi1p86_obs1/images/' +
                'SPS_nper2_a1_Dphi0p5Pi_g0p32_eps0p22_phi1p86_obs0p5_' + str(image) + '.png')

#%%
#%%

