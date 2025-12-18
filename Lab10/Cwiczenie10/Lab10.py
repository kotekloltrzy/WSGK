from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps
from PIL import ImageStat as stat

obraz = Image.open("obraz.jpg")

def statystyki(im):
    print("tryb obrazu", im.mode)
    print("rozmiar obrazu", im.size)
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

def statystyki_z_maska(im, maska):
    print("tryb obrazu", im.mode,  "tryb maski",  maska.mode)
    print("rozmiar obrazu", im.size, "rozmiar maski", maska.size)
    s = stat.Stat(im, mask = maska)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

def zadanie1(image):
    print("\n Zadanie 1 \n")
    w, h = image.size
    temp = image
    s_w = 0.15
    s_h = 0.27
    w0 = int(w*s_w)
    h0 = int(h*s_h)
    im1 = temp.resize((w0, h0), reducing_gap=None, resample=0)
    im2 = temp.resize((w0, h0), reducing_gap=None, resample=1)
    im3 = temp.resize((w0, h0), reducing_gap=None, resample=2)
    im4 = temp.resize((w0, h0), reducing_gap=None, resample=3)
    im5 = temp.resize((w0, h0), reducing_gap=None, resample=4)
    im6 = temp.resize((w0, h0), reducing_gap=None, resample=5)
    im7 = ImageChops.difference(im1, im2)
    im8 = ImageChops.difference(im1, im3)
    im9 = ImageChops.difference(im1, im4)
    im10 = ImageChops.difference(im1, im5)
    im11 = ImageChops.difference(im1, im6)
    plt.figure(figsize=(8,12))
    plt.subplot(6, 2, 1)
    plt.imshow(im1)
    plt.title("NEAREST")
    plt.axis("off")
    plt.subplot(6, 2, 3)
    plt.imshow(im2)
    plt.title("LANCZOS")
    plt.axis("off")
    plt.subplot(6, 2, 4)
    plt.imshow(im7)
    plt.title("LANCZOS różnice")
    plt.axis("off")
    plt.subplot(6, 2, 5)
    plt.imshow(im3)
    plt.title("BILINEAR")
    plt.axis("off")
    plt.subplot(6, 2, 6)
    plt.imshow(im8)
    plt.title("BILINEAR różnice")
    plt.axis("off")
    plt.subplot(6, 2, 7)
    plt.imshow(im4)
    plt.title("BICUBIC")
    plt.axis("off")
    plt.subplot(6, 2, 8)
    plt.imshow(im9)
    plt.title("BICUBIC różnice")
    plt.axis("off")
    plt.subplot(6, 2, 9)
    plt.imshow(im5)
    plt.title("BOX")
    plt.axis("off")
    plt.subplot(6, 2, 10)
    plt.imshow(im10)
    plt.title("BOX różnice")
    plt.axis("off")
    plt.subplot(6, 2, 11)
    plt.imshow(im6)
    plt.title("HAMMING")
    plt.axis("off")
    plt.subplot(6, 2, 12)
    plt.imshow(im11)
    plt.title("HAMMING różnice")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("fig1.png")
    plt.show()
    print(statystyki(im7))
    print(statystyki(im8))
    print(statystyki(im9))
    print(statystyki(im10))
    print(statystyki(im11))

zadanie1(obraz)

def zadanie2(image):
    print("\n Zadanie 2 \n")
    temp = image
    w_p = 600
    h_p = 100
    w_k = 1000
    h_k = 400
    wycinek = (w_p, h_p, w_k, h_k)
    wyc_w = wycinek[2] - wycinek[0]
    wyc_h = wycinek[3] - wycinek[1]
    s_w = 2
    s_h = 3
    glowa = temp.resize((s_w * wyc_w, s_h * wyc_h), box = wycinek, resample=0)
    glowa.show()

    glowa_crop = temp.crop(wycinek)
    w = 400
    h = 300
    w0 = int(w*s_w)
    h0 = int(h*s_h)
    glowa_resize = glowa_crop.resize((w0,h0), resample=0)
    glowa_resize.show()

    roznice = ImageChops.difference(glowa, glowa_resize)
    roznice.show()
    print(statystyki(roznice))

zadanie2(obraz)