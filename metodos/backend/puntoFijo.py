
#* Igualamos a 0 y luego debemos despejar x de la funcion para hallar el g(x) y
#* luego debemos encontrar la derivada de la funcion encontrada y evaluar todo intervalo en esta derivada esa es la K
#* Si todas las K dan <1 nos sirve la funcion despejada
#* Si 0.5 < K < 1 es mejor biseccion, si K = 0.5  es igual y si K < 0.5 es mejor punto fijo

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

def doPuntoFijo(tol, x, niter, g):
    x1 = eval(g)
    error = abs(x1-x)
    cont = 0
    while tol < error and cont < niter:
        x = x1
        x1 = eval(g)
        error = abs(x1-x)
        cont += 1
    if error <= tol:
        print('{x1} es punto fijo con tolerancia {tol}'.format(x1=x1, tol=tol))
        return '{x1} es punto fijo con tolerancia {tol}'.format(x1=x1, tol=tol)
    else:
        print('No se encontró solución')
        return 'No se encontró solución'

x_test = 0
tol_test = 0.001
niter_test = 15
g_test = 'e(-x)'
doPuntoFijo(tol_test, x_test, niter_test, g_test)
