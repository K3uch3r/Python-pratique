somme = []
for i in range(10):
    nombre = float(input("Entrer un nombre: "))
    somme.append(nombre)
sommes = sum(somme)
moyenne = sommes / len(somme)
print("La moyenne est :", moyenne)