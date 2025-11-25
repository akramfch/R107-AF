date = input("Entrez une date au format jjmmaaaa : ")

if len(date) != 8:
    print("Date incorrecte : jjmmaaaa (8 chiffres).")

jour = int(date[0:2])
mois = int(date[2:4])
annee = int(date[4:8])

if mois < 1 or mois > 12:
    print("Date incorrecte : mois compris entre 01 et 12.")

if mois in [1, 3, 5, 7, 8, 10, 12]:
    nb_jours = 31
elif mois in [4, 6, 9, 11]:
    nb_jours = 30
else:
    if (annee % 400 == 0):
        nb_jours = 29
    else:
        nb_jours = 28

if jour < 1 or jour > nb_jours:
    print("Date incorrecte : le jour n'est pas valide pour ce mois.")

else:
    print("Date correcte")