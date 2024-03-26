N = int(input("Entre un nombre: "))
somme = 0
for i in range(1, N+1):
    if (i %2) != 0:
        somme+=i
print("La somme des entiers impairs de 1 à", N, "est :", somme)