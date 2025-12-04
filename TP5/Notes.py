notes = []
coeffs = []

for i in range(5):
    saisie = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant : ")
    parties = saisie.split(" ")

    note = float(parties[0])         # note
    coef = float(parties[1])         # coefficient

    notes.append(note)
    coeffs.append(coef)

# calcul de la moyenne pondérée
numerateur = 0
denominateur = 0

for i in range(5):
    numerateur += notes[i] * coeffs[i]
    denominateur += coeffs[i]

moyenne = numerateur / denominateur

print("Moyenne générale :", moyenne)

# test d'admission
if moyenne > 10 and min(notes) >= 8:
    print("L'étudiant est admis.")
else:
    print("L'étudiant n'est pas admis.")
