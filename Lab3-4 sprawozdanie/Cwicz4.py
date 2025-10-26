from PIL import Image
import numpy as np

# Zadanie 5


def zmien_kolor(kolor, zmiana):
    kolor[0] = (kolor[0] + zmiana) % 256
    kolor[1] = (kolor[1] + zmiana) % 256
    kolor[2] = (kolor[2] + zmiana) % 256
    return kolor


def rysuj_pasy_pionowe_szare(w, h, grub, kolor_tlo, kolor_pas):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    tab[:] = kolor_pas
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                if k % 2 == 0:
                    tab[j, i] = kolor_tlo
    return tab


red = rysuj_pasy_pionowe_szare(300, 200, 10, 150, 255)
green = rysuj_pasy_pionowe_szare(300, 200, 18, 150, 255)
blue = rysuj_pasy_pionowe_szare(300, 200, 26, 150, 255)

obrazek = np.zeros((200, 300, 3), dtype=np.uint8)


def rysuj_pasy_kolorowe():
    for i in range(300):
        for j in range(200):
            obrazek[j, i, 0] = (obrazek[j, i, 0] + red[j, i]) % 255
            obrazek[j, i, 1] = (obrazek[j, i, 1] + green[j, i]) % 255
            obrazek[j, i, 2] = (obrazek[j, i, 2] + blue[j, i]) % 255
    return obrazek


#Image.fromarray(rysuj_pasy_kolorowe()).show()
#Image.fromarray(rysuj_pasy_kolorowe()).save("obraz6.png")

# Zadanie 6


def rysuj_po_skosie_szare(h, w, a, b):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a*i + b*j) % 256
    return Image.fromarray(tab)


canal_a = rysuj_po_skosie_szare(200, 300, 6, 5)
rgb = rysuj_pasy_kolorowe()

a_ext = np.expand_dims(canal_a, axis=-1)

combined = np.concatenate((rgb, a_ext), axis=-1)
#obraz7 = Image.fromarray(combined)
#obraz7.show()
#obraz7.save("obraz7.png")

# Zadanie 7


def rgb_to_cmyk(rgb_array):
    rgb = rgb_array.astype(float) / 255
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    k = 1 - np.max(rgb, axis=2)
    c = (1 - r - k) / (1 - k + 1e-8)
    m = (1 - g - k) / (1 - k + 1e-8)
    y = (1 - b - k) / (1 - k + 1e-8)
    c[np.isnan(c)] = 0
    m[np.isnan(m)] = 0
    y[np.isnan(y)] = 0
    cmyk = np.stack((c, m, y, k), axis=2) * 255
    return cmyk.astype(np.uint8)


t_cmyk = rgb_to_cmyk(rysuj_pasy_kolorowe())
image_cmyk = Image.fromarray(t_cmyk, mode="CMYK")
#image_cmyk.show()
#image_cmyk.save("obraz8.tiff")


def kanal_r(obraz):
    tab = np.zeros((200, 300, 3), dtype=np.uint8)
    for i in range(300):
        for j in range(200):
            tab[j, i, 0] = obraz[j, i, 0]
    return tab


#Image.fromarray(kanal_r(rysuj_pasy_kolorowe())).show()
#Image.fromarray(kanal_r(rysuj_pasy_kolorowe())).save("r.png")


def kanal_c(obraz):
    tab = np.zeros((200, 300, 4), dtype=np.uint8)
    for i in range(300):
        for j in range(200):
            tab[j, i, 0] = obraz[j, i, 0]
    return tab


#Image.fromarray(kanal_c(t_cmyk), mode="CMYK").show()
#Image.fromarray(kanal_c(t_cmyk), mode="CMYK").save("c.tiff")
