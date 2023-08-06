import sys
import importlib.util
from rosignoli_lib import *

            
file_name = "SELETTORE_FUNC.py"
file_input = file_name
lines = read_file(file_name)
funzioni_importate = leggi_lista_da_file(file_name, "funzioni")

nuova_funzione = "z**16/128 - z**14/64 + 3*z**13 + z**7 - z**5 - .001"

new_letter = find_next_uppercase_letter(funzioni_importate)
funzioni_importate = [elemento.strip('\'"') for elemento in funzioni_importate]
funzioni_importate.append(f"{new_letter} : {nuova_funzione}")

cancella_righe_lista(file_name, "funzioni")

linea_da_trovare = 'a, b, c'  # La linea da trovare nel file che inizia con 'print("Q"'
lista_da_scrivere = funzioni_importate  # La lista da scrivere alla linea successiva

scrivi_lista_linea_successiva(file_input, linea_da_trovare, lista_da_scrivere, 'funzioni')







