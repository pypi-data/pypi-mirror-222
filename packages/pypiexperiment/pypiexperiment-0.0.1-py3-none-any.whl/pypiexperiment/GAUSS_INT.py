import numpy as np
from sympy import *
from third import *
from SELETTORE_FUNC import *
from SELETTORE_POLY import *
from ROOTFINDER import *
from rosignoli_lib import *
from INT_SYMP import *
from GENERA_POLY import *
from scipy.integrate import quad

def arrotonda_coefficienti(polinomio, deg):
    z = Symbol('z')
    polinomio = expand(polinomio)
    polinomio_arrotondato = 0
    coeffs = []
    for i in range(deg):
        coeffs.append(round(polinomio.coeff(z, i), 10))
        polinomio_arrotondato += z ** i * coeffs[i]
    return polinomio_arrotondato
         
def lagrange_inter_poly(zeros):
    z = Symbol('z')
    polynomials = []
    deg = len(zeros)
    for i in range(deg):
        num = 1
        den = 1
        zi = zeros[i]
        for j in range(deg):
            zj = zeros[j]
            if zj != zi:
                num *= z - zj
                den *= zi - zj
        poly = num / den
        polynomials.append(arrotonda_coefficienti(poly, deg))
    return polynomials

global nome
global p
global px
global dp
global ddp
global dddp

nome, p, dp, ddp, dddp, px = seleziona_polinomio()

global f
global fx
global df
global ddf
global dddf

f, df, ddf, dddf, fx = seleziona_funzione("Seleziona il polinomio del quale vuoi calcolare l'integrale con il peso w(z) = " + str(px))

# Inserisco i parametri della ricerca degli zeri e dell'integrale
interval = []
interval.append(chiedi_numero("Inserisci l'estremo inferiore di ricerca degli zeri : "))
interval.append(chiedi_numero("Inserisci l'estremo superiore di ricerca degli zeri : "))
max_it = chiedi_numero_int("Inserisci il massimo numero di iterazioni : ")
deg = chiedi_numero_int("Qual'è il grado del polinomio che hai inserito? : ")
tol = 10**(-chiedi_numero_pos("L'accuratezza nella stima degli zeri è uguale a 10 ** -"))
interval_int = []
interval_int.append(chiedi_numero("Inserisci l'estremo inferiore di integrazione: "))
interval_int.append(chiedi_numero("Inserisci l'estremo superiore di integrazione : "))
range_int = interval_int[1] - interval_int[0]
intervals = []
a = float(interval_int[0])
b = float(interval_int[0] + range_int/5)
c = float(interval_int[0] + 2*range_int/5)
d = float(interval_int[0] + 3*range_int/5)
e = float(interval_int[0] + 4*range_int/5)
g = float(interval_int[1])
intervals.append([a, b])
intervals.append([b, c])
intervals.append([c, d])
intervals.append([d, e])

num_zeros = np.ceil((deg + 1)/2)

# Genero il polinomio

global q
global qx
global dq
global ddq
global dddq

q, dq, ddq, dddq, qx = seleziona_generatore(nome, num_zeros)
print("Ci aiuta il polinomio " + str(qx))

# Identifico le radici del polinomio

zeros = halley_gen(q, dq, ddq, interval, max_it, num_zeros, 100, tol)
zeros = [round(zero, 10) for zero in zeros]
print("Il polinomio " + str(qx) + " ha zeri " + str(zeros))

lagrange_interpolation_polynomials = lagrange_inter_poly(zeros)
print("Abbiamo calcolato i polinomi di interpolazione di Lagrange corrispondenti e sono " + str(len(lagrange_interpolation_polynomials)))

polinomi = [pol * px for pol in lagrange_interpolation_polynomials]
#print(polinomi)

integrals = []

pesi = []
for polinomio in polinomi:
    subintegral = 0
    for integration_range in intervals:
        subintegral = quad(lambdify(z, polinomio), interval_int[0], interval_int[1])[0]
        #subintegral += symp(integration_range, lambdify(z, polinomio), tol, max_it)
    #print(subintegral)
    pesi.append(subintegral)
print("Abbiamo calcolato i pesi.")

for i in range(len(zeros)):
    print("Il peso corrispondente allo zero " + str(zeros[i]) + " è uguale a " + str(pesi[i]))

integral = 0
fzeros = [f(zero) for zero in zeros]

for i in range(len(zeros)):
    integral += pesi[i] * fzeros[i]

integral = round(integral, 10)
print("L'integrale del polinomio " + str(fx) + " per il peso w(z) = " + str(px) + " nell'intervallo " + str(interval_int) + " con l'utilizzo dei polinomi di " + str(nome) + " è = " + str(integral))
