from PIL import Image
import numpy as np

from Lab3 import rysuj_ramki_kolorowe, rysuj_po_skosie_szare

def zmien_kolor(kolor, zmiana):
    kolor[0] = (kolor[0] + zmiana) % 256
    kolor[1] = (kolor[1] + zmiana) % 256
    kolor[2] = (kolor[2] + zmiana) % 256
    return kolor

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

#rysuj_ramki_szare(250, 180, 20, 50).show()
#rysuj_ramki_szare(250, 180, 20, 50).save("rysuj_ramki_szare.bmp")

def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w,3)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    kolor1 = [50, 50, 50]
    kolor2 = [150, 150, 150]
    for k in range(ile):
        kolor = kolor1 if k % 2 == 0 else kolor2
        for g in range(ile):
            i = k * grub + g
            for j in range(h):
                tab[j,i] = kolor
        zmien_kolor(kolor1, zmiana_koloru)
        zmien_kolor(kolor2, zmiana_koloru)
    tab = tab * 255
    return Image.fromarray(tab)


#rysuj_pasy_pionowe_szare(100, 180, 10, 50).show()
#rysuj_pasy_pionowe_szare(100, 180, 10, 50).save("rysuj_pasy_pionowe_szare.bmp")

# Zadanie 2
gwiazdka = Image.open("gwiazdka.bmp")

def negatyw(obraz):
    tab = np.asarray(obraz)
    if len(tab.shape) == 2:
        h, w = tab.shape
    elif len(tab.shape) == 3:
        h, w, c = tab.shape
    tab_neg = tab.copy()
    if obraz.mode == "1":
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 1 - tab[i, j]
        return Image.fromarray(tab_neg)
    elif obraz.mode == "L" or obraz.mode == "RGB":
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab[i, j]
        return Image.fromarray(tab_neg)
    else:
        return "Zły format obrazu"


#negatyw(gwiazdka).show()
#negatyw(gwiazdka).save("negatyw_gwiazdka.bmp")
#negatyw(rysuj_ramki_kolorowe(200, [20,120,220], 6, 5, -6)).show()
#negatyw(rysuj_ramki_kolorowe(200, [20,120,220], 6, 5, -6)).save("negatyw_ramki_kolorowe.png")
#negatyw(rysuj_po_skosie_szare(100, 300, 6, 5)).show()
#negatyw(rysuj_po_skosie_szare(100, 300, 6, 5)).save("negatyw_skosy_szare.bmp")

# Zadanie 3
inicjaly = Image.open("inicjaly.bmp")

def koloruj_w_paski(obraz, grub, zmiana_kolor):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t =(h, w, 3)
    kolor = [120, 240, 50]
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h/ grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if t_obraz[i, j] == False:
                    tab[i, j] = kolor
                else:
                    tab[i, j] = [255, 255, 255]
        zmien_kolor(kolor, zmiana_kolor)
    return Image.fromarray(tab)

koloruj_w_paski(inicjaly, 10, 50).show()
koloruj_w_paski(inicjaly, 10, 50).save("koloruj_paski.png")
koloruj_w_paski(inicjaly, 10, 50).save("koloruj_paski.jpg")
