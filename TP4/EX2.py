# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
somme = 0.0;
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []
for i in range (nombreEtudiants):
    note=float(input(f"Note étudiant {i} :"))
    while note<0 or note>20:
        print("Erreur : la note doit être comprise entre 0 et 20 !")
        note= float(input(f"note etudiant {i} :"))
    notes.append(note)
    somme+=note
    moyenne = somme/nombreEtudiants
print("\nMoyenne de classe :,", moyenne)
print("\nNuméro de l'etudiant | note | ecart de la moyenne")
for i in range (nombreEtudiants):
    ecart =round(notes[i]-moyenne, 2)
    print (i, "|", notes[i], "|", ecart)
