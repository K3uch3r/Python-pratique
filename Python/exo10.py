# Calcul de Prix TTC avec remise 15%

prixHT =  float(input("Entrer le montant HT: "))
prixTTC = prixHT + prixHT*0.2
if  prixTTC > 200:
    prixTTC = prixTTC - prixTTC*0.15
    print("le montant TTC aprés remise est: ",prixTTC)
else:
    print("le montant TTC aprés remise est: ",prixTTC)