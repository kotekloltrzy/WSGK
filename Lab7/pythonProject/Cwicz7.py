from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

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
    for i,j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if podpis.getpixel((i, j)) == 0:
                temp.putpixel((i+m, j+n), (kolor[0], kolor[1], kolor[2]))
    return temp

obraz1 = obraz.copy()
wstaw_inicjaly(obraz1, inicjaly, 1948, 974, [255, 0, 0]).show()

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
    for i,j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if podpis.getpixel((i, j)) == 0:
                temp.putpixel((i + m, j + n), (255 - (pobierz_kolor_pixela(temp, i + m, j + n)[0]) % 255,
                                               255 - (pobierz_kolor_pixela(temp, i + m, j + n)[1]) % 255,
                                               255 - (pobierz_kolor_pixela(temp, i + m, j + n)[2]) % 225))
            return temp


obraz2 = obraz.copy()
wstaw_inicjaly_maska(obraz2, inicjaly, 1024, 512).show()

# Zadanie 3

def wstaw_inicjaly_load(im, podpis, m, n, kolor): # zamienić tak by używało load
    temp = im.copy()
    w, h = im.size
    w0, h0 = podpis.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if podpis.getpixel((i, j)) == 0:
                temp.putpixel((i + m, j + n), (kolor[0], kolor[1], kolor[2]))
    return temp


obraz1 = obraz.copy()
wstaw_inicjaly(obraz1, inicjaly, 1948, 974, [255, 0, 0]).show()


def wstaw_inicjaly_maska_load(im, podpis, m, n, x, y, z): # zamienić tak by używało load
    temp = im.copy()
    w, h = im.size
    w0, h0 = podpis.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if podpis.getpixel((i, j)) == 0:
                temp.putpixel((i + m, j + n), x, y, z)
    return temp


obraz2 = obraz.copy()
wstaw_inicjaly_maska_load(obraz2, inicjaly, 1024, 512, 50, 150, 200).show()
