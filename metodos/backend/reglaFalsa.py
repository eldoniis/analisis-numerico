import numpy as np
from math import sqrt

def cos(x):
    return np.cos(x)
def sin(x):
    return np.sin(x)
def tan(x):
    return np.tan(x)
def e(x):
    return np.exp(x)
def ln(x):
    return np.log(x)

def doReglaFalsa(x, xs, tol, niter, f):
    fxi = eval(f)
    aux = x
    x = xs #* Para evaluar con xs lo debemos llamar x
    fxs = eval(f)
    x = aux
    if fxi == 0:
        print('{xi} es raiz'.format(xi=x))
        return '{xi} es raiz'.format(xi=x)
    elif fxs == 0:
        print('{xs} es raiz'.format(xs=xs))
        return '{xs} es raiz'.format(xs=xs)
    elif fxi * fxs < 0:
        xm = (x) - ((fxi * (x - xs)) / (fxi - fxs))
        aux = x #* Auxiliar para guardar el valor de x
        x = xm #* Para evaluar con xm lo debemos llamar x
        fxm = eval(f)
        x = aux
        cont = 1
        error = tol + 1
        while error > tol and fxm != 0 and cont < niter:
            if (fxi * fxm) < 0:
                xs = xm
                fxs = fxm
            else:
                x = xm
                fxi = fxm
            x_aux = xm
            xm = xm = (x) - ((fxi * (x - xs)) / (fxi - fxs))
            aux = x #* Auxiliar para guardar el valor de x
            x = xm #* Para evaluar con xm lo debemos llamar x
            fxm = eval(f)
            x = aux
            error = abs(xm - x_aux)
            cont += 1
        if xm == 0:
            print('{xm} es raiz'.format(xm=xm))
            return '{xm} es raiz'.format(xm=xm)
        elif error < tol:
            print('{xm} es una aproximacion a una raiz con una tolerancia igual a {tol}'.format(xm=xm, tol=tol))
            return '{xm} es una aproximacion a una raiz con una tolerancia igual a {tol}'.format(xm=xm, tol=tol)
    else:
        print('El intervalo es inadecuado')
        return 'El intervalo es inadecuado'

x_test = 2
xs_test = 3
tol_test = 0.5*10**-3
niter_test = 11
f_test = 'e(3*x-12)+x*cos(3*x)-(x**2)+4'
doReglaFalsa(x_test, xs_test, tol_test, niter_test, f_test)
