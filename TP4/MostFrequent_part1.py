L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""
most_freq = 0
val_max = 0

for i in range(len(L1)):
    val = L1[i]
    freq = 0
    for j in range(len(L1)):
        if L1[j] == val:
            freq += 1
    if freq > most_freq:
        most_freq = freq
        val_max = val
print("Le nombre le plus frequent dans la liste est le :", val_max, f"({most_freq} x)")
""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""