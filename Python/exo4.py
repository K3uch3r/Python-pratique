# afficher paire ou impaire

Num = int(input("Entrer un entier : "))
if (Num % 2) == 0:
    print("{0} est Paire".format(Num))
else:
    print("{0} est Impaire".format(Num))