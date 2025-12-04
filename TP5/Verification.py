import os.path
import datetime

f1 = input("Entrez le nom du premier fichier : ")
f2 = input("Entrez le nom du deuxième fichier : ")

if not os.path.isfile(f1):
    print(f"Le fichier {f1} n'existe pas.")
else:
    taille1 = os.path.getsize(f1)
    modif1 = os.path.getmtime(f1)
    print(f"Taille de {f1} :", taille1, "octets")
    date1 = datetime.datetime.fromtimestamp(modif1)
    print("Dernière modification de", f1, ":", date1)

if not os.path.isfile(f2):
    print(f"Le fichier {f2} n'existe pas.")
else:
    taille2 = os.path.getsize(f2)
    modif2 = os.path.getmtime(f2)
    print(f"Taille de {f2} :", taille2, "octets")
    date2 = datetime.datetime.fromtimestamp(modif2)
    print("Dernière modification de", f2, ":", date2)

# Comparer seulement si les deux existent
if os.path.isfile(f1) and os.path.isfile(f2):
    if modif1 > modif2:
        print(f"{f1} est le fichier le plus récent.")
    elif modif2 > modif1:
        print(f"{f2} est le fichier le plus récent.")
    else:
        print("Les deux fichiers ont la même date de modification.")
