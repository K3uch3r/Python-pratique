occurrences = 0
while True:
    inp = int(input("Entrez un entier (0 pour terminer) : "))
    if inp == 0:
        break

    while inp > 0:
        if inp % 10 == 5:
            occurrences += 1
        inp //= 10

print("Le nombre d'occurrences de 5 dans la suite est :", occurrences)