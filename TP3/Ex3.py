import random
x= random.randint(0, 100)
essais = 0
y = int(input("Devinez le nombre aléatoire :"))
while x !=y:
    essais +=1
    if y < x:
        print("La valeur est plus grande")
    elif y>x:
        print("La valeur est plus petite")

    y = int(input("Devinez le nombre aléatoire :"))
essais+=1
print ("Bien joué, vous avez trouvé la valeur après", essais,"essais")
