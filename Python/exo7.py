# Demander deux Nb M et N et informaer sur le signe de leur produit

M = int(input("Entrer un nombre: "))
N = int(input("Entrer un nombre: "))
produit = M + N
if produit >= 0:
    print("Positif")
elif produit <= 0:
    print("Négatif")
else:
    print("Nul")