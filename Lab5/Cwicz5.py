from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# Zadanie 1 a)

im = Image.open("obraz.png").convert("RGB")

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

print("tryb", im.mode)
print("format", im.format)
print("rozmiar", im.size)
statystyki(im)

def rysuj_histogram_rgb(obraz):
    hist = obraz.histogram()
    plt.title("histogram  RGB")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()

#rysuj_histogram_rgb(im)

def rysuj_histogram_r(obraz):
    hist = obraz.histogram()
    plt.title("histogram  R")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.show()

def rysuj_histogram_g(obraz):
    hist = obraz.histogram()
    plt.title("histogram  G")
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.show()

def rysuj_histogram_b(obraz):
    hist = obraz.histogram()
    plt.title("histogram  B")
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()

#rysuj_histogram_r(im)
#rysuj_histogram_g(im)
#rysuj_histogram_b(im)

# Zadanie 1 b)

tab = np.array(im)

kanal_r = tab[:, :, 0]
kanal_g = tab[:, :, 1]
kanal_b = tab[:, :, 2]

r_ilosc = np.sum(kanal_r == 155)
g_ilosc = np.sum(kanal_g == 155)
b_ilosc = np.sum(kanal_b == 155)

print(f"Liczba pikslei o wartości 155: \nR: {r_ilosc}\nG: {g_ilosc}\nB: {b_ilosc}")

# Zadanie 1 c)

def zlicz_piksele(obraz, kolor):
    tab = obraz.load()
    h, w = obraz.size
    ile = 0
    for i in range(h):
        for j in range(w):
            if tab[i, j] == kolor:
                ile += 1
    return ile

print("W obrazie jest:", zlicz_piksele(im, (155,155,155)), "pikseli podanego koloru")

# Zadanie 2
