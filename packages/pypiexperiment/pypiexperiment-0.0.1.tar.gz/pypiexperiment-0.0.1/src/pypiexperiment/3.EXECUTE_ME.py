import subprocess
import importlib

# Lista delle librerie da installare
libraries = ['sympy', 'mpmath', 'numpy', 'scipy', 'time', 'random', 'matplotlib']

# Installazione delle librerie
for library in libraries:
    try:
        importlib.import_module(library)
        print(f"La libreria {library} è già installata.")
    except ImportError:
        print(f"Installazione di {library}...")
        subprocess.call(['pip3', 'install', library])
