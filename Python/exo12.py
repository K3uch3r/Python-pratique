# Afficher le mois selon le numero definit
num_mois = int(input("Entrez le numero représentant le mois : "))

correspondance_mois = {
    1: "Janvier",
    2: "Février",
    3: "Mars",
    4: "Avril",
    5: "Mai",
    6: "Juin",
    7: "Juillet",
    8: "Août",
    9: "Septembre",
    10: "Octobre",
    11: "Novembre",
    12: "Décembre"
}
if num_mois in correspondance_mois:
    print("Le mois correspondant est :", correspondance_mois[num_mois])