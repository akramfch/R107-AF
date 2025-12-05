import unicodedata

def enlever_accents(texte):
    """Retire les accents d'une chaîne de caractères."""
    nfkd = unicodedata.normalize("NFKD", texte)
    return "".join(c for c in nfkd if not unicodedata.combining(c))

def nettoyer(texte):
    """Met en minuscules, enlève accents et ne garde que les lettres."""
    t = texte.lower()
    t = enlever_accents(t)
    propre = ""
    for c in t:
        if c.isalpha():   # garde uniquement les lettres
            propre += c
    return propre

def est_palindrome(texte):
    """Retourne True si le texte est un palindrome (après nettoyage)."""
    t = nettoyer(texte)
    return t == t[::-1]

phrase = input("Entrez un mot ou une phrase : ")

if est_palindrome(phrase):
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")