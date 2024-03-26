table = []
for i in range(1, 11):
    num = int(input("Entre un nombre: "))
    table.append(num)
pair = 0
impair = 0
for num in table:
    if (num % 2) == 0:
        pair+=1
    else:
        impair+=1
print("Nombre element Pair :", pair, "et Nombre element Impair :", impair)