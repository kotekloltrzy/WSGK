import matplotlib
from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
import random
matplotlib.use('TkAgg')


# Zadanie 1 a)

im = Image.open("obraz.png")


def statystyki(image):
    s = stat.Stat(image)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


#print("tryb", im.mode)
#print("format", im.format)
#print("rozmiar", im.size)
#statystyki(im)


def rysuj_histogram_rgb(obraz):
    hist = obraz.histogram()
    plt.title("histogram  RGB")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()


#rysuj_histogram_rgb(im)


def rysuj_histogram_r(obraz):
    hist = obraz.histogram()
    plt.title("histogram  R")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.show()


def rysuj_histogram_g(obraz):
    hist = obraz.histogram()
    plt.title("histogram  G")
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.show()


def rysuj_histogram_b(obraz):
    hist = obraz.histogram()
    plt.title("histogram  B")
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()


#rysuj_histogram_r(im)
#rysuj_histogram_g(im)
#rysuj_histogram_b(im)

# Zadanie 1 b)


tabela = np.array(im)

kanal_r = tabela[:, :, 0]
kanal_g = tabela[:, :, 1]
kanal_b = tabela[:, :, 2]

r_ilosc = np.sum(kanal_r == 155)
g_ilosc = np.sum(kanal_g == 155)
b_ilosc = np.sum(kanal_b == 155)

#print(f"\nLiczba pikslei o wartości 155: \nR: {r_ilosc}\nG: {g_ilosc}\nB: {b_ilosc}")

# Zadanie 1 c)


def zlicz_piksele(obraz, kolor):
    tab = obraz.load()
    h, w = obraz.size
    ile = 0
    for i in range(h):
        for j in range(w):
            if tab[i, j] == kolor:
                ile += 1
    return ile


#print("\nW obrazie jest:", zlicz_piksele(im, (155, 155, 155)), "pikseli podanego koloru")

# Zadanie 2

im.save("obraz.jpg")
im_jpg = Image.open("obraz.jpg")

def zadanie2():
    print("\nStatystyki im:")
    statystyki(im)
    print("tryb", im.mode)
    print("format", im.format)
    print("rozmiar", im.size)
    w, h = im.size
    im.show()
    print("\nStatystyki im_jpg:")
    statystyki(im_jpg)
    print("tryb", im_jpg.mode)
    print("format", im_jpg.format)
    print("rozmiar", im_jpg.size)
    im_jpg.show()


#zadanie2()

# Zadanie 2 b)

def zadanie2b():
    diff = ImageChops.difference(im, im_jpg)
    diff.show()
    print("\nStatystyki diff:")
    statystyki(diff)
    print("tryb", diff.mode)
    print("format", diff.format)
    print("rozmiar", diff.size)


#zadanie2b()

# Zadanie 2 c)


im_jpg.save("obraz2.jpg")
im_jpg2 = Image.open("obraz2.jpg")
im_jpg2.save("obraz3.jpg")
im_jpg3 = Image.open("obraz3.jpg")

diff2 = ImageChops.difference(im_jpg, im_jpg3)
#diff2.show()
#print("\nStatystyki diff2:")
#statystyki(diff2)
#print("tryb", diff2.mode)
#print("format", diff2.format)
#print("rozmiar", diff2.size)


# Zadanie 3 a)


tab_r, tab_g, tab_b = im.split()

#tab_r.save("im_r.png")
#tab_g.save("im_g.png")
#tab_b.save("im_b.png")

# Zadanie 3 b)

im1 = Image.merge('RGB', (tab_r, tab_g, tab_b))
#im1.show()
im1.save("im1.png")
diff3 = ImageChops.difference(im, im1)
#diff3.show()
diff3.save("diff3.png")

# Zadanie 3 c)

plt.figure(figsize=(16, 8))
plt.subplot(2, 2, 1)
plt.imshow(im)
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(im1, "gray")
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(diff3, "gray")
plt.axis('off')
plt.savefig('figura1.png')
plt.show()

# Zadanie 4 a)


def negatyw(obraz):
    tab = np.asarray(obraz)
    if len(tab.shape) == 2:
        h, w = tab.shape
    elif len(tab.shape) == 3:
        h, w, c = tab.shape
    tab_neg = tab.copy()
    if obraz.mode == "1":
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 1 - tab[i, j]
        return Image.fromarray(tab_neg)
    elif obraz.mode == "L" or obraz.mode == "RGB":
        for i in range(h):
            for j in range(w):
                tab_neg[i, j] = 255 - tab[i, j]
        return Image.fromarray(tab_neg)
    else:
        return "Zły format obrazu"


def mieszaj_kanaly(obraz):
    t_r, t_g, t_b = obraz.split()
    n_r = negatyw(t_r)
    n_g = negatyw(t_g)
    n_b = negatyw(t_b)
    choice_list = [t_r, t_g, t_b, n_r, n_g, n_b]
    rng_list = (random.choice(choice_list), random.choice(choice_list), random.choice(choice_list))
    rng_image = Image.merge('RGB', rng_list)
    return rng_image


mix = mieszaj_kanaly(im)
#mix.show()
mix.save("mix.png")

