# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.


Prima dell'esecuzione degli scripts assicurarsi che siano tutti nella stessa cartella.
Inoltre assicurarsi che:
    1. Python3 o versioni successive sia installato sul PC
    2. Siano stati eseguiti da riga di comando i seguenti comandi: pip3 install subprocess, pip3 install importlib
    3. Non si modifichi in modo sostanziale il contenuto dei file
    4. La libreria rosignoli_lib sia correttamente posizionata nella cartella
    5. Prima di eseguire qualsiasi script sia stato eseguito EXECUTE_ME.py
Con tutti questi accorgimenti tutti gli script dovrebbero essere funzionanti.


rosignoli_lib  <- libreria da me scritta con tutte le funzioni utilizzate - ok
README         <- Le istruzioni per l'utilizzo del pacchetto. - ok
lista_programmi<- Il file aperto - ok
EXECUTE_ME     <- installa le librerie necessarie per l'esecuzione degli script - ok

# Integrazione con algoritmi del trapezoide/Sympson e PV
trapzd         <- svolge ogni iterazione del metodo del trapezio - ok
qtrap          <- integra con il metodo del trapezio - ok
INT_SYMP       <- integra con Sympson - ok
INT_SYMP_PV    <- integra con Sympson e valuta il PV di funzioni razionali - ok

# Ricerca degli zeri
zeros          <- individua zeri e mostra i vari rate di convergenza - ok
nr             <- metodo di Newton - Raphson / radice cubica - ok
third          <- implementa la soluzione della cubica - ok

# Bacino di convergenza di funzioni complesse
fractal_zoom   <- disegna il bacino di convergenza di funzioni complesse con diversi metodi di ricerca degli zeri - ok

# Integrazione esatta con la quadratura di Gauss
ROOTFINDER     <- script che individua un certo numero di zeri in un intervallo specificato - ok
SELETTORE_FUNC <- seleziona funzioni - ok
METAFUNC       <- modifica la lista di funzioni disponibili - ok
SELETTORE_POLY <- seleziona la classe di polinomi - ok
METAPOLY       <- aggiorna la lista delle classi di polinomi - ok
GENERA_POLY    <- Genera il polinomio ortogonale della classe specificata - ok
GAUSS_INT      <- Integra esattamente con il metodo della quadratura di Gauss - ok

# Implementazione del metodo Monte Carlo
mc_integral_1_dim <- integra le funzioni 1-dimensionali di segno misto con il metodo MC - ok
MC_analisi     <- analizza i dati scritti su file durante HoM - ok
