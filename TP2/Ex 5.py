nb = int(input("Entrez un nombre entier :"))
if nb > 0:
    if nb % 2 == 0:
        print("Le nombre est positif et pair")
    else:
        print("Le nombre est positif et impair")
elif nb < 0:
        if nb % 2 == 0:
            print ("Le nombre est négatif et pair")
        else:
            print("le nombre est négatif et impair")
else :
    print ("Le nombre est zéro (et il est pair)")
