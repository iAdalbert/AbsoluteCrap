import time
import math
nazwapliku_z_x= r"pliki/plik_x.txt"
nazwapliku_z_y= r"pliki/plik_y.txt"

f1 = open(nazwapliku_z_x, "a")
f2 = open(nazwapliku_z_y, "a")

plik_z_nazwami = open(nazwapliku_z_nazwami, "r")
lista_nazw = plik_z_nazwami.readlines()

plik_nowy = open("plik_" + str(len(lista_nazw)) + ".txt", "x")

plik_nowy.write("Now the file has more content!")
plik_nowy.close()