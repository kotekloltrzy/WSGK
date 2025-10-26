from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly.bmp")

print("tryb", inicjaly.mode)
print("format", inicjaly.format)
print("rozmiar", inicjaly.size)

t_inicjaly = np.asarray(inicjaly)
print("tyd danych tablicy", t_inicjaly.dtype)
print("rozmiar tablicy", t_inicjaly.shape)

def rysuj_paski_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h,w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j]=0
        for j in range(w-grub, w):
            tab_obraz[i][j]=0
    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)

rysuj_paski_w_obrazie(inicjaly, 7).show()


def rysuj_ramke(w, h, grub):
    t = (h,w)
    tab = np.ones(t, dtype=np.uint8)
    tab[grub:h - grub, grub:w - grub] = 0
    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)

rysuj_ramke(200, 100, 20).show()

def rysuj_pasy_poziome(w,h,grub):
    t = (h,w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(h/grub)
    for k in range(ile):
        for g in range(ile):
            i = k * grub + g
            for j in range(w):
                tab[i, j] = k % 2
    tab = tab * 255
    return Image.fromarray(tab)

rysuj_pasy_poziome(100,200,20).show()

def wstaw_obraz(w,h,m,n, obraz):
    tab_obraz = np.asarray(obraz).astype(np.int_)
    h0, w0 = tab_obraz.shape
    t = (h,w)
    tab = np.zeros(t, dtype=np.uint8)
    n_k = min(h, n + h0)
    m_k = min(w,m+w0)
    n_p = max(0,n)
    m_p = max(0,m)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab[i][j] = tab_obraz[i-n][j-m]
    tab = tab.astype(bool)
    return Image.fromarray(tab)


wstaw_obraz(200, 100, 10, 10, inicjaly).show()
