from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from numpy.ma.core import array

# Zadanie 1 a)

im = Image.open("obraz.png")

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

#print("tryb", im.mode)
#print("format", im.format)
#print("rozmiar", im.size)
#statystyki(im)


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

#print(f"\nLiczba pikslei o wartości 155: \nR: {r_ilosc}\nG: {g_ilosc}\nB: {b_ilosc}")

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

#print("\nW obrazie jest:", zlicz_piksele(im, (155,155,155)), "pikseli podanego koloru")

# Zadanie 2

im.save("obraz.jpg")
im_jpg = Image.open("obraz.jpg")

#print("\nStatystyki im:")
#statystyki(im)
#print("tryb", im.mode)
#print("format", im.format)
#print("rozmiar", im.size)
#w, h = im.size
#im.show()
#print("\nStatystyki im_jpg:")
#statystyki(im_jpg)
#print("tryb", im_jpg.mode)
#print("format", im_jpg.format)
#print("rozmiar", im_jpg.size)
#w, h = im_jpg.size
#im_jpg.show()

# Zadanie 2 b)

#diff = ImageChops.difference(im, im_jpg)
#diff.show()
#print("\nStatystyki diff:")
#statystyki(diff)
#print("tryb", diff.mode)
#print("format", diff.format)
#print("rozmiar", diff.size)
#w, h = diff.size

# Zadanie 2 c)

#im_jpg.save("obraz2.jpg")
#im_jpg2 = Image.open("obraz2.jpg")
#im_jpg2.save("obraz3.jpg")
#im_jpg3 = Image.open("obraz3.jpg")

#diff2 = ImageChops.difference(im_jpg, im_jpg3)
#diff2.show()

# Zadanie 3

tab_im = np.asarray(im)
print(tab_im)

def pobierz_kanal(obraz, kanal):
    t_obraz = np.asarray(obraz)
    h, w, k = t_obraz.shape
    t = (h, w, 3)
    tablica = np.ones(t, dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            tablica[j,i] = obraz[j,i,kanal]
    return tablica


im_r = Image.fromarray(pobierz_kanal(tab_im, 0))
im_g = Image.fromarray(pobierz_kanal(tab_im, 1))
im_b = Image.fromarray(pobierz_kanal(tab_im, 2))
im_r.show()
im_g.show()
im_b.show()
