from numpy import e, log, array, linspace

# MATHEMATICS #


def affine(x, a, b):  # affine function for linear regression
    return a * x + b


def sig(x, lam=1, amp=1, x0=0):  # sigmoid
    return amp / (1 + e ** (-lam * (x - x0)))


def asig(x, lam=1., amp=1., x0=0.):  # inverse sigmoid for non uniform sampling of the phase space
    return log((x - x0) / (amp - (x - x0))) / lam


def asig_sampling(vect, amp=1.):  # non uniform inverse-sigmoidal sampling of the phase space
    v_i, v_f, lenght_vect = vect[0], vect[-1], len(vect)
    x = linspace((1 - amp) / 2 + 1e-3, (1 + amp) / 2 - 1e-3, lenght_vect)  # as asig : ]0;1[ -> R
    asig_scaled_offset = asig(x) / 2 / max(asig(x)) + 0.5  # new asig : ]0;1[ -> [0, 1]

    return array([v_i + (v_f - v_i) * i for i in asig_scaled_offset])


# def true_div(a, b):
# super sketchy
#     c = []
#     for i in range(len(a)):
#         if a[i] == 0 and b[i] == 0:
#             c.append(1)
#         else:
#             c.append(a[i]/b[i])
#     return array(c)
