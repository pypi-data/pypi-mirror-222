import sys
import importlib.util
from rosignoli_lib import *

#    polinomi = ['A : Legendre', 'B : Laguerre', 'C : Hermite', 'D : Chebyschev I specie', 'E : Chebyschev II specie', 'F : Gegenbauer', 'G : inserisci il nome di una nuova classe di polinomi', 'H : Jacobi']
#    pesi = ['A : 1', 'B : e ** (- z)', 'C :  e ** (- z ** 2)', 'D : 1 / (sqrt(1 - z ** 2))', 'E : sqrt(1 - z ** 2)', 'F : (1 - z ** 2) ** (a - 1/2)','G : inserisci il peso della nuova classe di polinomi', 'H : (1 - z) ** a * (1 + z) ** b']

    
file_name = "SELETTORE_POLY.py"
lines = read_file(file_name)

polinomi_importati = leggi_lista_da_file(file_name, "polinomi")
pesi_importati = leggi_lista_da_file(file_name, "pesi")

nuovo_polinomio = "Tricomi"
nuovo_peso = "(x * y)^(1/2) * e^(-x * y/2)"

new_letter = find_next_uppercase_letter(polinomi_importati)
polinomi_importati = [elemento.strip('\'"') for elemento in polinomi_importati]
polinomi_importati.append(f"{new_letter} : {nuovo_polinomio}")

new_letter = find_next_uppercase_letter(pesi_importati)
pesi_importati = [elemento.strip('\'"') for elemento in pesi_importati]
pesi_importati.append(f"{new_letter} : {nuovo_peso}")

cancella_righe_lista(file_name, "polinomi")
cancella_righe_lista(file_name, "pesi")

linea_da_trovare = 'a, b, c'  # La linea da trovare nel file che inizia con 'print("Q"'
lista_da_scrivere = polinomi_importati  # La lista da scrivere alla linea successiva

scrivi_lista_linea_successiva(file_name, linea_da_trovare, lista_da_scrivere, 'polinomi')

linea_da_trovare = 'polinomi = '  # La linea da trovare nel file che inizia con 'print("Q"'
lista_da_scrivere = pesi_importati  # La lista da scrivere alla linea successiva

scrivi_lista_linea_successiva(file_name, linea_da_trovare, lista_da_scrivere, 'pesi')






