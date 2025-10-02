from PIL import Image
import numpy as np

# Zadanie 2

obrazek = Image.open("inicjaly.bmp")
print("Informacje o obrazie")
print("Tryb: ", obrazek.mode)
print("Format: ", obrazek.format)
print("Rozmiar: ", obrazek.size)

# Zadanie 3

dane_obrazka = np.asarray(obrazek)
dane_obrazka1 = dane_obrazka.astype(np.uint8)
print(dane_obrazka1)

inicjaly_text = open('inicjaly.txt', 'w')
for rows in dane_obrazka1:
    for item in rows:
        inicjaly_text.write(str(item) + ' ')
    inicjaly_text.write('\n')

inicjaly_text.close()

# Zadanie 4

print("wartość pikslea 25,25: ", dane_obrazka[25][25])
print("wartość pikslea 50,30: ", dane_obrazka[30][50])
print("wartość pikslea 90,40: ", dane_obrazka[40][90])
print("wartość pikslea 99,0: ", dane_obrazka[0][99])

# Zadanie 5

inicjaly_bool = np.loadtxt("inicjaly.txt", dtype=np.bool_)
print(inicjaly_bool)

# Zadanie 6

inicjaly_uint8 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
print(inicjaly_uint8)

ob_uint8 = Image.fromarray(inicjaly_uint8)
ob_uint8.show()

# Zadanie 7

obrazek_png = Image.open("inicjaly.png")
print("---------- informacje o obrazie")
print("tryb:", obrazek_png.mode)
print("format:", obrazek_png.format)
print("rozmiar:", obrazek_png.size)
