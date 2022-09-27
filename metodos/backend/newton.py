
#* Es conocido como el metodo de las tangentes
#* Solo garantiza en multiplicidad 1 que la convergencia sea cuadratica

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


def doNewton(tol, x, niter, df, f):
    x1 = x - (eval(f)/eval(df))
    error = abs(x1-x)
    cont = 0
    while tol < error and cont < niter: 
        x = x1
        x1 = x - (eval(f)/eval(df))
        error = abs(x1-x)
        cont += 1
    if error <= tol:
        print('{x1} aproximación a una raíz con una tolerancia {tol}'.format(x1=x1, tol=tol))
        return '{x1} aproximación a una raíz con una tolerancia {tol}'.format(x1=x1, tol=tol)
    else:
        print('No se encontró solución')
        return 'No se encontró solución'

x_test = 0
tol_test = 0.001
niter_test = 15
#f_test = 'e(-x)-x'
f_test = 'x**2-2*x+2-e(x)'
fDerivada_test = '2*x-2-e(x)'
doNewton(tol_test, x_test, niter_test, fDerivada_test, f_test)
