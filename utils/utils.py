from integrators.rk4 import rk4


# useful miscellaneous functions

# An explicit resolution function
def resolution(system, w0, vect_t, param, integrateur=rk4):
    w_sol = integrateur(system, w0, vect_t, param)
    return w_sol[:, 0], w_sol[:, 1]
