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
    h, w = tab_obraz.shape
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

# Zadanie 2 1.1


def rysuj_ramki(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = min(w, h) // (2 * grub)
    for i in range(ile):
        kolor = 0 if i % 2 == 0 else 255
        # wymiary ramki
        x0, y0 = i * grub, i * grub
        x1, y1 = w - i * grub, h - i * grub
        for y in range(y0, y1):
            for x in range(x0, x1):
                if x - x0 < grub or x1 - x <= grub or y - y0 < grub or y1 - y <= grub:
                    tab[y, x] = kolor

    return Image.fromarray(tab)


rysuj_ramki(200, 150, 10).show()

# Zadanie 2 1.2


def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for k in range(ile):
        for g in range(ile):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    return Image.fromarray(tab)


rysuj_pasy_pionowe(100, 180, 10).show()

# Zadanie 2 1.3


def rysuj_wlasne(w, h, ile):
    t = (h, w)
    b = 0
    c = 0
    tab = np.ones(t, dtype=np.uint8)
    for a in range(ile):
        for i in range(int(h/ile)):
            for j in range(int(w/ile)):
                tab[i+b, j+c] = 0
        b += int(h/ile)
        c += int(w/ile)
    tab = tab.astype(bool)
    return Image.fromarray(tab)


rysuj_wlasne(200, 160, 4).show()


# Zadanie 3

inicjaly = Image.open("inicjaly.bmp")
obraz_bazowy = Image.open("obraz_bazowy.bmp")

def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_obraz_wstawiany = np.asarray(obraz_wstawiany).astype(np.uint8)
    tab_obraz_bazowy = np.asarray(obraz_bazowy).astype(np.uint8)
    h, w = tab_obraz_bazowy.shape
    h0, w0 = tab_obraz_wstawiany.shape
    t = (h, w)
    tab = np.asarray(obraz_bazowy).astype(np.uint8)
    n_k = min(h, n + h0)
    m_k = min(w, m + w0)
    n_p = max(0, n)
    m_p = max(0, m)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab[i][j] = tab_obraz_wstawiany[i - n][j - m]
    tab = tab.astype(bool)
    return Image.fromarray(tab)


wstaw_obraz_w_obraz(obraz_bazowy, inicjaly, 50, 10).show()
