#5)
prenom = input("Votre prénom : ")
nom = input("Votre nom : ")
promo = input("Votre promo : ")
groupe = input("Votre groupe : ")

etu1 = {
    "firstname": prenom,
    "name": nom,
    "promo": promo,
    "group": groupe
}
#6
"""d = {"name":"toto", "firstname":"titi", "promo":2022, "group":202}
print("Les clés du dictionnaire sont :")
for cle in d.keys():
    print("-", cle)

print("Les valeurs du dictionnaire sont :")
for val in d.values():
    print("-", val)

print("Les tuplets du dictionnaire sont :")
for item in d.items():
    print("-", item)"""

#7)
prenom2 = input("Prénom du deuxième étudiant : ")
nom2 = input("Nom du deuxième étudiant : ")
promo2 = input("Promo du deuxième étudiant : ")
groupe2 = input("Groupe du deuxième étudiant : ")

etu2 = {
    "firstname": prenom2,
    "name": nom2,
    "promo": promo2,
    "group": groupe2
}

# 8)
binome = {
    "login1": etu1,
    "login2": etu2
}

# 9)
print("\nLes étudiants formants le binôme sont : ")

print(f"- L’étudiant {binome['login1']['firstname']} {binome['login1']['name']} "
      f"du groupe {binome['login1']['group']}")

print(f"- L’étudiant {binome['login2']['firstname']} {binome['login2']['name']} "
      f"du groupe {binome['login2']['group']}")