
#* Multiplicidad 0: Si al evaluar la funcion sin derivar nos da diferente de 0, si da uno sacamos derivada y seguimos
#* Multiplicidad 1: Si da diferente de 0 es multipliidad 1, si da 0 repetimos proceso
#* (x-3)^4(x+4)^2(x-2)(x^2+x+1)
#* En x=3 tiene multiplicidad 4
#* En x=-4 tiene multiplicidad 2
#* En x=2 tiene una raiz simple

import numpy as np
import math 
from math import sqrt, inf

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


def doRaicesMultiples(f,f1, f2,x0,tol,niter):

    #se inicializa los valores iniciales
    x = x0
    fun = f
    func = eval(fun)
    fun_prima = f1
    func_prima = eval(fun_prima)
    fun_2prima = f2
    func_2prima = eval(fun_2prima)
    error = math.inf

    for i in range(niter):
        if error <= tol:
           break
        error = abs(x)
        x = x - (func * func_prima) / ( (func_prima**2) - (func * func_2prima))

        fun = f
        func = eval(fun)
        fun_prima = f1
        func_prima = eval(fun_prima)
        fun_2prima = f2
        func_2prima = eval(fun_2prima)
        error = abs(error-x)

    print("Aproximación de la raiz en {x}".format(x=x))
    return "Aproximación de la raiz en {x}".format(x=x)


f_test = 'e(x)-x-1'
f1_test = 'e(x)-1'
f2_test = 'e(x)'
x_test = 1
tol_test = 10**-5
niter_test = 50
doRaicesMultiples(f_test, f1_test, f2_test, x_test, tol_test, niter_test)
