from ODE.euler_expl import euler_expl
from ODE.euler_impl import euler_impl_newton
from numpy import *

g = 9.81
l = 1
y0 = [pi/2, 0]
tspan = [0, 20]
N = 2000


def ode_pendulum(t, y):
    return array([y[1], -g/l*sin(y[0])])


def ode_pendulum_y(t, y):
    return array([[0, 1], [-g/l*cos(y[0]), 0]])


[Te, Ye] = euler_expl(ode_pendulum, tspan, y0, N)
[Ti, Yi] = euler_impl_newton(ode_pendulum, tspan, y0, N,ode_pendulum_y)



