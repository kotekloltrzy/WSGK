from PIL import Image
import numpy as np

def rysuj_po_skosie_szare(h,w,a,b):
    t = (h,w)
    tab = np.zeros(t,dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i,j] = (a*i + b*j) %256
    return tab

im_skos = Image.fromarray(rysuj_po_skosie_szare(100, 100, -20, 20))

#im_skos.show()

def rysuj_ramki_kolorowe(w, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = 6
    kolor_g = 4
    kolor_b = 2
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r)%256
        kolor_g = (kolor_g - zmiana_koloru_g)%256
        kolor_b = (kolor_b - zmiana_koloru_b)%256
    return tab

rgb_im = Image.fromarray(rysuj_ramki_kolorowe(100,20,13,4))

#rgb_im.show()

def rysuj_kolo(w, h, r, m, n, kolor): # koło o promieniu r i środku m, n, kolor = 0 lub 255
    t = (h, w) # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if (i-n)**2+(j-m)**2 < r**2: # wzór na koło o środku (m_s, n_s) i promieniu r
                tab[i, j] = kolor
            else:
                tab[i, j] = 255 - kolor
    return tab

kolo_im = Image.fromarray(rysuj_kolo(100,100,40,50,50, 255))

#kolo_im.show()

a = rysuj_kolo(100,100,40,50,50, 200) # tablica kanału alfa

rgb  = rysuj_ramki_kolorowe(100,20,13,4)   # tablica RGB
a_ext = np.expand_dims(a, axis=-1)
combined = np.concatenate((rgb, a_ext), axis=-1)

rgba_im = Image.fromarray(combined)

#rgba_im.show()

a = rysuj_kolo(100,100,40,50,50, 200) # tablica kanału alfa
rgb  = rysuj_ramki_kolorowe(100,20,13,4)   # tablica RGB

a_ext = np.expand_dims(a, axis=-1)
combined1 = np.concatenate((rgb, a_ext), axis=-1)


cmyk_im = Image.fromarray(combined1, mode='CMYK')

#cmyk_im.show()

