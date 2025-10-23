from PIL import Image
import numpy as np

def zmien_kolor(kolor, zmiana):
    kolor[0] = (kolor[0] + zmiana) % 256
    kolor[1] = (kolor[1] + zmiana) % 256
    kolor[2] = (kolor[2] + zmiana) % 256
    return kolor


def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w,3)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    kolor = [50, 50, 50]
    for k in range(ile):
        for g in range(ile):
            i = k * grub + g
            for j in range(h):
                tab[j,i] = kolor
        zmien_kolor(kolor, zmiana_koloru)
    tab = tab * 255
    return Image.fromarray(tab)


rysuj_pasy_pionowe_szare(100, 180, 10, 50).show()