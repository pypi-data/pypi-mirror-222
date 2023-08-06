import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sympy import *
from complex_third import *
import time
import random
from SELETTORE_FUNC import *

def generate_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = '#{:06x}'.format(random.randint(0, 0xFFFFFF))
        colors.append(color)
    return colors

# Genera 100 colori diversi
colors = generate_colors(100)

global domain, num_enl, metodo, part

domain = (-3, 3, -3, 3)
num_enl = 1
pr = 20
part = 200

global f
global df
global ddf
global dddf

f, df, ddf, dddf, fx = seleziona_funzione()

# Segli il metodo di individuazione dello zero che preferisci utilizzare
metodo = chiedi_char("""Segli il metodo di individuazione dello zero che preferisci utilizzare
A : Newton-Raphson (m=2)
B : Rosignoli + (m=3)
C : Rosignoli - (m=3)
D : Rosignoli medio (m=3)
E : 4 termini del polinomio di Taylor
F : 5 termini del polinomio di Taylor
G : 6 termini del polinomio di Taylor
H : Metodo di Halley (m=3)
La tua scelta è: """)

"""
# A list of colors to distinguish the roots.
colors = ['#0000FF', '#FF0000', '#00FF00', '#FFFF00', '#00FFFF', '#FF00FF', '#800080', '#FFA500', '#008080', '#FFC0CB', '#800000']
"""

TOL = 1.e-10

global fig
fig = None

def newton_ros(z0, MAX_IT=1000):
    global f, df, ddf, dddf, domain, metodo
    """
    The Newton-Raphson method applied to f(z).
    Returns the root found, starting with an initial guess, z0, or False
    if no convergence to tolerance TOL was reached within MAX_IT iterations.
    """
    z = z0
    for i in range(MAX_IT):
        a = ddf(z)/2
        b = df(z)
        c = f(z)
        
        if metodo == "A":
            dz = - c/b
        elif metodo == "B":
            dz = (- b + (b**2 - 4*a*c)**.5)/(2*a)
        elif metodo == "C":
            dz = (- b - (b**2 - 4*a*c)**.5)/(2*a)
        elif metodo == "D":
            dz = (- b)/(2*a)
        elif metodo == "E":
            dz = - a/b - c*a**2/(2*b**3) - c**2*a**3/(2*b**5)
        elif metodo == "F":
            dz = - a/b - c*a**2/(2*b**3) - c**2*a**3/(2*b**5) - 5*c**3*a**4/(8*b**7)
        elif metodo == "G":
            dz = - a/b - c*a**2/(2*b**3) - c**2*a**3/(2*b**5) - 5*c**3*a**4/(8*b**7) - 7*c**4*a**5/(8*b**9)
        elif metodo == "H":
            dz = - c / (b - c * a / b )
            
        if abs(dz) < TOL:
            return z
        z += dz
    return False

def onclick(event):
    global domain, fig, num_enl, part
    xmin, xmax, ymin, ymax = domain
    if event.inaxes is not None:
        x = event.xdata
        y = event.ydata
        
    if event.button == 1:
        x_r = event.xdata/part
        y_r = event.ydata/part
        x = xmin*(1 - x_r) + xmax*(x_r)
        y = ymin*(1 - y_r) + ymax*(y_r)
        dec = 5
        print("You just clicked on the point ("f"{x:.{dec}f}, "f"{y:.{dec}f})")
        x_range = xmax - xmin
        y_range = ymax - ymin
        xmin = x - x_range / 8
        xmax = x + x_range / 8
        ymin = y - y_range / 8
        ymax = y + y_range / 8
        rectangle = plt.Rectangle((xmin, ymin), x_range/4, y_range/4, edgecolor='red', facecolor='none', linewidth=2)
        plt.gca().add_patch(rectangle)
        time.sleep(2)
        rectangle.set_visible(False)
        plt.close(fig)
        domain = (xmin, xmax, ymin, ymax)
        num_enl *= 4
        plot_newton_fractal(part)
        
    if event.button == 3:
        x_r = event.xdata/part
        y_r = event.ydata/part
        x = xmin*(1 - x_r) + xmax*(x_r)
        y = ymin*(1 - y_r) + ymax*(y_r)
        dec = 5
        print("You just right clicked on the point ("f"{x:.{dec}f}, "f"{y:.{dec}f})")
        plt.close(fig)
        x_range = xmax - xmin
        y_range = ymax - ymin
        xmin = x - 2*x_range
        xmax = x + 2*x_range
        ymin = y - 2*y_range
        ymax = y + 2*y_range
        domain = (xmin, xmax, ymin, ymax)
        num_enl /= 4
        plot_newton_fractal(part)
        
