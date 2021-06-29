from numpy import *


def heun(f,tspan,y0,N):
    t = linspace(tspan[0],tspan[1],N)
    y = array([y0])
    h = t[1]-t[0]

    for i in range(N):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h, y[i]+h * k1)
        append(y, [y[i]+h * (1 / 2) * (k1 + k2)], axis=0)

    return [t, y]

