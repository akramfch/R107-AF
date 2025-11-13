x = int(input("Entrez la valeur X :"))
somme=0
N=0
while somme+N <= x:
    somme+=N
    N+=1
N-=1
print("Le plus grand nombre N tel que la somme de 0 à N est inférieure à x est:", N)