# LIBRERIA INTERAMENTE SVILUPPATA DA IMAN ROSIGNOLI 18-08-1998 TERNI (TR)
def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def chiedi_char(frase="Inserisci un carattere: "):
    while True:
        carattere = input(frase)
        if check_quit(carattere):
            print("Applicazione terminata.")
            quit()
        if len(carattere) == 1 and not carattere.isdigit(): # Controlla se il carattere è una lettera
            return carattere  # Restituisci il carattere se è valido
        else:
            print("Input non valido. Inserisci un solo carattere.")

def chiedi_conferma(frase="Inserisci S o N: "):
    while True:
        user_input = input(frase)
        if check_quit(user_input):
            print("Applicazione terminata.")
            quit()
        if user_input.upper() == "S":
            return True
        elif user_input.upper() == "N":
            return False
        else:
            print("Input non valido. Riprova.")

def chiedi_numero(frase="Inserisci l'input: "):
    while True:
        try:
            user_input = input(frase)
            if check_quit(user_input):
                print("Applicazione terminata.")
                quit()
            numero = float(user_input)
            return numero  # Restituisci il numero se è valido
        except ValueError:
            print("Input non valido. Riprova.")

def chiedi_numero_int(frase="Inserisci l'input: "):
    while True:
        try:
            user_input = input(frase)
            if check_quit(user_input):
                print("Applicazione terminata.")
                quit()
            numero = int(user_input)
            return numero  # Restituisci il numero se è valido
        except ValueError:
            print("Input non valido. Riprova.")

def chiedi_numero_pos(frase="Inserisci l'input: "):
    while True:
        try:
            user_input = input(frase)
            if check_quit(user_input):
                print("Applicazione terminata.")
                quit()
            numero = float(user_input)
            if numero > 0: # Controlla se il carattere è una lettera
                return numero  # Restituisci il carattere se è valido
            else:
                print("Input non valido. Inserisci un numero positivo.")
        except ValueError:
            print("Input non valido. Riprova.")

def chiedi_numero_neg(frase="Inserisci l'input: "):
    while True:
        try:
            user_input = input(frase)
            if check_quit(user_input):
                print("Applicazione terminata.")
                quit()
            numero = float(user_input)
            if numero < 0: # Controlla se il carattere è una lettera
                return numero  # Restituisci il carattere se è valido
            else:
                print("Input non valido. Inserisci un numero positivo.")
        except ValueError:
            print("Input non valido. Riprova.")
            
