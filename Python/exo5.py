# afficher le + grand des entiers

Num1 = int(input("Entrer un entier 1: "))
Num2 = int(input("Entrer un entier 2: "))
Num3 = int(input("Entrer un entier 3: "))

max = 0
if Num1 >= Num2 and Num1 >= Num3:
    max = Num1
elif Num2 >= Num1 and Num2 >= Num3:
    max = Num2
else:
    max = Num3
print("Valeur max: ", max)