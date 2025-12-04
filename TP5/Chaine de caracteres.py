T = input("Entrez une chaîne : ")

# 1) Taille de la chaîne
taille = 0
for c in T:
    taille += 1
print("Taille de la chaîne :", taille)

# 2) Pourcentage de voyelles
voyelles = "aeiouyAEIOUY"
nb_voyelles = 0
for c in T:
    if c in voyelles:
        nb_voyelles += 1

if taille > 0:
    pourcentage = nb_voyelles * 100 / taille
else:
    pourcentage = 0

print("Pourcentage de voyelles :", pourcentage, "%")

# 3) Tester si 'wagon' est une sous-chaîne de T
mot = "wagon"
lm = 0
for _ in mot:
    lm += 1

trouve = False
pos = -1

for i in range(taille - lm + 1):
    j = 0
    # comparer T[i+j] à mot[j] pour j de 0 à lm-1
    while j < lm and T[i + j] == mot[j]:
        j += 1
    if j == lm:
        trouve = True
        pos = i
        break

if trouve:
    print("Le mot 'wagon' est une sous-chaîne, première occurrence à la position", pos)
else:
    print("Le mot 'wagon' n'est pas une sous-chaîne.")

# 4) Nombre d'occurrences de 'wagon'
nb_occ = 0
for i in range(taille - lm + 1):
    j = 0
    while j < lm and T[i + j] == mot[j]:
        j += 1
    if j == lm:
        nb_occ += 1

print("Nombre d'occurrences de 'wagon' :", nb_occ)
