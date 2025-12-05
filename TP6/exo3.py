def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    return lst

print("Premier appel :", ajouter_elt())
print("Deuxième appel :", ajouter_elt())
print("Troisième appel :", ajouter_elt())

# avec chaînes de caractères

def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

print("\nPremier appel ajouter_carac() :", ajouter_carac())
print("Deuxième appel ajouter_carac() :", ajouter_carac())
print("Troisième appel ajouter_carac() :", ajouter_carac())
