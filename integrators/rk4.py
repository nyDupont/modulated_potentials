from numpy import zeros, array


def rk4(f, y0, vect_t, *args):
    """
    rk4(f, y0, vect_t, *args, **kwargs)

    Return the solution of f, a python function one wants to integrate numerically using the Runge-Kutta 4 method.

    Parameters
    ----------
    f : python function of the system. For instance with the harmonic oscillator (HO), f is the following "oh" function:

            def oh(y, t, param):
                x, p = y
                omega = param

                g = [p,
                     -omega**2*x]
                return g

        where g is the list of the functions dx_i/dt = f({x_j}). For the HO, they are the Hamilton equations.
    y0 : tuple of floats, initial conditions (e.g. (x0, p0)),
    vect_t : time vector,
    *args : facultative parameters to be passed to the function (e.g. param for HO),
    **kwargs : keyword facultative paremeters to be passed to the function.
    """
    # results array
    y = zeros((len(vect_t), len(y0)))  # column i = solution x_i ; # lign j = [x_1(t_j), x_2(t_j), ...]
    y[0, :] = y0

    # loop to compute y_(n+1)
    for i in range(len(vect_t)-1):
        t_n, t_n1 = vect_t[i], vect_t[i+1]
        h = t_n1 - t_n  # time step, inside the loop as it can vary depending on vect_t
        y_n = y[i, :]  # y_n

        # k_i coefficients of RK4 ;
        # see https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods#The_Runge%E2%80%93Kutta_method
        k1 = h * array(f(y_n, t_n, args))
        k2 = h * array(f(y_n + k1/2, t_n + h/2, args))
        k3 = h * array(f(y_n + k2 / 2, t_n + h / 2, args))
        k4 = h * array(f(y_n + k3, t_n + h, args))

        # y_n1 = (y_n + (k1+2*k2+2*k3+k4))/6
        y[i+1, :] = y_n + (k1+2*k2+2*k3+k4)/6
    return y
