import matplotlib
from PIL import Image, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

img = Image.open("obraz.png").convert("RGB")

# Zadanie 1


def filtruj(obraz, kernel, scale=1):
    obraz = np.array(obraz, dtype=np.float32)

    if obraz.ndim == 3:  # RGB
        kanaly = []
        for c in range(3):
            kanaly.append(konwolucja(obraz[:, :, c], kernel, scale))
        wynik = np.stack(kanaly, axis=2)
    else:
        wynik = konwolucja(obraz, kernel, scale)

    wynik = np.clip(wynik, 0, 255)
    return Image.fromarray(wynik.astype(np.uint8))


def konwolucja(channel, kernel, scale):
    k = np.array(kernel)
    size = k.shape[0]
    d = size // 2

    h, w = channel.shape
    temp = np.zeros_like(channel)

    for y in range(d, h - d):
        for x in range(d, w - d):
            fragment = channel[y-d:y+d+1, x-d:x+d+1]
            temp[y, x] = np.sum(fragment * k) / scale

    return temp


# Zadanie 2

blur_a = img.filter(ImageFilter.BLUR)

kernel_blur = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

blur_b = filtruj(img, kernel_blur, scale=9)

# Zadanie 3

contour_a = img.filter(ImageFilter.CONTOUR)

kernel_contour = [
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
]

contour_b = filtruj(img, kernel_contour, scale=1)

# Zadanie 4

img_L = img.convert("L")
emboss = img_L.filter(ImageFilter.EMBOSS)

sobel1 = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

sobel1_img = filtruj(img_L, sobel1, scale=1)


sobel2 = [
    [-1, -2, -1],
    [0,  0,  0],
    [1,  2,  1]
]

sobel2_img = filtruj(img_L, sobel2, scale=1)


def pokaz(obraz, tytul):
    plt.figure(figsize=(4,4))
    plt.imshow(obraz, cmap='gray')
    plt.title(tytul)
    plt.axis("off")
    plt.show()


pokaz(blur_a, "BLUR – gotowy")
pokaz(blur_b, "BLUR – konwolucja")

pokaz(contour_a, "CONTOUR – gotowy")
pokaz(contour_b, "CONTOUR – konwolucja")

pokaz(emboss, "EMBOSS")
pokaz(sobel1_img, "SOBEL 1")
pokaz(sobel2_img, "SOBEL 2")