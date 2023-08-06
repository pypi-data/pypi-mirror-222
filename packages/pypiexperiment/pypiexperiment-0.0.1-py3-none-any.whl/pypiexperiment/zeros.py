import numpy as np
from sympy import *
from third import *
from nr import *
from SELETTORE_FUNC import *

pr = 20

# Definizione del Metodo di N-R per individuare uno zero
def newtonMethod(x0,iterationNumber,f,df):
    print("\n\nMetodo di Newton-Raphson")
    for i in range(iterationNumber):
        delta = - float(N(f(x0),pr))/float(N(df(x0),pr))
        x0 += delta
        print("x0 = " + str(x0) + ", delta = " + str(delta) + ", i = " + str(i))
    residual=np.abs(float(N(f(x0),pr)))
    return x0, residual

risultati = []

x, y, z, f1, f2, f3, f0 = symbols('x y z f1 f2 f3 f0')
init_printing(use_unicode=True)


global f
global fx
global df
global ddf
global dddf

f, df, ddf, dddf, fx = seleziona_funzione()

prec = 10**(-chiedi_numero_pos("precisione = 10 ** -"))
x0 = chiedi_numero("Inserisci il valore della posizione x0: ")
print("Le derivate della funzione con cui lavoriamo sono situate in: ")
print("f^(1) = " + str(df) + "\nf^(2) = " + str(ddf) + "\nf^(3) = " + str(dddf))
x00 = x0
x01 = x0
x02 = x0
x000 = x0
x001 = x0
x002 = x0
val0 = True
val1 = True
val2 = True
n = 0
print("\n\nMetodo di Rosignoli/della radice cubica")
print("x0 = " + str(x0) + ", delta = " + str(0) + ", n = " + str(n))
print("\nPrimo ramo")
while (val0):
    a0 = float(N(f(x0),pr))
    a1 = float(N(df(x0),pr))
    a2 = float(N(ddf(x0),pr))
    a3 = float(N(dddf(x0),pr))
    A = 3*a2/a3
    B = 6*a1/a3
    C = 6*a0/a3
    delta = solve_t(1,A,B,C)[0]
    if np.absolute(delta) < prec:
        val0 = False
    x0 += delta
    print("x0 = " + str(x0) + ", delta = " + str(delta) + ", n = " + str(n+1))

    n += 1
    val0 = (n < 10)
    
n = 0
print("\nSecondo ramo")
while (val1):
    a0 = complex(N(f(x001),pr))
    a1 = complex(N(df(x001),pr))
    a2 = complex(N(ddf(x001),pr))
    a3 = complex(N(dddf(x001),pr))
    A = 3*a2/a3
    B = 6*a1/a3
    C = 6*a0/a3
    delta1 = solve_t(1,A,B,C)[1]
    if np.absolute(delta1) < prec:
        val1 = False
    x001 += delta1
    print("x001 = " + str(x001) + ", |delta| = " + str(abs(delta1)) + ", n = " + str(n+1))

    n += 1
    val1 = (n < 10)
    
n = 0  
print("\nTerzo ramo")
while (val2):
    a0 = complex(N(f(x002),pr))
    a1 = complex(N(df(x002),pr))
    a2 = complex(N(ddf(x002),pr))
    a3 = complex(N(dddf(x002),pr))
    A = 3*a2/a3
    B = 6*a1/a3
    C = 6*a0/a3
    delta2 = solve_t(1,A,B,C)[2]
    if np.absolute(delta2) < prec:
        val2 = False
    x002 += delta2
    print("x001 = " + str(x002) + ", |delta| = " + str(abs(delta2)) + ", n = " + str(n+1))

    n += 1
    val2 = (n < 10)

num = 10 
num_zeros = 5
solution,residual = newtonMethod(x00,num,f,df)
solution,residual = newtonMethod(2*x00,num,f,df)
solution,residual = newtonMethod(-x00,num,f,df)
zeros = nr_gen(f, df, x01, 10**(-10), num, num_zeros)
zeroz = rosign_gen(f, df, ddf, dddf, x00, prec, num, num_zeros)
print("\n\nAlgoritmo di Newton-Raphson generalizzato.\nGli zeri individuati sono:", zeros)
print("\n\nAlgoritmo della radice cubica generalizzato.\nGli zeri individuati sono:", zeroz)

print("\n\nAlgoritmo di bisezione")
a = -15.0
b = 29.0
scarto = 0.1
c = (a+b)/2.0
prog = 0
def bisezione(a, b, c, prog, scarto):
    print("Intervallo iniziale: [" + str(a) + ", " + str(b) + "] Punto medio: " + str(c))
    while abs(float(N(f(x0),pr))) > prec and prog < 10:
        print("f(" + str(c) + ") = " + str(float(N(f(x0),pr))))
        if float(N(f(x0),pr)) < 0:
            a = c
        else:
            b = c
        c = (a+b)/2
        prog += 1
        print("Nuovo int.: [" + str(a) + ", " + str(b) + "] Punto medio: " + str(c))
    return c
c = bisezione(a, b, c, prog, scarto)
print("Soluzione: x = " + str(c))
print("f(" + str(c) + ") = " + str(float(N(f(x0),pr))))

    
