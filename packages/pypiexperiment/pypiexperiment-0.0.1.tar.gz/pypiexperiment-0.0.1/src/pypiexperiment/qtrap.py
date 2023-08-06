import scipy as s
import numpy as np
#from INT_SYMP_PV import *
from trapzd import *
from SELETTORE_FUNC import *

global f
global fx
global df
global ddf
global dddf

f, df, ddf, dddf, f_expr = seleziona_funzione()

def qtrap(a,b,s,eps,jmax,ncalls,f):
    olds = 10**(-7)
    jcount = 0
    for j in range(1, jmax, 1):
        olds = s
        s, jcount = trapzd(a,b,s,j,jcount,f)
        if (jcount > 2) : print("The sum is ", s, "While the number of calls is ", jcount)
        if(jcount > 100):
            if((abs(s-olds) < eps*abs(olds)) or (s == 0 and olds == 0)):
                return s, jcount
            else:
                return olds, jcount
    print('too many steps in qtrap')


# Inserisco i parametri dell'integrale
eps = 10**(chiedi_numero_pos("Accuratezza = 10 eleavato alla -"))
a = chiedi_numero("Inserisci l'estremo inferiore: ")
b = chiedi_numero("Inserisci l'estremo superiore: ")
x, numcalls = qtrap(a,b,0,eps,10**6,1,f)

print("Approssimazione con il trapezio = " + str(x) + "\ncon " + str(numcalls) + " chiamate della funzione.")

