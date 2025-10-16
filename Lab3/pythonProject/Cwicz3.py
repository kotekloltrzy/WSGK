from PIL import Image
import numpy as np

from Lab3 import rysuj_ramki_kolorowe, rysuj_po_skosie_szare


# Zadanie 1

def rysuj_ramki_szare(w, h, grub, zmiana_koloru):
    t = (h, w, 3)
    kolor = [255, 255, 255]
    tab = np.ones(t, dtype=np.uint8)
    ile = min(w, h) // (2 * grub)
    for i in range(ile):
        kolor[0] = kolor[0] - zmiana_koloru
        kolor[1] = kolor[1] - zmiana_koloru
        kolor[2] = kolor[2] - zmiana_koloru
        # wymiary ramki
        x0, y0 = i * grub, i * grub
        x1, y1 = w - i * grub, h - i * grub
        for y in range(y0, y1):
            for x in range(x0, x1):
                if x - x0 < grub or x1 - x <= grub or y - y0 < grub or y1 - y <= grub:
                    tab[y, x] = kolor

    return Image.fromarray(tab)

rysuj_ramki_szare(250, 180, 10, 25).show()

def rysuj_pasy_pionowe_szare(w, h, grub, kolor1, kolor2):
    t = (h, w,3)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for k in range(ile):
        kolor = kolor1 if k % 2 == 0 else kolor2
        for g in range(ile):
            i = k * grub + g
            for j in range(h):
                tab[j,i] = kolor
    tab = tab * 255
    return Image.fromarray(tab)


#rysuj_pasy_pionowe_szare(100, 180, 10, [50,50,50], [200,200,200]).show()

# Zadanie 2
gwiazdka = Image.open("gwiazdka.bmp")

def negatyw(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    if obraz.mode == 1:
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 1 - tab[i, j]
        return Image.fromarray(tab_neg)
    elif obraz.mode == "L":
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab[i, j]
        return Image.fromarray(tab_neg)
    elif obraz.mode == "RGB":
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab[i, j]
        return Image.fromarray(tab_neg)
    else:
        return "Zły format obrazu"

negatyw(gwiazdka).show()
negatyw(rysuj_ramki_kolorowe(200, [20,120,220], 6, 5, -6)).show()
negatyw(rysuj_po_skosie_szare(100, 300, 6, 5)).show()

