from numpy import *


def euler_expl(f, tspan, y0, N):

    t = linspace(tspan[0], tspan[1], N+1)
    h = t[1]-t[0]
    y = array([y0])

    for i in range(1, N):
        y = append(y, [y[i-1] + h * f(t[i-1], y[i-1])],axis = 0 )
    return t, y

