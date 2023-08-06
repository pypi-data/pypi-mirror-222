from sympy import *
import sys
from rosignoli_lib import *


def seleziona_generatore(nome, n):
    # Definisco la variabile simbolica
    a, b, c, d, z, x = symbols('a b c d z x')
    classi_polinomi = ['A : Legendre', 'B : Laguerre', 'C : Hermite', 'D : Chebyschev I specie', 'E : Chebyschev II specie', 'F : Gegenbauer', 'G : no add', 'H : Jacobi', 'I : Charlier', 'J : Kravchuk', 'K : Tricomi']
    generatori = ['A : legendre(n, z)', 'B : (exp(z) / (fattoriale(n)) * diff(exp(- z)*z**n, z, n))', 'C : hermite_poly(n, z)', 'D : chebyshevt(n, z)', 'E : chebyshevu(n, z)', 'F : ', 'G : no add', 'H : ', 'I : ', 'J : ', 'K : ']

    lettera = elemento_lettera(nome, classi_polinomi)
    generatore = elemento_lista(lettera, generatori)
    f0 = eval(generatore)

    # Derivo le espressioni ricorsivamente
    f1 = diff(f0, z)
    f2 = diff(f1, z)
    f3 = diff(f2, z)

    # Genero delle funzioni con input complesso
    f = lambdify(z, f0)
    df = lambdify(z, f1)
    ddf = lambdify(z, f2)
    dddf = lambdify(z, f3)
    
    return f, df, ddf, dddf, f0

#seleziona_generatore('Chebyschev I specie', 20)
