from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

im = Image.open('pasy_3kolory.png')
print("tryb", im.mode)
print("format", im.format)
print("rozmiar", im.size)
w, h = im.size
im.show()

def usrednij_obraz(obraz):
    t  = np.asarray(obraz)
    tab = t.copy()
    srednie = t.mean(axis=(0, 1)).astype(np.uint8)
    print(srednie)
    for i in range(3):
        tab[:, :, i] = srednie[i]
    return Image.fromarray(tab)


im1 = usrednij_obraz(im)
im1.show()

statystyki(im)
statystyki(im1)

im2 = Image.open('beksinski.png')
print("tryb", im2.mode)
print("format", im2.format)
print("rozmiar", im2.size)
w, h = im2.size
im2.show()

statystyki(im2)

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()

def rysuj_histogram_L(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:])
    plt.show()

rysuj_histogram_RGB(im2)

hist = im2.histogram()
print("kanał r ", hist[0])
print("kanał g ", hist[0+256])
print("kanał b ", hist[0+2*256] )

# Kanały pobrane jako obrazy
r, g, b = im2.split()  # powstają obrazy
print("tryb kanału r: ", r.mode)
print("tryb kanału g: ", g.mode)
print("tryb kanału b: ", b.mode)

# przedstawienie 4 obrazów w jednym oknie plt
plt.figure(figsize=(16, 16))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im2)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(r, "gray")
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(g, "gray")
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(b, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('figura1.png')
plt.show()

rysuj_histogram_L(r)

# efekt przestawienia  kanałow
im3 = Image.merge('RGB', (b, r, g))
im3.show()

# własny obraz w trybie L jako kanał
w, h = im2.size
t = (h, w)
A = np.zeros(t, dtype=np.uint8)
A_im = Image.fromarray(A) # czarny obraz
im4 = Image.merge('RGB', (r, g, A_im))
im4.show()

# własny obraz w trybie L jako kanał - drugi przykład
def rysuj_kolo(w, h, r, m, n, kolor, kolor_tla): # koło o promieniu r i środku m, n, kolor = 0 lub 255
    t = (h, w) # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if (i-n)**2+(j-m)**2 < r**2: # wzór na koło o środku (m_s, n_s) i promieniu r
                tab[i, j] = kolor
            else:
                tab[i, j] = kolor_tla
    return tab


kolo_im = Image.fromarray(rysuj_kolo(363, 432,120,180,280, 150, 0))
im5 = Image.merge('RGB', (kolo_im, g, b))
im5.show()

diff = ImageChops.difference(im2,im5)
diff.show()

statystyki(diff)
