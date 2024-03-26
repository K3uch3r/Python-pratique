Max = None
for i in range(10):
    nbr = int(input("Entre un nombre :"))
    if Max is None or nbr > Max:
        Max = nbr
print("Le + grand est :", Max)