from PIL import Image
import numpy as np

inicjaly = Image.open("inicjaly.bmp")
pionowe = Image.open("pionowe.bmp")
pionowe_tablica = np.asarray(pionowe)
rysuj_ramki = Image.open("rysuj_ramki.bmp")
rysuj_ramki_tablica = np.asarray(rysuj_ramki)

print("Tryb rysuj ramki: ", rysuj_ramki.mode)
print("Rozmiar obrazu: ", rysuj_ramki.size)
print("Wymiar tablicy: ", rysuj_ramki_tablica.ndim)
print("Liczba elementów tablicy: ", rysuj_ramki_tablica.size)

print("Tryb pionowe: ", pionowe.mode)
print("Piksel (66,13): ", pionowe_tablica[13][66])
print("Wartość elementu tablicy (97,20): ", pionowe_tablica[97][20])

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


# rysuj_ramke_w_obrazie(inicjaly, 5).show()

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


# rysuj_ramki(200, 150, 10).show()

# Zadanie 2 1.2


def rysuj_paski_pionowe(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    return Image.fromarray(tab)


# rysuj_paski_pionowe(200, 100, 10).show()

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


rysuj_wlasne(200, 160, 4).save("rysuj_wlasne.bmp")


# Zadanie 3

inicjaly = Image.open("inicjaly.bmp")
obraz_bazowy = Image.open("obraz_bazowy.bmp")


def wstaw_obraz_w_obraz(obraz_baz, obraz_wstawiany, m, n):
    tab_obraz_wstawiany = np.asarray(obraz_wstawiany).astype(np.uint8)
    tab_obraz_bazowy = np.asarray(obraz_baz).astype(np.uint8)
    h, w = tab_obraz_bazowy.shape
    h0, w0 = tab_obraz_wstawiany.shape
    tab = np.asarray(obraz_baz).astype(np.uint8)
    n_k = min(h, n + h0)
    m_k = min(w, m + w0)
    n_p = max(0, n)
    m_p = max(0, m)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab[i][j] = tab_obraz_wstawiany[i - n][j - m]
    tab = tab.astype(bool)
    return Image.fromarray(tab)


# wstaw_obraz_w_obraz(obraz_bazowy, inicjaly, 50, 10).show()

tablica = np.loadtxt("tablica.txt", dtype=np.uint8)
tablica = tablica.astype(bool)
tablica_obraz = Image.fromarray(tablica)
rysuj_ramke_w_obrazie(tablica_obraz, 40).save("ramka_w_obrazie.bmp")

wstaw_obraz_w_obraz(rysuj_paski_pionowe(300,200,15), inicjaly, 250, 100).save("obraz_w_obraz_1.bmp")
wstaw_obraz_w_obraz(rysuj_paski_pionowe(300,200,15), inicjaly, 0, 0).save("obraz_w_obraz_2.bmp")
