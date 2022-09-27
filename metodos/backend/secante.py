 #* Super lineal 1,62

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

def doSecante(tol, x, x1, niter, f):
    fx0 = eval(f)
    if fx0 == 0:
        print('{x0} es una raíz'.format(x0=x))
        return '{x0} es una raíz'.format(x0=x)
    else:
        aux = x #* Auxiliar para guardar el valor de x
        x = x1 #* Para evaluar con x1 lo debemos llamar x
        fx1 = eval(f)
        x = aux
        cont = 0
        error = tol + 1
        den = fx1 - fx0
        while(error > tol and fx1 != 0 and den != 0 and cont < niter):
            x2 = x1 - ((fx1 * (x1 - x)) / (den))
            error = abs(x2-x1)
            x = x1
            fx0 = fx1
            x1 = x2
            aux = x #* Auxiliar para guardar el valor de x
            x = x1 #* Para evaluar con x1 lo debemos llamar x
            fx1 = eval(f)
            x = aux
            den = fx1 - fx0
            cont += 1
        if fx1 == 0:
            print('{x1} es raíz'.format(x1=x1))
            return '{x1} es raíz'.format(x1=x1)
        elif error < tol:
            print('{x1} es aproximación a una raíz con una toleracia de {tol}'.format(x1=x1, tol=tol))
            return '{x1} es aproximación a una raíz con una toleracia de {tol}'.format(x1=x1, tol=tol)
        elif den == 0:
            print('Hay una posible raíz multiple')
            return 'Hay una posible raíz multiple'
        else:
            print('Fracasó en {niter} iteraciones'.format(niter=niter))
            return 'Fracasó en {niter} iteraciones'.format(niter=niter)

x_test = 0
x1_test = 1
tol_test = 0.00001
niter_test = 15
#f_test = 'e(x)-5*x+2-1'
f_test = 'e(-x**2)-x'
doSecante(tol_test, x_test, x1_test, niter_test, f_test)
