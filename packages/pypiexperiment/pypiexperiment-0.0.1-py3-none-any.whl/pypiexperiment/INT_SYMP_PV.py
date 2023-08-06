import numpy as np
import scipy as s
from sympy import *
from SELETTORE_FUNC import *

global f
global fx
global df
global ddf
global dddf

# Seleziono la funzione da integrare
f, df, ddf, dddf, fx = seleziona_funzione()

def fu(z,c): # Definisco la funzione divisa per il polinomio di grado 1
    global f
    return f(z)*(z-c)**(-1)

def h(z,c): # Definisco la funzione somma simmetrica rispetto all'asintoto
    return fu(z,c)+fu(2*c-z,c)

def intg(a,b,c): 
    x = Symbol('z')
    return integrate(h(z,c),(z,a,b))

def g(a,b): # Calcolo il valore analitico dell'integrale
    global fx
    z = Symbol('z')
    return integrate(fx,(z,a,b))

# Algoritmo di integrazione di Sympson
def symp(a,b,f,eps):
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
        print("Risultato parziale = " + str(t) + " con " + str(i) + " chiamate.")
        if (abs(t-u)/t < eps) and (i > 5):
            return t, i
        i += 1

def intg(a,b,c):
    x = Symbol('x')
    return integrate(h(x,c),(x,a,b))

# Algoritmi di integrazione al PV su domini simmetrici o asimmetrici
def symp_PV_1(a,b,c,d,eps):
    s = 0
    r = 0
    t = 0
    u = 0
    n = 0
    s = .5 * (c-d-a) * (h(a,c)+h(c-d,c))
    #s = s/2 + (b-a)/2 * func((a+b)/2)
    p = 0
    i = 2
    while 1:
        u = t
        p = 0
        for j in range(0,2**(i-2),1):
            x = (2*j+1)*(a+c-d)/(2**(i-1))
            p += h(x,c)
        r = s
        s = s/2 + p*((a+c-d)/(2**(i-1)))
        t = (4*s-r)/3
        if (abs(t-u)/t < eps) and (i > 5):
            return t, i
        i += 1

def symp_PV_2(a,b,c,d,eps):
    s = 0
    r = 0
    t = 0
    u = 0
    n = 0
    s = .5 * (b-c-d) * (h(c+d,c)+h(b,c))
    #s = s/2 + (b-a)/2 * func((a+b)/2)
    p = 0
    i = 2
    while 1:
        u = t
        p = 0
        for j in range(0,2**(i-2),1):
            x = (2*j+1)*(b+c+d)/(2**(i-1))
            p += h(x,c)
        r = s
        s = s/2 + p*((b+c+d)/(2**(i-1)))
        t = (4*s-r)/3
        if (abs(t-u)/t < eps) and (i > 5):
            return t, i
        i += 1

# Funzione di decisione dell'intervallo : simmetrico / asimmetrico
def int_PV(a,b,c,d,eps):
    integ = 0
    numcalls = 0
    result_PV = [integ, numcalls]
    if (c-a < b-c):
        print("First case a--c----b")
        result_PV = symp_PV_1(a,b,c,d,eps)
        result_PV = [x + y for x, y in zip(result_PV, symp(2*c-a,b,f,eps))]
    elif (c-a > b-c):
        print("Second case a----c--b")
        result_PV = symp_PV_2(a,b,c,d,eps)
        result_PV = [x + y for x, y in zip(result_PV, symp(a,2*c-b,f,eps))]
    else:
        print("Symmetrical case a---c---b")
        result_PV = symp_PV_1(a,b,c,d,eps)
    return result_PV


# Inserisco i parametri dell'integrale
eps = 10**(-2) # tolleranza
a = chiedi_numero("Inserisci l'estremo inferiore: ")
b = chiedi_numero("Inserisci l'estremo superiore: ")
c = chiedi_numero("Se la funzione fosse divisa per (x-c), quanto sarebbe c? ")
d = 10**(chiedi_numero_neg("Qual'è l'esponente negativo di 10 dello scostamento d dall'asintoto verticale? "))
x, numcalls = symp(a,b,f,eps)
x_PV, numcalls_PV = int_PV(a,b,c,d,eps)

print("Approssimazione con Sympson = " + str(x) + ", valore analitico = " + str(simplify(g(a,b))) + "\ncon " + str(numcalls) + " chiamate della funzione.")
print("L'integrale al PV ha valore = " + str(x_PV) + ", ha una precisione di " + str(eps) + "\ncon " + str(numcalls_PV) + " chiamate della funzione.")




