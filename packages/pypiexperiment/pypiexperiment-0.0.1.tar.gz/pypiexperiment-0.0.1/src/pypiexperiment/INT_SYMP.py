import numpy as np
import scipy as s
from sympy import *
from SELETTORE_FUNC import *

# Algoritmo di integrazione di Sympson
def symp(interval, f, eps, max_it):
    a = interval[0]
    b = interval[1]
    s = 0
    r = 0
    t = 0
    u = 0
    n = 0
    s = .5 * (b-a) * (f(a)+f(b))
    #s = s/2 + (b-a)/2 * func((a+b)/2)
    p = 0
    i = 2
    while 1:
        u = t
        p = 0
        for j in range(0,2**(i-2),1):
            x = (2*j+1)*(a+b)/(2**(i-1))
            p += f(x)
        r = s
        s = s/2 + p*((a+b)/(2**(i-1)))
        t = (4*s-r)/3
        if (abs(t-u)/t < eps) and (i > 5) or (i > max_it):
            return t
        i += 1



