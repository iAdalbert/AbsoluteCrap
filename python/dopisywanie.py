nazwapliku_z_x= r"pliki/plik_x.txt"
nazwapliku_z_y= r"pliki/plik_y.txt"

f1 = open(nazwapliku_z_x, "a")
f2 = open(nazwapliku_z_y, "a")

kontynuacja = 'c'
nowe_x = '0'
nowe_y = '0'

while True:
    if kontynuacja == 'c':
        print("Input new x")
        nowe_x = "\n"+input()
        print("Input new y")
        nowe_y = input()
        f1.write(nowe_x)
        f2.write("\n"+nowe_y)
        print("'c' for continuation, 'e' for end of program")
        kontynuacja = input()
    elif kontynuacja == 'e':
        exit()
    else:
        print("Input proper value")