from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly.bmp")

print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

t_inicjaly = np.asarray(inicjaly)
print("tyd danych tablicy", t_inicjaly.dtype)
print("rozmiar tablicy", t_inicjaly.shape)

# Zadanie 1

def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h,w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j] = 0
        for j in range(w - grub, w):
            tab_obraz[i][j] = 0
    for i in range(w):
        for j in range(grub):
            tab_obraz[j][i] = 0
        for j in range(h - grub, h):
            tab_obraz[j][i] = 0

    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)

rysuj_ramke_w_obrazie(inicjaly, 5).show()

# Zadanie 2

def rysuj_ramki(w,h,grub):
    t = (h,w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for a in range(ile):
        for i in range(h):
            for j in range(grub-a):
                tab[i-a][j-a] = 0
            for j in range(w - grub-a, w-a):
                tab[i][j] = 0
        for i in range(w):
            for j in range(grub-a):
                tab[j][i] = 0
            for j in range(h - grub-a, h-a):
                tab[j][i] = 0


    tab = tab.astype(bool)
    return Image.fromarray(tab)

rysuj_ramki(200, 150, 10).show()