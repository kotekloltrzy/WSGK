from PIL import Image
import numpy as np

def rysuj_ramke_szare(w,h,grub,kolor_ramki,kolor):
    t =(h,w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki
    tab[grub:h-grub, grub:w-grub] = kolor
    return Image.fromarray(tab)

im_ramka = rysuj_ramke_szare(120,60,8,100,200)
#im_ramka.show()


def rysuj_pasy_poziome_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h/grub)
    for k in range(ile):
        for g in range(grub):
            i=k*grub+g
            for j in range(w):
                tab[i, j] = (k + zmiana_koloru) % 256
    return Image.fromarray(tab)

im_paski = rysuj_pasy_poziome_szare(100, 246, 1, 10)
#im_paski.show()

def negatyw_szare(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i,j] = 255 - tab[i,j]
    return Image.fromarray(tab_neg)

obraz_neg = negatyw_szare(im_paski)
#obraz_neg.show()

def rysuj_po_skosie_szare(h, w, a, b):
    t = (h,w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i,j] = (a*i + b*j) % 256
    return Image.fromarray(tab)

im_skos = rysuj_po_skosie_szare(100, 300, 1, 3)
#im_skos.show()

def rysuj_ramke_kolor(w, h, grub, kolor_ramki, kolor_tla):
    t = (h,w,3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki
    tab[grub:h - grub, grub:w - grub, 0] = kolor_tla[0] # R
    tab[grub:h - grub, grub:w - grub, 1] = kolor_tla[1] # G
    tab[grub:h - grub, grub:w - grub, 2] = kolor_tla[2] # B
    return Image.fromarray(tab)

im_ramka_kolor = rysuj_ramke_kolor(120, 60, 8, [0, 0, 255], [100, 200, 0])
#im_ramka_kolor.show()

def rysuj_pasy_poziome_3kolory(w, h, grub):
    t = (h,w,3)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if k % 3 == 0:
                    tab[i,j] = [255, 0,0]
                elif k % 3 == 1:
                    tab[i,j] = [0, 255, 0]
                else:
                    tab[i,j] = [0, 0, 255]
    return Image.fromarray(tab)

obraz1 = rysuj_pasy_poziome_3kolory(200, 100, 10)
#obraz1.show()

def rysuj_pasy_poziome_kolor(w,h,grub,kolor, zmiana_koloru):
    t = (h,w,3)
    tab = np.ones(t, dtype =np.uint8)
    tab[:] = kolor
    ile = int(h/grub)
    for k in range(ile):
        r = (kolor[0] + k * zmiana_koloru) % 256
        g = (kolor[1] + k * zmiana_koloru) % 256
        b = (kolor[2] + k * zmiana_koloru) % 256
        for m in range(grub):
            i = k * grub + m
            for j in range(w):
                tab[i, j] = [r, g, b]
    return Image.fromarray(tab)

obraz2 = rysuj_pasy_poziome_kolor(200, 100, 4, [100,200,0], 19)
#obraz2.show()

def koloruj_obraz(obraz, kolor):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t = (h, w ,3)
    tab = np.ones(t,dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if t_obraz[i, j] == False:
                tab[i, j] = kolor
            else:
                tab[i, j] = [255, 255, 255]
    return Image.fromarray(tab)

gwiazdka = Image.open("gwiazdka.bmp")
inicjaly = Image.open("inicjaly.bmp")
obraz3 = koloruj_obraz(gwiazdka, [120, 240, 50])
obraz4 = koloruj_obraz(inicjaly, [200, 120, 40])
#obraz3.show()
#obraz4.show()

def rysuj_ramki_kolorowe(w, kolor, zmiana_koloru_r, zmiana_koloru_g,zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t,dtype=np.uint8)
    kolor_r = kolor[0]
    kolor_g = kolor[1]
    kolor_b = kolor[2]
    z = w
    for k in range(int(w/2)):
        for i in range(k,z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r) % 256
        kolor_g = (kolor_g - zmiana_koloru_g) % 256
        kolor_b = (kolor_b - zmiana_koloru_b) % 256
    return Image.fromarray(tab)

obraz5 = rysuj_ramki_kolorowe(200, [0, 120, 220], 8, 15, -13)
#obraz5.show()
