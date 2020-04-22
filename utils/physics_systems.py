from numpy import sin, cos

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
def harmonic_oscillator_adim(w, t, param):
    x, p = w  # unpacking variables at time t
    omega = param  # unpacking potential parameter

    f = [p,
         -omega**2*x]
    return f


######################################
# I: constant cosinusoidal potential #
######################################
# Hamilton equations of the simple pendulum (mass m = 1, cord length = 1)
def simple_pendulum(w, t, param):
    x, p = w  # unpacking variables at time t
    k = param[0]  # unpacking potential parameter

    f = [p,
         -k**2*sin(x)]
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
def hamiltonian_amp_phase_mod_adim(w, t, param):
    x, p = w  # unpacking variables at time t
    g, e, phi, a, dphi = param  # unpacking potential parameters
    phi_0 = -phi * cos(dphi)  # a dependent parameters

    return p**2/2 - g*(1+e*cos(t)) * cos(x + phi*cos(a*t+dphi) + phi_0)


# Potential of the system : "amplitude and phase modulated" (dimensionless)
def potential_amp_phase_mod_adim(x, t, param):
    g, e, phi, a, dphi = param  # unpacking potential parameters
    phi_0 = -phi*cos(dphi)  # a dependent parameter

    return -g*(1+e*cos(t)) * cos(x + phi*cos(a*t + dphi) + phi_0)


# Hamilton equations of the system : "amplitude and phase modulated" (dimensionless)
def pendulum_amp_phase_mod_adim(w, t, param):
    x, p = w  # unpacking variables at time t
    g, e, phi, a, dphi = param[0]  # unpacking potential parameters

    phi_0 = -phi * cos(dphi)  # a dependent parameter
    # list of Hamilton equations
    f = [p,
         -g*(1+e*cos(t)) * sin(x + phi*cos(a*t+dphi) + phi_0)]
    return f


def force_pendulum_amp_phas_mod_adim(x, t, param):
    g, e, phi, a, dphi = param  # unpacking potential parameters
    phi_0 = -phi * cos(dphi)  # a dependent parameter

    return -g * (1 + e*cos(t)) * sin(x + phi*cos(a*t+dphi) + phi_0)