# Zadanie 4 b)


def rozpoznaj_mix(obraz, mieszany):
    o_r, o_g, o_b = obraz.split()
    oryg_kanaly = [
        ("r", np.asarray(o_r)),
        ("g", np.asarray(o_g)),
        ("b", np.asarray(o_b)),
        ("negatyw r", np.asarray(negatyw(o_r))),
        ("negatyw g", np.asarray(negatyw(o_g))),
        ("negatyw b", np.asarray(negatyw(o_b)))
    ]
    m_r, m_g, m_b = mieszany.split()
    mix_kanaly = [
        ("mix R", np.asarray(m_r)),
        ("mix G", np.asarray(m_g)),
        ("mix B", np.asarray(m_b))
    ]
    wynik = []
    for nazwa_mix, mix in mix_kanaly:
        for nazwa_org, org in oryg_kanaly:
            if np.array_equal(mix, org):
                wynik.append(f"{nazwa_mix} = {nazwa_org}")
                break
    return "\n".join(wynik)


#print(rozpoznaj_mix(im, mix))

beksinski = Image.open("beksinski.png")
beksinski1 = Image.open("beksinski1.png")
beksinski2 = Image.open("beksinski2.png")
beksinski3 = Image.open("beksinski3.png")

# Zadanie 6


def ocen_czy_identyczne(obraz1, obraz2):
    if obraz1.mode != obraz2.mode:
        return "Obrazy nie są identyczne ponieważ mają różne tryby"
    if obraz1.size != obraz2.size:
        return "Obrazy nie są identyczne ponieważ mają rózny rozmiar"
    tab_1 = np.asarray(obraz1)
    tab_2 = np.asarray(obraz2)
    if not np.array_equal(tab_1, tab_2):
        return "Obraz nie są identyczne ponieważ mają różne piksele"
    return "Obrazy są identyczne"


print(ocen_czy_identyczne(beksinski, beksinski1))
print(ocen_czy_identyczne(beksinski, beksinski2))
print(ocen_czy_identyczne(beksinski, beksinski3))

# Zadanie 7


def pokaz_roznice(obraz_wejsciowy):
    r, g, b = obraz_wejsciowy.split()
    r_stat = stat.Stat(r)
    g_stat = stat.Stat(g)
    b_stat = stat.Stat(b)
    r_max = r_stat.extrema[0][1]
    g_max = g_stat.extrema[0][1]
    b_max = b_stat.extrema[0][1]
    r_skal = r.point(lambda x: (x/r_max) * 255)
    g_skal = g.point(lambda x: (x/g_max) * 255)
    b_skal = b.point(lambda x: (x/b_max) * 255)
    obraz_wynikowy = Image.merge('RGB', (r_skal, g_skal, b_skal))
    return obraz_wynikowy


diff4 = ImageChops.difference(im, im_jpg3)
diff4.save("diff4.png")

plt.figure(figsize=(16, 8))
plt.subplot(2, 2, 1)
plt.imshow(im)
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(im_jpg3, "gray")
plt.axis('off')
plt.subplot(2, 2, 3)
plt.imshow(diff4, "gray")
plt.axis('off')
plt.subplot(2, 2, 4)
plt.imshow(pokaz_roznice(diff4), "gray")
plt.axis('off')
plt.savefig('fig2.png')
#plt.show()

# Zadanie 8

inicjaly = Image.open("inicjaly.bmp")

def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n, kolor):
    tab_obraz_wstawiany = np.asarray(obraz_wstawiany).astype(np.uint8)
    wstawiane = np.asarray(obraz_bazowy).astype(np.uint8)
    h, w, _ = wstawiane.shape
    h0, w0 = tab_obraz_wstawiany.shape
    tab = np.asarray(obraz_bazowy).astype(np.uint8)
    n_k = min(h, n + h0)
    m_k = min(w, m + w0)
    n_p = max(0, n)
    m_p = max(0, m)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            piksel = tab_obraz_wstawiany[i - n, j - m]
            if piksel == 0:
                wstawiane[i, j] = kolor
    return Image.fromarray(wstawiane)


wstaw_inicjaly(wstaw_inicjaly(wstaw_inicjaly(im, inicjaly, 2002, 487, (200, 50, 150)), inicjaly, 0, 974, (150, 200, 50)), inicjaly, 1948, 0, (50, 150, 200)).save("obraz_inicjaly.png")

# Zadanie 9


def odkoduj(obraz1, obraz2):
    tab1 = np.asarray(obraz1).astype(np.int16)
    tab2 = np.asarray(obraz2).astype(np.int16)

    if tab1.shape != tab2.shape:
        return "Obrazy mają różne wymiary — nie można porównać."

    if tab1.ndim == 3:
        diff = np.any(tab1 != tab2, axis=2).astype(np.uint8) * 255
    else:
        diff = (tab1 != tab2).astype(np.uint8) * 255

    return Image.fromarray(diff, mode="L")


oryg = Image.open("jesien.jpg")
zakod = Image.open("zakodowany1.bmp")

kod2 = odkoduj(oryg, zakod)
kod2.save("kod2.bmp")
kod2.show()
