from sympy import *
import random
import keyboard
from SELETTORE_FUNC import *
import matplotlib.pyplot as plt

def assegna_bin(bins, limits, num_bins, point, estremi_bins):
    bin_index = 0
    for range_min, range_max in estremi_bins:
        if range_min < point <= range_max:
            bins[bin_index].append(point)
            break
        bin_index += 1

    return bins

def genera_estremi_bin(limits, num_bins):
    range_ = limits[1] - limits[0]
    bin_range = range_/ num_bins
    estremi_bins = [[0,0] for _ in range(num_bins)]
    bin_index = 0
    for estremo in estremi_bins:
        estremo[0] = bin_index * bin_range + limits[0]
        estremo[1] = (bin_index + 1) * bin_range + limits[0]
        bin_index += 1
        
    return estremi_bins

def err_MC(funcs, funcs_sq, num_points, range_):
    f_m = (sum(funcs) / len(funcs))**2
    f_sq_m = sum(funcs_sq) / len(funcs_sq)
    var_mc = ((f_sq_m - f_m)/(num_points - 1))**(.5)
    #error = var_mc * range_ / (num_points)**(.5)
    return var_mc

def monte_carlo_integration(func, limits, num_points, num_bins):
    integral = 0
    max_f = 0
    min_f = 0
    funcs = []
    funcs_sq = []
    estremi_bins = genera_estremi_bin(limits, num_bins)
    bins = [[] for _ in range(num_bins)]
    for _ in range(num_points):
        point = random.uniform(limits[0], limits[1])
        bins = assegna_bin(bins, limits, num_bins, point, estremi_bins)
        integrand = func(point)
        funcs.append(integrand)
        funcs_sq.append(integrand**2)
        max_f = max(integrand, max_f)
        min_f = min(integrand, min_f)
        integral += integrand

    range_ = (limits[1] - limits[0])
    err_mc = err_MC(funcs, funcs_sq, num_points, range_)
    integral *= range_
    result = integral / num_points
    limits_y = [min_f, max_f]
    return result, limits_y, bins, err_mc

def accetta_punto(point_y, integrand):
    if integrand > 0 and point_y < integrand and point_y > 0:
        accettato = True
    elif integrand < 0 and point_y > integrand and point_y < 0:
        accettato = True
    else:
        accettato = False
    return accettato

def hit_or_miss(func, limits, num_points, limits_y):
    acc = 0
    acc_int = 0
    bys = 0
    funcs = []
    funcs_sq = []
    for _ in range(num_points):
        point_x = random.uniform(limits[0], limits[1])
        point_y = random.uniform(limits_y[0], limits_y[1])
        integrand = func(point_x)
        abs_value = abs(integrand)
        accettato = accetta_punto(point_y, integrand)
        if accettato:
            acc += 1
            if integrand < 0:
                acc_int -= 1
            elif integrand > 0:
                acc_int += 1
            funcs.append(integrand)
            funcs_sq.append(integrand**2)
            with open("mc_integral_8.txt", "a") as file:
                file.write(str(point_x) + "\n")
        else:
            bys += 1
    range_ = limits[1] - limits[0]
    area = range_*(limits_y[1] - limits_y[0])
    integral = acc_int * area / num_points
    eff = acc / num_points
    eff_b = bys / acc
    # Moltiplico l'errore per l'area in cui estraggo punti
    err_1 = area * ((eff*(1-eff))/(num_points))**(.5) 
    err_2 = err_MC(funcs, funcs_sq, num_points, range_)
    return integral, eff, eff_b, err_1, err_2
    
def main():
    global f
    global df
    global ddf
    global dddf

    f, df, ddf, dddf, fx = seleziona_funzione()
    
    limits = []
    lower = float(input("Inserisci il limite inferiore: "))
    upper = float(input("Inserisci il limite superiore: "))
    limits.append((lower, upper))

    num_points = int(input("Inserisci il numero di punti per il metodo Monte Carlo: "))
    num_bins = int(input("Inserisci il numero di bin per l'integrazione: "))

    result, limits_y, bins, err_mc = monte_carlo_integration(f, limits[0], num_points, num_bins)
    
    print("Risultato dell'integrale MC: " + str(result) + " +/- " + str(err_mc))
    print("Err_MC = " + str(err_mc))
    
    medie = [sum(lst) / len(lst) for lst in bins]
    f_medie = [f(x_media) for x_media in medie]
    bin_count = [len(lst) for lst in bins]
    
    plt.scatter(medie, f_medie)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Scatter Plot')
    plt.grid(True)
    plt.axis('equal')
    plt.show()
    
    result, eff, eff_b, err_1, err_2 = hit_or_miss(f, limits[0], num_points, limits_y)
    print("Risultato dell'integrale HoM: " + str(result) + " +/- " + str(err_1))
    print("Efficienza = " + str(eff))
    print("Efficienza byas = " + str(eff_b))
    print("Err_1 = " + str(err_1))
    print("Err_2 = " + str(err_2))
    
    
if __name__ == "__main__":
    main()
