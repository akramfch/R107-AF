import random
def generer(nbr, vmin, vmax):
    """Génère une liste de nbr entiers aléatoires entre vmin et vmax (inclus)."""
    tab = []
    for _ in range(nbr):
        tab.append(random.randint(vmin, vmax))
    return tab

def combienInferieur(table, vseuil):
    """Retourne le nombre d'éléments de table strictement inférieurs à vseuil."""
    c = 0
    for v in table:
        if v < vseuil:
            c += 1
    return c

nb = int(input("Combien de valeurs générer ? "))
vmin = int(input("Valeur minimale : "))
vmax = int(input("Valeur maximale : "))

choix = input("Voulez-vous préciser le seuil ? (O/N) : ")

if choix.upper() in ["O", "OUI"]:
    seuil = int(input("Seuil : "))
else:
    seuil = 30

tab = generer(nb, vmin, vmax)
tab.sort()

print("Tableau généré et trié :")
print(tab)

total = combienInferieur(tab, seuil)
print(f"Nombre de valeurs strictement inférieures à {seuil} :", total)
