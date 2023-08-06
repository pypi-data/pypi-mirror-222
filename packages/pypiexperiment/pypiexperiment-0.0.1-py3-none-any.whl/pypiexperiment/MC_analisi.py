from mc_integral_1_dim import *

dati_acquisiti = []
num_bins = 20
bins = [[] for _ in range(num_bins)]
limits = [1, 2]
estremi_bins = genera_estremi_bin(limits, num_bins)

# Apre il file in modalità lettura
with open("mc_integral_8.txt", "r") as file:
    # Legge il contenuto del file riga per riga
    for riga in file:
        # Rimuove eventuali spazi o caratteri di nuova riga dalla riga
        riga = riga.strip()
        # Se la riga non è vuota, estrae la x e la aggiunge alla lista dei dati acquisiti
        if riga:
            x = float(riga)
            dati_acquisiti.append(x)
            bins = assegna_bin(bins, limits, num_bins, x, estremi_bins)

# Stampa la lista dei dati acquisiti

medie = [sum(lst) / len(lst) for lst in bins]
bin_count = [len(lst) for lst in bins]
print(sum(bin_count))
print(medie)

