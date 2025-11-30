import matplotlib
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

# Zadanie 1

obraz = Image.open("obraz.jpg")
inicjaly = Image.open("inicjaly.bmp")

# Zadanie 2 a)


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def wstaw_inicjaly(im, podpis, m, n, kolor):
    temp = im.copy()
    w, h = im.size
    w0, h0 = podpis.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if podpis.getpixel((i, j)) == 0:
                temp.putpixel((i+m, j+n), (kolor[0], kolor[1], kolor[2]))
    return temp


obraz1 = obraz.copy()
wynik1 = wstaw_inicjaly(obraz1, inicjaly, 1948, 974, [255, 0, 0])
#wynik1.show()

# Zadanie 2 b)


def pobierz_kolor_pixela(im, m, n):
    w, h = im.size
    if m < w and n < h:
        kolor = im.getpixel((m, n))
    return kolor


def wstaw_inicjaly_maska(im, podpis, m, n):
    temp = im.copy()
    w, h = im.size
    w0, h0 = podpis.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if podpis.getpixel((i, j)) == 0:
                temp.putpixel((i + m, j + n), (255 - (pobierz_kolor_pixela(temp, i + m, j + n)[0]) % 255,
                                               255 - (pobierz_kolor_pixela(temp, i + m, j + n)[1]) % 255,
                                               255 - (pobierz_kolor_pixela(temp, i + m, j + n)[2]) % 225))
    return temp


obraz2 = obraz.copy()
wynik2 = wstaw_inicjaly_maska(obraz2, inicjaly, 1024, 512)
#wynik2.show()

# Zadanie 3


def wstaw_inicjaly_load(im, podpis, m, n, kolor):
    temp = im.copy()
    pixel_im = temp.load()
    pixel_pod = podpis.load()
    w, h = obraz.size
    w0, h0 = podpis.size
    for i in range(w0):
        for j in range(h0):
            if pixel_pod[i, j] == 0:
                x, y = i + m, j + n
                if x < w and y < h:
                    pixel_im[x, y] = kolor
    return temp


obraz3 = obraz.copy()
wynik3 = wstaw_inicjaly(obraz3, inicjaly, 1948, 974, [255, 0, 0])
#wynik3.show()


def wstaw_inicjaly_maska_load(im, podpis, m, n, x, y, z):
    temp = im.copy()
    pixel_im = temp.load()
    pixel_pod = podpis.load()
    w, h = temp.size
    w0, h0 = podpis.size
    for i in range(w0):
        for j in range(h0):
            if pixel_pod[i, j] == 0:
                k, l = i + m, j + n
                if k < w and l < h:
                    r, g, b = pixel_im[x, y]
                    pixel_im[k, l] = (255 - (r % x), 255 - (g % y), 255 - (b % z))
    return temp


obraz4 = obraz.copy()
wynik4 = wstaw_inicjaly_maska_load(obraz4, inicjaly, 1024, 512, 255, 255, 255)
#wynik4.show()

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(wynik1)
plt.title("Zad 2a")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(wynik2)
plt.title("Zad 2b")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(wynik3)
plt.title("Zad 3a")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(wynik4)
plt.title("Zad 3b")
plt.axis("off")

plt.tight_layout()
plt.savefig("fig1.png", dpi=300)
#plt.show()

# Zadanie 4 a)


def kotrast(oryginal, wsp_kontrastu):
    if wsp_kontrastu < 0 or wsp_kontrastu > 100:
        print("Współczynnik kontrastu przyjmuje wartości od 0 do 100")
        return 0
    temp = oryginal.copy()
    m = ((255 + wsp_kontrastu)/255)**2
    return temp.point(lambda i: 128 + (i - 128) * m)


obraz5 = obraz.copy()
wynik5 = kotrast(obraz5, 25)
#wynik5.show()
wynik6 = kotrast(obraz5, 50)
#wynik6.show()
wynik7 = kotrast(obraz5, 100)
#wynik7.show()

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(obraz)
plt.title("Oryginał")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(wynik5)
plt.title("Kontrast 25")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(wynik6)
plt.title("Kontrast 50")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(wynik7)
plt.title("Kontrast 100")
plt.axis("off")

