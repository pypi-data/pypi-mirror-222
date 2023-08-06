import numpy as np
from sympy import *
from third import *
from SELETTORE_FUNC import *

pr = 20

def halley(f, df, ddf, x):
    d = - 2 * f(x) * df(x) / (2 * df(x) ** 2 - f(x) * ddf(x))
    return d

def halley_find(f, df, ddf, x0, tol, max_it, zeros):
    n = 0
    while n < max_it:
        delta = halley(f, df, ddf, x0)
        if abs(delta) <= tol and abs(f(x0)) < tol:
            if not any(abs(zero-x0) <= tol for zero in zeros):
                zeros.append(N(x0,pr))
            x0 += .1
        x0 += delta
        n += 1
    return zeros

def halley_gen(f, df, ddf, interval, max_it, num_zeros, fin, tol = 10**(-5)):
    i = 0
    val = True
    zeros = []
    x0 = interval[0]
    width = interval[1] - interval[0]
    step = width / fin
    while len(zeros) < num_zeros and val:
        zeros += [N(num,pr/2) for num in halley_find(f, df, ddf, x0, tol, max_it, zeros) if num not in zeros]
        x0 += step
        i += 1
        val = (i<100)
    return zeros

"""
global f
global fx
global df
global ddf
global dddf

f, df, ddf, dddf, fx = seleziona_funzione("Scegli la funzione della quale vuoi trovare gli zeri")
interval = []
interval.append(chiedi_numero("Inserisci l'estremo inferiore di ricerca : "))
interval.append(chiedi_numero("Inserisci l'estremo superiore di ricerca : "))
max_it = chiedi_numero_int("Inserisci il massimo numero di iterazioni : ")
num_zeros = chiedi_numero_int("Quanti zeri della funzione vuoi individuare? : ")
tol = 10**(-chiedi_numero_pos("L'accuratezza è uguale a 10 ** -"))
print(halley_gen(f,df,ddf, interval, max_it, num_zeros, 100, tol))
"""
