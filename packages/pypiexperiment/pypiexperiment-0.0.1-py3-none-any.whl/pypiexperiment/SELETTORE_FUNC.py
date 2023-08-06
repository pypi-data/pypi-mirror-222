from sympy import *
import sys
from rosignoli_lib import *


def seleziona_funzione(frase = "Seleziona la funzione."):
    # Definisco la variabile simbolica
    print(frase)
    a, b, c, d, z, x = symbols('a b c d z x')
    funzioni = ['A : z**4 - 1', 'B : z**6 + z**4 - 1', 'C : z - z**3/(3*2) + z**5/(5*4*3*2) - z**7/(7*6*5*4*3*2) + z**9/(9*8*7*6*5*4*3*2)', 'D : cos(z**3) - z**2 + 2*z**3', 'E : z**3 - 3*z**2 + z + 1', 'F : z**5/5 - z**3/3 + z**2/2 - 1/2', 'G : inserisci la tua funzione', 'H : sin(sin(z))', 'I : z**4+z**5-z**3', 'J : z**(3+z)-sqrt(z)', 'K : z**37', 'L : z**z', 'M : z**6-z**5+z**4-3', 'N : sqrt(1-z**2)', 'O : (z-1)**2', 'P : (z-1)*(z-1.75)*(z-2.5)', 'Q : sin(z)', 'R : (1/2)*(z**2 - 4*z + 2)', 'S : e**(-z**2)', 'T : 0.8333333334*z**2 - 0.6454972244*z', 'U : 1.0 - 1.6666666668*z**2', 'V : 8*z**4 - 8*z**2 + 1', 'W : z**16/128 - z**14/64 + 3*z**13 + z**7 - z**5 - .001']
    frase = """Seleziona la funzione utile.\n"""
    frase += '\n'.join(funzioni)
    frase += "\nLa tua scelta è: "
    scelta = chiedi_char(frase)
    file_name = "METAFUNC.py"
    if scelta == "G":
        nuova_funzione = input("""Inserisci un'espressione per la funzione nella variabile z
f(z) = """)
        f0 = sympify(nuova_funzione)
        
        lines = read_file(file_name)
        # Trova la riga contenente la dichiarazione della variabile nuovo_frutto
        nuova_funzione_line = None
        for i, line in enumerate(lines):
            if line.startswith("nuova_funzione ="):
                nuova_funzione_line = i
                break

        if nuova_funzione_line is not None:
            # Sostituisci il valore tra le virgolette con la nuova funzione nella riga corrispondente
            lines[nuova_funzione_line] = f'nuova_funzione = "{nuova_funzione}"\n'

            # Scrivi le righe modificate nello script 1
            with open(file_name, "w") as file:
                file.writelines(lines)
        sys.argv.append(file_name)
        exec(open(file_name).read())
    else:    
        for funzione in funzioni:
            if scelta.upper() in funzione:
                funzione = funzione.split(":")[1].strip()
                break
        f0 = sympify(funzione)
    
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