plt.tight_layout()
plt.savefig("fig2.png", dpi=300)
#plt.show()

# Zadanie 4 b)


def transformacja_logarytmiczna(image):
    temp = image.copy()
    return temp.point(lambda i: 255 * np.log(1 + i/255))


obraz8 = obraz.copy()
wynik8 = transformacja_logarytmiczna(obraz8)
#wynik8.show()


def filtr_liniowy_point(image, a, b):
    return image.point(lambda i: i*a + b)


obraz9 = obraz.copy()
wynik9 = filtr_liniowy_point(obraz9, 2, 100)
#wynik9.show()

plt.figure(figsize=(8, 10))

plt.subplot(3, 1, 1)
plt.imshow(obraz)
plt.title("Oryginał")
plt.axis("off")

plt.subplot(3, 1, 2)
plt.imshow(wynik8)
plt.title("Transformacja Logarytmiczna")
plt.axis("off")

plt.subplot(3, 1, 3)
plt.imshow(wynik9)
plt.title("Filtr liniowy")
plt.axis("off")

plt.tight_layout()
plt.savefig("fig3.png", dpi=300)
#plt.show()


# Zadanie 4 c)

def transformacja_gamma(image, gamma):
    if gamma < 0 or gamma > 100:
        print("gamma kontrastu przyjmuje wartości od 0 do 100")
        return 0
    temp = image.copy()
    return temp.point(lambda i: (i/255)**(1/gamma)*255)


obraz10 = obraz.copy()
wynik10 = transformacja_gamma(obraz10, 0.5)
wynik11 = transformacja_gamma(obraz10, 5)
wynik12 = transformacja_gamma(obraz10, 10)
#wynik10.show()
#wynik11.show()
#wynik12.show()

plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.imshow(obraz)
plt.title("Oryginał")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(wynik10)
plt.title("Gamma 0.5")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(wynik11)
plt.title("Gamma 5")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(wynik12)
plt.title("Gamma 10")
plt.axis("off")

plt.tight_layout()
plt.savefig("fig4.png", dpi=300)
#plt.show()

# Zadanie 5


def transformacja_gamma_lista(image, gamma):
    if gamma < 0 or gamma > 100:
        print("gamma kontrastu przyjmuje wartości od 0 do 100")
        return 0
    temp = image.copy()
    lista = [int((i/255) ** (1 / gamma) * 255) for i in range(256)]
    if temp.mode == "RGB":
        lista = lista * 3
    return temp.point(lista)


obraz13 = obraz.copy()
wynik13 = transformacja_gamma_lista(obraz13, 0.5)
#wynik13.show()
obraz14 = obraz.copy()
wynik14 = transformacja_gamma(obraz14, 0.5)
#obraz14.show()

plt.figure(figsize=(8, 10))

plt.subplot(3, 1, 1)
plt.imshow(obraz)
plt.title("Oryginał")
plt.axis("off")

plt.subplot(3, 1, 2)
plt.imshow(wynik13)
plt.title("Gamma 0.5")
plt.axis("off")

plt.subplot(3, 1, 3)
plt.imshow(wynik14)
plt.title("Gamma lista 0.5")
plt.axis("off")

plt.tight_layout()
plt.savefig("fig5.png", dpi=300)
#plt.show()

# Zadanie 6 a)

obraz15 = obraz.copy()
obraz16 = obraz.copy()
T = np.array(obraz15, dtype='uint8')
T += 100
wynik15 = Image.fromarray(T, "RGB")
wynik16 = obraz16.point(lambda i: i+100)
#wynik15.show()
#wynik16.show()

# Dzieje się tak dlatego że NumPy uint8 stosuje modulo 256 a point zatrzymuje wartość na 255

# Zadanie 6 5)


def dodaj_100(image):
    d = np.array(image, dtype="uint16")
    d = d + 100
    d = np.clip(d, 0, 255)
    return Image.fromarray(d.astype("uint8"), "RGB")


obraz17 = obraz.copy()
wynik17 = dodaj_100(obraz17)
#wynik17.show()