def fattoriale(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 1:
        return 1
    else:
        risultato = n * fattoriale(n-1, memo)
        memo[n] = risultato
        return int(risultato)

def elemento_lista(lettera, lista):
    for elemento in lista:
        separatore = " : "
        indice_separatore = elemento.find(separatore)
        if indice_separatore != -1:
            lettera_elemento = elemento[:indice_separatore].strip().upper()
            espressione = elemento[indice_separatore + len(separatore):]
            if lettera_elemento == lettera.strip().upper():
                return espressione
    print("Nessuna espressione trovata per la lettera", lettera)

def elemento_lettera(title, lista):
    lettera = None
    for elemento in lista:
        lettera, nome = elemento.split(" : ")
        if nome == title:
            return lettera
            break
    print("Nessuna lettera trovata per l'espressione", title)

def check_esc():
    return keyboard.is_pressed('esc')

def check_quit(user_input):
    return "quit()" in user_input.lower()

def leggi_lista_da_file(nome_file, nome_lista = 'polinomi'):
    linea_dichiarazione = None

    with open(nome_file, "r") as file:
        for line in file:
            if nome_lista + " =" in line:
                linea_dichiarazione = line
                break

    elementi = []

    if linea_dichiarazione:
        # Rimuovi "frutti =" dalla linea di dichiarazione
        linea_senza_dichiarazione = linea_dichiarazione.replace(nome_lista + " =", "")

        # Rimuovi spazi bianchi e parentesi quadre
        linea_senza_dichiarazione = linea_senza_dichiarazione.strip().strip("[]")

        # Separa gli elementi utilizzando la virgola come delimitatore
        elementi = linea_senza_dichiarazione.split(",")

    # Rimuovi eventuali spazi bianchi dagli elementi
    elementi = [elemento.strip() for elemento in elementi]

    return elementi

def cancella_righe_lista(file_name, nome_lista = "polinomi"):
    with open(file_name, 'r+') as file:
        contenuto = file.readlines()
        file.seek(0)  # Torna all'inizio del file

        for linea in contenuto:
            if not linea.startswith("    " + nome_lista + " =") and not linea.startswith("    " + nome_lista + ".append("):
                file.write(linea)  # Scrivi solo le linee diverse da quelle da cancellare

        file.truncate()  # Riduci la dimensione del file se necessario

def formatta_lista_somma(lista):
    maiuscole = set()
    risultato = []

    for elemento in lista:
        parte_sinistra, parte_destra = elemento.split(" : ", 1)
        iniziale = parte_sinistra[0]

        if iniziale not in maiuscole:
            maiuscole.add(iniziale)
            risultato.append(parte_sinistra + " : " + parte_destra)

    risultato = sorted(risultato)
    risultato = [elemento.replace("'", '').strip() for elemento in risultato]  # Rimuovi anche i singoli apici

    return risultato

# Funzioni di selezione codice lettera + numero successivo

def associa_valori_alfabeto():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    associazioni = {}

    for indice, lettera in enumerate(alfabeto, 1):
        associazioni[lettera] = indice

    return associazioni

def scomponi(parola):
    lettere = ""
    numeri = ""
    for carattere in parola:
        if carattere.isalpha():
            lettere += carattere
        elif carattere.isdigit():
            numeri += carattere
    if numeri != "":
        return lettere, int(numeri)
    else:
        return lettere, 0

def primo_numero_mancante(lista_numeri):
    lista_numeri.sort()  # Ordina la lista in modo crescente
    numero_mancante = 1
    for numero in lista_numeri:
        if numero == numero_mancante:
            numero_mancante += 1
        else:
            return numero_mancante
    return numero_mancante

def find_next_uppercase_letter(funzioni_importate):
    used_letters = set()
    indici_usati = []
    associazioni = associa_valori_alfabeto()
    valori_numerici = {numero: lettera for lettera, numero in associazioni.items()}

    for funzione in funzioni_importate:
        funzione = funzione.strip("'\"")  # Rimuovi gli apici singoli e doppi
        parts = funzione.split(" : ")
        if len(parts) >= 2:
            letter, number = scomponi(parts[0].strip())
            if letter and letter.isalpha() and letter.isupper():
                # Determino l'indice di ogni codice
                indice = number*26 + associazioni.get(letter)
                indici_usati.append(indice)

    # Determino l'indice mancante
    indice = primo_numero_mancante(indici_usati)
    
    # Qui determino la combinazione lettera + numero dell'indice mancante
    numero = indice // 26
    indice_lettera = indice - numero * 26
    lettera_corrispondente = valori_numerici[indice_lettera]
    if numero == 0:
        return lettera_corrispondente
    else:
        return lettera_corrispondente + str(numero)

def scrivi_lista_linea_successiva(file_name, linea_da_trovare, lista_da_scrivere, nome_lista = 'polinomi'):
    with open(file_name, 'r+') as file:
        contenuto = file.readlines()
        indice_linea = None

        # Trova l'indice della linea da trovare
        for i, linea in enumerate(contenuto):
            if linea.strip().startswith(linea_da_trovare):
                indice_linea = i
                break

        # Se l'indice è stato trovato, scrivi la dichiarazione della lista "funzioni" alla linea successiva
        if indice_linea is not None:
            indice_linea += 1  # Calcola l'indice della linea successiva
            dichiarazione_lista = f'    {nome_lista} = {lista_da_scrivere}\n'
            contenuto.insert(indice_linea, dichiarazione_lista)

            # Scrivi il contenuto aggiornato nel file
            file.seek(0)
            file.writelines(contenuto)
        else:
            print("Linea non trovata nel file.")
            
"""
def lagrange_inter_poly(zeros):
    z = Symbol('z')
    polynomials = []
    for i in range(len(zeros)):
        num = 1
        den = 1
        zi = zeros[i]
        for j in range(len(zeros)):
            zj = zeros[j]
            if zj != zi:
                num *= z - zj
                den *= zi - zj
        poly = num / den
        polynomials.append(poly)
    return polynomials
"""

def integrate_polynomial(polynomial, interval, deg):
    z = Symbol('z')
    a = interval[0]
    b = interval[1]
    polynomial = expand(polynomial)
    integral = 0
    for i in range(deg):
        integral += polynomial.coeff(z, i) / (i+1) * (b ** (i+1) - a ** (i+1))
    return integral
