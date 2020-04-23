from integrators.rk4 import rk4

# useful miscellaneous functions


def resolution(system, w0, vect_t, param, integrator=rk4):
    """
    resolution(system, w0, vect_t, param, integrateur=rk4)

    An explicit resolution function of a system of 2 coupled differential equations dx_i/dt = f{xi}, here restrained to
    i = 0 or 1. Returns a tuple of 2 vertical 1d arrays, namely x_0(t) and x_1(t).

    Parameters
    ----------
    system: a python function written as the ones integrators/rk4.py or odeint accepts, i.e.
            f((x_i), vect_t, param) = [dx_i/dt], where each dx_i/dt depends the x_i, parameters of param (see below) and
            eventually time of vect_t. (see integrators.rk4.py, or examples of systems in utils.physics_systems.py
    w0: tuple of initial conditions on (x_i). Must be countain 2 elements.
    vect_t: time vector along which the system must be integrated.
    param: tuple of all the parameters needed to define system (e.g. the pulsation omega is system =
           harmonic_oscillator).
    integrator: a python function, the numerical integrator to solve the system ; integrators/rk4.py by default.
    """
    w_sol = integrator(system, w0, vect_t, param)
    return w_sol[:, 0], w_sol[:, 1]


def decimals(x, n, trunc=False):
    """
    decimals(x, n, trunc=False)

    Takes a float and returns it rounded with n decimals.

    Parameters
    ----------
    x: float
    n: int
    trunc: boolean, to be set to True if one wants x to be returned truncated and not rounded.
    """
    if trunc:
        return int(10**n*x)/10**n
    else:
        return round(10**n*x)/10**n
