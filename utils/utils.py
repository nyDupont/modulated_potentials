from integrators.rk4 import rk4


# useful miscellaneous functions

# An explicit resolution function
def resolution(system, w0, vect_t, param, integrateur=rk4, **kwargs):
    w_sol = integrateur(system, w0, vect_t, param, kwargs)
    return w_sol[:, 0], w_sol[:, 1]


def dict2kwargs(dictionnary):
    possible_variables = ['a', 'b', 'c', 'd', 'dphi', 'e', 'eps', 'f', 'g', 'k', 'm', 's', 'v', 'V0']
    result = ()
    for k, v in sorted(dictionnary.items()):
        for variable in possible_variables:
            if k == variable:
                result += (v,)
    return result
