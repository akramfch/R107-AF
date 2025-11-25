x = float(input("Vous chercher la table de multiplication de quel nombre ?"))
resultats = []
for i in range (10):
    resultats.append(x*i)

for i in range (10):
     produit= round(resultats[i],1)
     print(x, "*", i,"=", produit)