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

def doRaicesMultiples(f, f1, f2, x, tol, niter):
    xi = x
    fxi = eval(f)
    if fxi == 0:
        print('{xi} es raiz'.format(xi=x))
        return '{xi} es raiz'.format(xi=x)
    else:
        cont = 0
        f1xi = eval(f1)
        f2xi = eval(f2)
        error = tol + 1
        det = f1xi**2 - (fxi*f2xi)
        while fxi != 0 and error > tol and cont < niter and det != 0:
            xiaux = xi
            xi = xi - ((fxi*f1xi)/(f1xi**2)-(fxi*f2xi))
            x = xi
            fxi = eval(f)
            f1xi = eval(f1)
            f2xi = eval(f2)
            error = abs(xi - xiaux)
            det = f1xi**2 - (fxi*f2xi)
            cont += 1
        if fxi == 0:
            print('{xi} es raíz'.format(xi=xi))
            return '{xi} es raíz'.format(xi=xi)
        elif error <= tol:
            print('{xi} es aproximación a una raíz con una toleracia de {tol}'.format(xi=xi, tol=tol))
            return '{xi} es aproximación a una raíz con una toleracia de {tol}'.format(xi=xi, tol=tol)
        else:
            print('Fracasó en {niter} iteraciones'.format(niter=niter))
            return 'Fracasó en {niter} iteraciones'.format(niter=niter)

f_test = 'e(x)-x-1'
f1_test = 'e(x)-1'
f2_test = 'e(x)'
x_test = 1
tol_test = 0.00001
niter_test = 15
doRaicesMultiples(f_test, f1_test, f2_test, x_test, tol_test, niter_test)