from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('baby_yoda.jpg')
print("tryb obrazu", im.mode)
print("rozmiar", im.size)
im.show()

def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]

def pobierz_kolor_pixela(obraz, m, n):  # m, n współrzędne punktu na obrazie
    w, h = obraz.size
    if m < w and n < h:
        kolor = obraz.getpixel((m, n))
    return kolor


print(pobierz_kolor_pixela(im, 260, 200))

def wstaw_pixel_w_punkt(obraz, m, n, kolor):  # m, n współrzędne punktu na obrazie, kolor -  dane pixela do wstawienia
    w, h = obraz.size
    if m < w and n < h:
        obraz.putpixel((m, n), kolor)
    return obraz


def wstaw_pixel_w_zakresie(obraz, m, n, kolor, w_z, h_z):  # w miejscu m,n wstawia prostokąt o bokach w_z, h_z
    w, h = obraz.size
    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            obraz.putpixel((i + m, j + n), kolor)
    return obraz

im1 = im.copy()
wstaw_pixel_w_zakresie(im1, -20, -100, (255, 255, 0), 100, 200)

def rozjasnij_obraz_w_zakresie(obraz, m, n, a, b, c, w_z, h_z):  # w miejscu m,n "rozjaśnia" prostokat o wymiarach w_z, h_z
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            p = obraz.getpixel((i + m, j + n))
            obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
    return obraz1

im2 = im.copy()
rozjasnij_obraz_w_zakresie(im2, 300, -20, -100, 50, -40, 100, 200).show()

def skopiuj_obraz_w_zakresie(obraz, m, n, m1, n1, w_z, h_z):  # kopiuje prostokat o wymiarach w_z, h_z z miejsca m,n i wstawia w miejscu m1,n1
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w_z, h_z):
        if i+m < w and j+n < h:
            p = obraz.getpixel((i + m, j + n))
            if i + m1 < w and j + n1 < h:
                obraz1.putpixel((i + m1, j + n1), p)
    return obraz1

def rozjasnij_obraz_z_maska(obraz, maska, m, n, a, b, c):  # w miejscu m, n zmienia tylko te pixele, które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = maska.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if maska.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
    return obraz1

im4 = im.copy()
maska = Image.open('gwiazdka.bmp')
rozjasnij_obraz_z_maska(im4, maska, 270, 0, 20, -50, 80).show()

def dodaj_szum(obraz, n, kolor1, kolor2):  # dodawanie szumu typu salt and pepper
    w, h = obraz.size
    x, y = np.random.randint(0, w, n), np.random.randint(0, h,
                                                         n)  # powtarza n razy losowanie z zakresu 0,w i z zakresu 0,h
    for (i, j) in zip(x, y):  # zip robi pary z list x,y
        obraz.putpixel((i, j), (kolor1 if np.random.rand() < 0.5 else kolor2))  # salt-and-pepper
    return obraz

im5 = im.copy()
dodaj_szum(im5, 10000, (255,255,0), (0,0,255)).show()

def zastosuj_funkcje(image, func):
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = func(pixele[i, j])

def przestaw_kolory(pixel):
    return pixel[1], pixel[2], pixel[0]

im6 = im.copy()
zastosuj_funkcje(im6, przestaw_kolory)
im6.show()

def filtr_liniowy(image, a, b): # a, b liczby całkowite
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = (pixele[i, j][0]* a + b, pixele[i, j][1]* a + b, pixele[i, j][2]* a + b)

im7 = im.copy()
filtr_liniowy(im7, 2, -50)
im7.show()

def filtr_liniowy_point(image, a, b):
    return image.point(lambda i: i*a + b)

im8 = im.copy()
filtr_liniowy_point(im8, 2, -50).show()

filtr_liniowy_point(im8, 1, 100).show() # rozjaśnia każdy piksel o 100

def utworz_negatyw(image):
    return image.point(lambda i: 255 - i)
utworz_negatyw(im8).show()

def efekt_plakatu(image, wsp):
    return image.point(lambda i: i > wsp and 255)  # jeżeli nieprawda, że i > wsp wstaw 0 a w przeciwnym przypadku wstaw 255

def efekt_plakatu_lista(image, wsp):
    listaL = [0 if i <= wsp else 255 for i in range(256)]
    listaRGB = listaL + listaL + listaL
    return image.point(listaRGB)

efekt_plakatu(im8, 120).show()

efekt_plakatu_lista(im8, 120).show()

# dlaczego poniższa funkcja nie rozjasnia obrazu tak jak "filtr_liniowy_point(image, 1, 100)"

def rozjasnij(image, b):
    im = image.copy()
    T = np.array(im, dtype='uint8')
    T += b
    return Image.fromarray(T, "RGB")

rozjasnij(im8, 100).show()

