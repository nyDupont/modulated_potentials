from numpy import linspace, zeros
from random import random
from integrators.rk4 import rk4
from utils.utils import resolution


def phase_space(system, param, vect_ic, vect_t, integrator=rk4, xmodulo=None, pmodulo=None):
    """
    phase_space(system, param, vect_ic, nper, ndt=200, integrator=rk4, xmodulo=None, pmodulo=None)

    Return a tuple of two numpy arrays x and p to be plotted in a phase space (PS). Both are of shape
    (nx*np, nper*ndt).

    Parameters
    ----------
    system : function the integrator will numerically solve. Has to be previously defined returning Hamilton equations
             in my case,
    param : tuple of param passed to the system (e.g. the frequency omega if system is the harmonic oscillator),
    vect_ic : python iterable of tuples (x_i, p_i), the set of initial conditions under which the trajectories will be
              plotted,
    vect_t : python iterable, being the time vector along |  This has been programmed to obtain the PS of a system
             which the system is integrated,              |  modulated in time. Anyway, for each IC, simulation
                                                          |  is of duration (nper*2*pi) and (nper*ndt) discretized.
    integrator : function, numerical integrator to be used,
    xmodulo, pmodulo : floats to be specified if one wants to fold the PS on itself, for instance when the system is
                       xmodulo-periodic in x and/or pmodulo-periodic in p (i.e. invariant by such discrete translations)
                       along those axis, Note: yet to be implemented along the p-axis.

    About x and p returned by the function : the first dimension is the number of initial conditions computed and the
    second dimension is the common length of each trajectory.
    """
    n_ic = len(vect_ic)
    n_t = len(vect_t)
    # computing the trajectories, solutions of the diff. eq. (DE) for each IC
    progression = 0
    xtot, ptot = zeros((n_ic, n_t)), zeros((n_ic, n_t))
    for ic in vect_ic:
        print('computing initial condition {}/{}...'.format(progression + 1, n_ic))
        # numerical integration for a IC (x_0i, p_0i)
        wsol = resolution(system, (ic[0], ic[1]), vect_t, param, integrator=integrator)
        # gathering results in the same cell if the system is xmodulo-periodic along the x-axis
        if xmodulo is not None:
            xtot[progression, :] = modulo_zcentered(wsol[0], xmodulo)
        else:
            xtot[progression, :] = wsol[0]
        ptot[progression, :] = wsol[1]
        progression += 1
    return xtot, ptot


def rect_sampling(xmin, xmax, pmin, pmax, nx, np):
    x, p = linspace(xmin, xmax, nx), linspace(pmin, pmax, np)
    res = []
    for i in x:
        for j in p:
            res.append((i, j))
    return res


def rand_sampling(xmin, xmax, pmin, pmax, n):
    res = []
    dx, dp = xmax-xmin, pmax-min
    for i in range(n):
        x, p = xmin+random()*dx, pmin+random()*dp
        res.append((x, p))
    return res


def modulo_zcentered(vect, modulo):
    """
    Modulo zero centered : modulo_zcentered(vect, modulo)

    Return vect folded on itself, centered around zero and with periodicity modulo

    Parameters
    ----------
    vect: iterable to fold
    modulo: float, desired periodicity
    """
    return [((element+0.5*modulo) % modulo)-0.5*modulo for element in vect]


def stroboscopic(x, p, strob_step, t0=0):
    """
    stroboscopic(x, p, strob_step, t0=0)

    Return a tuple of two numpy arrays x and p to be plotted in a stroboscopic phase space (SPS) of a 1d system. Both
    are of shape (nx*np, j), where j is either (nper*ndt/strob_step) either (nper*ndt/strob_step - 1) if t0 > 0 (see
    below).

    Parameters
    ----------
    x, p: two numpy arrays. Their first dimension is the number of trajectories they contain (i.e. the number of initial
          condition computed) and the second dimension is the common length of each trajectory (i.e. the length of the
          time vector).
    strob_step: an integer stating the frequency at trajectories must be reported on the SPS. To observe stroboscopical-
                ly the dynamics of a system modulated in time, and with a time vector looking like
                t = numpy.linspace(t0, tf, ndt*tf) going from t0 to tf periods with ndt the number of time step by
                periods, strob_step should be ndt
    t0: a float, the starting point of the stroboscopic observation as a fraction of strob_step : 0 <= t0 < 1
        (i.e. the angle of the Poincaré section intersecting the phase space torus in the (x, p, t) space.)
    """
    return x[:, round(t0*strob_step)::round(strob_step)], p[:, round(t0*strob_step)::round(strob_step)]
