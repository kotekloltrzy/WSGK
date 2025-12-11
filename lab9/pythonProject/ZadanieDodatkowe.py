import numpy as np
from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

obraz = Image.open("obraz.png")
filtr = np.ones(obraz.size)


def filtruj(image, kernel, scale):
    image = np.array(image)
    if len(image.shape) == 3 and image.shape[2] == 3:
        wynik = np.zeros_like(image)
        for c in range(3):
            wynik[:, :, c] = filtruj_kanal(image[:, :, c], kernel, scale)
    else:
        wynik = filtruj_kanal(image, kernel, scale)
    wynik_obraz = Image.fromarray(np.uint8(wynik))
    return wynik_obraz


def filtruj_kanal(image, kernel, scale):
    obraz_h, obraz_w = image.shape
    kernel_h, kernel_w = kernel.shape
    offset_h = kernel_h // 2
    offset_w = kernel_w // 2
    wynik = np.zeros_like(image)
    for i in range(offset_h, obraz_h - offset_h):
        for j in range(offset_w, obraz_w - offset_w):
            region = image[i - offset_h:i + offset_h + 1, j - offset_w:j + offset_w + 1]
            suma_wazona = np.sum(region * kernel)
            wynik[i, j] = suma_wazona / scale

    return wynik

zadanie1 = filtruj(obraz, filtr, 1)
zadanie1.show()