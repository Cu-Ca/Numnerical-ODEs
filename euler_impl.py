from numpy import *


def euler_impl_newton(f,tspan,y0,N,fy):
    ny = len(y0)
    t = linspace(tspan[0], tspan[1], N+1)
    y = array([y0])
    maxit = 100
    tol = 1e-8
    h = t[1]-t[0]

    for i in range(1, N):
        y = append(y, [y[i-1]],axis = 0)
        dy = ones((1, ny))
        for j in range(maxit):
            dy = -1*linalg.solve(
                identity(ny)-h*fy(t[i], y[i]),
                y[i]-y[i-1]-h*f(t[i], y[i])
                )
            y[i] = y[i]+dy
            if linalg.norm(dy)<tol:
                break
    return t,y


