N = int(input("Entre un nombre: "))
for i in range(1, N+1):
    ligne = ""
    for x in range(1, i+1):
        ligne+= str(x) + " "
    print(ligne)