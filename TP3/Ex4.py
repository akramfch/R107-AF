n=int(input("Entrez un entier n :"))

print("Choisissez la boucle :")
print("1 - Boucle FOR")
print("2 - boucle WHILE")
choix=int(input("Quel choix ?"))
fact=1
if choix==1:
    print("Choix de la boucle FOR")
    for i in range (1, n+1):
        fact*=i
        print(f"Après l'utilisation de la boucle FOR la factorielle de {n} vaut {fact}")
elif choix==2:
    print("Choix de la boucle WHILE")
    i=1
    while i<=n:
        fact*=i
        print(f"Après l'utilisation de la boucle WHILE la factorielle de {n} vaut {fact}")
        i+=1
print(f"La factorielle de {n} vaut donc {fact}")