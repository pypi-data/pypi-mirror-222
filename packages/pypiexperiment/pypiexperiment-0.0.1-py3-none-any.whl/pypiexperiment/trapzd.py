import numpy as np
import scipy as s
#from INT_SYMP_PV import *
from sympy import *

def trapzd(a, b, s, n, jcount, func):
    l = b-a
    it = 0
    icount = 0
    _sum = 0
    if(n==1):
        s = .5 * (b-a) * (func(a) + func(b))
        icount = 2
    else:
        it = 2**(n-2)
        tnm = it
        _del = l / tnm
        x = a + 0.5 * _del
        for j in range(1, it, 1):
            _sum += func(x)
            x += _del
            s = .5 * ( s + l * _sum / tnm )
            icount += it
    return s, icount
    



