from numpy import *


def rungekutta(f, tspan, y0, N):
    t = linspace(tspan[0], tspan[1], N)
    y = array([y0])
    h = t[1] - t[0]

    for i in range(1,N):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + 1 / 2 * h, y[i]+1 / 2 * h * k1)
        k3 = f(t[i] + 1 / 2 * h, y[i]+1 / 2 * h * k2)
        k4 = f(t[i] + h, y[i]+h * k1)

    append(y,[y[i] + (1/6*k1+1/3*k2+1/3*k3+1/6*k4)])

    return [t, y]
