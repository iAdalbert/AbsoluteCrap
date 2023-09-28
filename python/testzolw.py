from turtle import Turtle

t = Turtle()

nazwapliku_z_x= r"pliki/plik_x.txt"
nazwapliku_z_y= r"pliki/plik_y.txt"

f1 = open(nazwapliku_z_x, "r")
f2 = open(nazwapliku_z_y, "r")
lista_x = f1.readlines()
lista_y = f2.readlines()
i = 0
nowe_x = 0
nowe_y = 0
kontynuacja = 'c'

while True:
    if kontynuacja == 'c':
        t.clear()
        while i < len(lista_x):
            print(lista_x[i])
            print(lista_y[i])

            nowe_x = int(lista_x[i])*5
            nowe_y = int(lista_y[i])*5

            t.penup()
            t.setx(nowe_x)
            t.sety(nowe_y)
            t.pendown()

            for j in range(8):
                t.color("black")
                t.forward(2)
                t.left(45)
            i+=1
        print("'c' for continuation, 'e' for end of program")
        kontynuacja = input()
    elif kontynuacja == 'e':
        exit()
    else:
        print("Input proper value")