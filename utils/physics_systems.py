from numpy import sin, cos, pi
from utils.utils import *
from integrators.rk4 import *

# NB: following systems are dimensionless


###############################
# 0: Harmonic oscillator (HO) #
###############################
# Hamiltonian of the HO (mass m=1)
def hamitonian_ho(w, t, param):
    x, p = w  # unpacking variables at time t
    omega = param  # unpacking potential parameter

    return p**2/2 + omega**2*x**2/2


# Potential of the HO (mass m=1)
def potential_ho(w, t, param):
    x, p = w  # unpacking variables at time t
    omega = param  # unpacking potential parameter

    return omega**2*x**2/2


# Hamilton equations of the HO (mass m = 1)
def oscillateur_harmonique_adim(w, t, param):
    x, p = w  # unpacking variables at time t
    omega = param  # unpacking potential parameter

    f = [p,
         -omega**2*x]
    return f


#######################################
# II-A: amplitude modulated potential #
#######################################
# Hamiltonian of the system : "amplitude modulated" (dimensionless)
def hamiltonian_amp_mod_adim(w, t, param):
    x, p = w  # unpacking variables at time t
    g, e = param  # unpacking potential parameters

    return p**2/2 - g*(1+e*cos(t)) * cos(x)


# Potential of the system : "amplitude modulated" (dimensionless)
def potential_amp_mod_adim(x, t, param):
    g, e = param  # unpacking potential parameters

    return -g*(1+e*cos(t)) * cos(x)


# Hamilton equations of the system : "amplitude modulated" (dimensionless)
def pendulum_amp_mod_adim(w, t, param):
    x, p = w  # unpacking variables at time t
    g, e = param[0]  # unpacking potential parameters

    # list of Hamilton equations
    f = [p,
         -g*(1+e*cos(t)) * sin(x)]
    return f


#################################################
# II-B: amplitude and phase modulated potential #
#################################################
# Hamiltonian of the system : "amplitude and phase modulated" (dimensionless)
def hamiltonian_amp_phase_mod_adim(w, t, param, a=1, dphi=pi/2):
    x, p = w  # unpacking variables at time t
    g, e, phi = param  # unpacking potential parameters
    phi_0 = -phi * cos(dphi)  # a dependent parameters

    return p**2/2 - g*(1+e*cos(t)) * cos(x + phi*cos(a*t+dphi) + phi_0)


# Potential of the system : "amplitude and phase modulated" (dimensionless)
def potential_amp_phase_mod_adim(x, t, param, a=1, dphi=pi/2):
    g, e, phi = param[0]  # unpacking potential parameters
    phi_0 = -phi*cos(dphi)  # a dependent parameter

    return -g*(1+e*cos(t)) * cos(x + phi*cos(a*t + dphi) + phi_0)


# Hamilton equations of the system : "amplitude and phase modulated" (dimensionless)
def pendulum_amp_phase_mod_adim(w, t, param):
    x, p = w  # unpacking variables at time t
    g, e, phi = param[0]  # unpacking potential parameters

    a, dphi = dict2kwargs(param[1])
    # explication : I use utils.dict2kwargs(dict) to upack key-word arguments passed through the serie of functions
    # (e.g. energy_minimization > resolution > rk4 > this). That has been done this way to choose the variables that
    # will be set as parameters for nelder-mead to minimize the mechanical energy after nper. More precisely, here,
    # g, e and phi are parameters nelder-mead has acces to and not a and dphi.

    phi_0 = -phi * cos(dphi)  # a dependent parameter
    # list of Hamilton equations
    f = [p,
         -g*(1+e*cos(t)) * sin(x + phi*cos(a*t+dphi) + phi_0)]
    return f
