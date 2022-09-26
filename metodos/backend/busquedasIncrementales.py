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

def doBusquedasIncrementales(x, delta, niter, f):
    fx0 = eval(f)
    if fx0 == 0:
        print('{x0} es raiz'.format(x0=x))
        return '{x0} es raiz'.format(x0=x)
    else:
        x1 = x + delta
        cont = 1
        x = x1 #* Para evaluar con x1 lo debemos llamar x
        fx1 = eval(f)
        while fx0 * fx1 > 0 and cont < niter:
            x = x1
            fx0 = fx1
            x1 = x + delta
            aux = x #* Auxiliar para guardar el valor de x
            x = x1
            fx1 = eval(f)
            x = aux
            cont += 1
        if fx1 == 0:
            print('{x1} es raiz'.format(x1=x))
            return '{x1} es raiz'.format(x1=x)
        elif fx0 * fx1 < 0:
            print('hay una raiz entre {x0} y {x1}'.format(x0=x, x1=x1))
            return 'hay una raiz entre {x0} y {x1}'.format(x0=x, x1=x1)
        else:
            print('el metodo fracasó en {niter} iteraciones'.format(niter=niter))
            return 'el metodo fracasó en {niter} iteraciones'.format(niter=niter)

x_test = 4
delta_test = 1
niter_test = 100
f_test = 'e(3*x-12)+x*cos(3*x)-x**2+4'

doBusquedasIncrementales(x_test, delta_test, niter_test, f_test)
