# Saisie des deux personnes
nom1 = input("Entrez le nom de la première personne : ")
prenom1 = input("Entrez le prénom de la première personne : ")

nom2 = input("Entrez le nom de la deuxième personne : ")
prenom2 = input("Entrez le prénom de la deuxième personne : ")

# Mise en forme : Prenom NOM
prenom1_format = prenom1.capitalize() + " " + nom1.upper()
prenom2_format = prenom2.capitalize() + " " + nom2.upper()

# Pour trier correctement, on compare les noms et prénoms en minuscules
cle1 = (nom1.lower(), prenom1.lower())
cle2 = (nom2.lower(), prenom2.lower())

if cle1 <= cle2:
    print(prenom1_format)
    print(prenom2_format)
else:
    print(prenom2_format)
    print(prenom1_format)
