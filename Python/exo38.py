N = int(input("Entre un nombre: "))
premier = True
if N <=1:
    premier = False
else:
    for i in range(2, N):
        if (N % i) == 0:
            premier = False
            break
if premier:
    print(N, "est premier")
else:
    print(N, "n'est pas un premier")