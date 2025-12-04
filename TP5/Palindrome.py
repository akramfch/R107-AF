chaine = input("Entrez un mot ou une phrase : ")

# mettre en minuscules
chaine = chaine.lower()

# que les lettres
lettres = ""
for c in chaine:
    if c.isalpha():           # True si c est une lettre
        lettres += c

# test
inverse =  lettres[::-1]  # chaîne inversée

if lettres == inverse:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
