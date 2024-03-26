M = int(input("Entre le nombre: "))
N = int(input("Entre le nombre: "))
PGCD = 1  
mini = min(M,N)
for i in range(1, mini+1):
    if (M % i) == 0 and (N %i) == 0:
        PGCD += i

print("Le PGCD de", M, "et", N, "est :", PGCD)