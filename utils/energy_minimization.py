from numpy import pi
from utils.physics_systems import *
from utils.utils import *

# useful global variables
iteration_optimisation = 0  # a counter of how many times energy_adim is called


# A function that returns the the mechanical energy increase after vect_t, used to find the param that minimize it
def mechanical_energy_pendulum_amp_phase_mod_adim(param, *args):
    vect_t, a, dphi = args
    param = list(param) + [a, dphi]  # that way only original argument parameters are accessible to Nelder-Mead
    x_sol_adim, p_sol_adim = resolution(pendulum_amp_phase_mod_adim, (0, 0), vect_t, param)

    global iteration_optimisation  # a counter of how many times energy_adim is called
    iteration_optimisation += 1

    if abs(x_sol_adim[-1]) > pi:  # checking that the particle has indeed changed site
        energie_i = hamiltonian_amp_phase_mod_adim((x_sol_adim[0], p_sol_adim[0]), vect_t[0], param)
        energie_f = hamiltonian_amp_phase_mod_adim((x_sol_adim[-1], p_sol_adim[-1]), vect_t[-1], param)
        print(iteration_optimisation, "saut")
        return energie_f - energie_i

    else:  # the particle has stayed in the same site
        print(iteration_optimisation, "non")
        great_energy = 2 ** 100  # a great amount of "energy" to force the passage in a next cell when minimizing
        # energie_adim ; should I use numpy.inf ?
        return great_energy  # the particle change site (great_energy is defined above)
