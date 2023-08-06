from sympy import *
import sys
from rosignoli_lib import * 

def seleziona_polinomio(frase = "Seleziona la tipologia di polinomi."):
    # Definisco la variabile simbolica
    print(frase)
    a, b, c, d, z, x = symbols('a b c d z x')
    polinomi = ['A : Legendre', 'B : Laguerre', 'C : Hermite', 'D : Chebyschev I specie', 'E : Chebyschev II specie', 'F : Gegenbauer', 'G : inserisci il nome di una nuova classe di polinomi', 'H : Jacobi', 'I : Charlier', 'J : Kravchuk', 'K : Tricomi']
    pesi = ['A : 1', 'B : exp(- z)', 'C :  exp(- z ** 2)', 'D : 1 / (sqrt(1 - z ** 2))', 'E : sqrt(1 - z ** 2)', 'F : (1 - z ** 2) ** (a - 1/2)', 'G : inserisci il peso della nuova classe di polinomi', 'H : (1 - z) ** a * (1 + z) ** b', 'I : exp(-z)*z**a', 'J : p**z * (1-p)**y', 'K : (x * y)^(1/2) * e^(-x * y/2)']
    frase = """Ogni classe di polinomi ha il suo peso corrispondente.\n"""
    frase += '\n'.join(polinomi)
    frase += "\nLa tua scelta è: "
    sicuro = False
    while not sicuro:
        scelta = chiedi_char(frase)
        if scelta != 'G':
            polinomio = elemento_lista(scelta, polinomi)
            print("Hai scelto i polinomi di " + str(polinomio))
            peso = elemento_lista(scelta, pesi)
            print("Il peso corrispondente è w(z) = " + str(peso))
            f0 = sympify(peso)
        sicuro = chiedi_conferma("Sei sicuro della scelta effettuata? (S/N) : ")
    
    file_name = "METAPOLY.py"
    
    if scelta == "G":
        nuovo_polinomio = input("""Inserisci il nome della nuova tipologia di polinomi
Nome : """)
        polinomio = nuovo_polinomio
        nuovo_peso = input("""Inserisci un'espressione per il peso nella variabile z
w(z) = """)
        peso = nuovo_peso
        f0 = sympify(nuovo_peso)
        
        lines = read_file(file_name)
        # Trova la riga contenente la dichiarazione della variabile nuovo_polinomio
        nuovo_polinomio_line = None
        for i, line in enumerate(lines):
            if line.startswith("nuovo_polinomio ="):
                nuovo_polinomio_line = i
                break

        # Trova la riga contenente la dichiarazione della variabile nuovo_peso
        nuovo_peso_line = None
        for i, line in enumerate(lines):
            if line.startswith("nuovo_peso ="):
                nuovo_peso_line = i
                break

        if nuovo_polinomio_line is not None and nuovo_peso_line is not None:
            # Sostituisci il valore tra le virgolette con la nuova funzione nella riga corrispondente
            lines[nuovo_polinomio_line] = f'nuovo_polinomio = "{nuovo_polinomio}"\n'
            lines[nuovo_peso_line] = f'nuovo_peso = "{nuovo_peso}"\n'

            # Scrivi le righe modificate nello script 1
            with open(file_name, "w") as file:
                file.writelines(lines)
        sys.argv.append(file_name)
        exec(open(file_name).read())
        
    
    # Derivo le espressioni ricorsivamente
    f1 = diff(f0, z)
    f2 = diff(f1, z)
    f3 = diff(f2, z)

    # Genero delle funzioni con input complesso
    f = lambdify(z, f0)
    df = lambdify(z, f1)
    ddf = lambdify(z, f2)
    dddf = lambdify(z, f3)
    
    return polinomio, f, df, ddf, dddf, f0

#seleziona_polinomio()