def plot_newton_fractal(n=200):
    global f, df, ddf, dddf, domain, fig, num_enl, part
    part = n
    print("Computation initialised...")
    """
    Plot a Newton Fractal by finding the roots of f(z).
    The domain used for the fractal image is the region of the complex plane
    (xmin, xmax, ymin, ymax) where z = x + iy, discretized into n values along
    each axis.
    """
    roots = []
    m = np.zeros((n, n))

    def get_root_index(roots, r):
        """Get the index of r in the list roots.

        If r is not in roots, append it to the list.

        """
        try:
            return np.where(np.isclose(roots, r, atol=TOL))[0][0]
        except IndexError:
            roots.append(r)
            return len(roots) - 1

    xmin, xmax, ymin, ymax = domain
    for ix, x in enumerate(np.linspace(xmin, xmax, n)):
        for iy, y in enumerate(np.linspace(ymin, ymax, n)):
            z0 = x + y*1j
            r = newton_ros(z0)
            if r is not False:
                ir = get_root_index(roots, r)
                m[iy, ix] = ir
    nroots = len(roots)
    
    """
    # Genera una lista di colori in base al numero di radici
    colors = ['#{:06x}'.format(0x1000000 + int(i * 0xffffff / nroots)) for i in range(nroots)]
    cmap = ListedColormap(colors)
    """
    
    if nroots > len(colors):
        # Use a "continuous" colormap if there are too many roots.
        cmap = 'hsv'
    else:
        # Use a list of colors for the colormap: one for each root.
        cmap = ListedColormap(colors[:nroots])
    
    # Aggiunta dei valori dei vertici
    dec = 5
    fig = plt.figure()
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.imshow(m, cmap=cmap, origin='lower')
    plt.axis('off')
    plt.annotate(f"(xmax = {xmax:.{dec}f})", (part, 0), textcoords="offset points", xytext=(0,-10), ha='center')
    plt.annotate(f"(xmin = {xmin:.{dec}f})", (0, part), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"(ymax = {ymax:.{dec}f})", (part, part), textcoords="offset points", xytext=(0,5), ha='center')
    plt.annotate(f"(ymin = {ymin:.{dec}f})", (0, 0), textcoords="offset points", xytext=(0,-10), ha='center')
    
    # Aggiunta del bordino nero
    border_color = 'black'
    border_width = 2
    plt.plot([0, part], [part, part], color=border_color, linewidth=border_width)
    plt.plot([part, part], [part, 0], color=border_color, linewidth=border_width)
    plt.plot([0, 0], [0, part], color=border_color, linewidth=border_width)
    plt.plot([part, 0], [0, 0], color=border_color, linewidth=border_width+1)
    
    # Annotazione sulla dimensione dell'immagine
    text_dim = "L'immagine è stata realizzata\ncon " +str(part)+"*"+str(part)+" componenti."
    plt.annotate(text_dim, (part/2, 0), textcoords="offset points", xytext=(0,- part/18), ha='center')

    # Aggiunta del titolo
    plt.title("Frattale con " + str(num_enl) + "X ingrandimenti")
    plt.show()

plot_newton_fractal(n=500)
