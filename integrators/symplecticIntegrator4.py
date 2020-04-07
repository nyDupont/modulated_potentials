from numpy import zeros
# by Gabriel Chatelain


def symplecticIntegrator4(t, F, x0p0, params):
    # 4th order symplectic integrator coefficients
    c = [1 / (2 * (2 - 2**(1 / 3))),
         (1 - 2**(1 / 3)) / (2 * (2 - 2**(1 / 3))),
         (1 - 2**(1 / 3)) / (2 * (2 - 2**(1 / 3))),
         1 / (2 * (2 - 2**(1 / 3)))]

    d = [1 / (2 - 2**(1 / 3)),
         -2**(1 / 3) / (2 - 2**(1 / 3)),
         1 / (2 - 2**(1 / 3)),
         0]

    X, P = x0p0
    x, p = zeros([t.size]), zeros([t.size])
    dt = t[1] - t[0]
    for i in range(t.size):
        x[i] = X
        p[i] = P
        for ind in range(4):
            if i > 0:
                X += c[ind] * p[i] * dt
                P += d[ind] * F((x[i], t[i], *params)) * dt
    return x, p
