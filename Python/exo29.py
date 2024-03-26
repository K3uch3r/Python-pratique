N = int(input("Entrer un nombre: "))
Factorielle = 1
for i in range(1,N + 1):
    Factorielle *= i
print('La factorielle de', N, 'est: ', Factorielle)