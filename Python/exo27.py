table = []
for i in range(10):
    nb = input("Entre un nombre: ")
    table.append(nb)
N = int(input("Entrez l'élément : "))
Occurrences = 0
for element in table:
    if element == N:
        Occurrences+=1
print("Le nombre d'occurrences de", N, "dans le tableau est :", Occurrences)