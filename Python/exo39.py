T = []
for i in range(10):
    nb = int(input("Entre un nombre: "))
    T.append(nb)
pair = []
impair = []
for nb in T:
    if (nb % 2) ==0:
        pair.append(nb)
    else:
        impair.append(nb)
print("Element pair: ", pair)
print('Element impair: ', impair)
    