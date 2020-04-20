from numpy import linspace
from utils.physics_systems import *
from utils.utils import resolution
from utils.math_functions import asig_sampling


def phase_space(system, param, xmin, xmax, pmin, pmax, nx, np, nper,
                ndt=200, integrator=rk4, xmodulo=None, pmodulo=None,
                sampling='rect', sampling_density='const', sampling_amp=1):
    """
    phase_space(system, param, xmin, xmax, pmin, pmax, nx, np, nper, ndt=200, integrator=rk4, xmodulo=None,
                pmodulo=None, sampling='rect', sampling_density='const', sampling_amp=1)

    Return a tuple of two numpy arrays x and p to be plotted in a phase space (PS). Both are of shape
    (nx*np, nper*ndt).

    Parameters
    ----------
    system : function the integrator will numerically solve. Has to be previously defined returning Hamilton equations
             in my case,
    param : tuple of param passed to the system (e.g. the frequency omega if system is the harmonic oscillator),
    xmin, xmax, pmin, pmax : floats bounding the rectangular sampling of initial conditions (IC) of the PS,
    nx, np : ints of how many IC are to be computed along x- and p-axis,
    nper : int, number of periods of modulation to check,  |  This has been programmed to obtain the PS of a system
    ndt : step times by periods,                           |  modulated in time. Anyway, for each IC, simulation
                                                           |  is of duration (nper*2*pi) and (nper*ndt) discretized.
    integrator : function, numerical integrator to be used,
                (i.e. the angle of the Poincaré section intersecting the phase space torus in the (x, p, t) space.)
    xmodulo, pmodulo : floats to be specified if one wants to fold the PS on itself, for instance when the system is
                       xmodulo-periodic in x and/or pmodulo-periodic in p (i.e. invariant by such discrete translations)
                       along those axis, Note: has not yet been implemented along the p-axis.
    sampling : string, o
    sampling_density : string, to switch from a constant sampling density to a arc-sigmoidal sampling density, getting
                       more CI arround the center of the PS. Options are ['const', 'asig'],
    sampling_amp : weight of that irregular non rectangular sampling. The smaller it is, the more regular the sampling
                   is.

    About x and p returned by the function : the first dimension is the number of initial conditions computed and the
    second dimension is the common length of each trajectory.
    """
    # defining the time vector
    tmax = nper * 2 * pi
    vect_time = linspace(0, tmax, nper*ndt)

    if sampling_density == 'asig':
        vect_x = asig_sampling(linspace(xmin, xmax, nx), amp=sampling_amp)
        vect_p = asig_sampling(linspace(pmin, pmax, np), amp=sampling_amp)
    else:
        vect_x = linspace(xmin, xmax, nx)
        vect_p = linspace(pmin, pmax, np)
    # computing the trajectories, solutions of the diff. eq. (DE) for each IC
    index_x = 0
    if sampling == 'diag':
        xtot, ptot = zeros((nx, int(nper * ndt))), zeros((np, int(nper * ndt)))
        for x_0i in vect_x:
            if sampling == 'diag':
                p_0i = vect_p[index_x]
                print('{}/{}'.format(index_x+1, nx))
                wsol = resolution(system, (x_0i, p_0i), vect_time, param, integrateur=integrator)
                if xmodulo is not None:
                    xtot[index_x, :] = \
                        [((x_j + 0.5 * xmodulo) % xmodulo) - 0.5 * xmodulo for x_j in wsol[0]]
                else:
                    xtot[index_x, :] = wsol[0]
                ptot[index_x, :] = wsol[1]
                index_x += 1
    elif sampling == 'rect':
        xtot, ptot = zeros((nx * np, int(nper * ndt))), zeros((np * nx, int(nper * ndt)))
        for x_0i in vect_x:
            index_p = 0
            for p_0i in vect_p:
                progression = index_p + index_x*np
                print('{}/{}'.format(progression, nx*np))
                # numerical integration for a IC (x_0i, p_0i)
                wsol = resolution(system, (x_0i, p_0i), vect_time, param, integrateur=integrator)
                # gathering results in the same cell if the system is xmodulo-periodic along the x-axis
                if xmodulo is not None:
                    xtot[progression, :] = \
                        [((x_j+0.5*xmodulo) % xmodulo) - 0.5*xmodulo for x_j in wsol[0]]
                else:
                    xtot[progression, :] = wsol[0]
                ptot[progression, :] = wsol[1]
                index_p += 1
            index_x += 1
    return xtot, ptot


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
    """

    return x[:, t0*strob_step::strob_step], p[:, t0*strob_step::strob_step]
