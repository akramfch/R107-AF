val1 = 0
val2 = 0
val3 = 0
for i in range (10):
    x=float(input("Entrez une valeur comprise entre 0 et 20:"))
    if x < 10:
        val1 += 1
    elif x < 15:
        val2 += 1
    else:
        val3 += 1

    while x<0 or x>20:
        print("Valeur hors intervalle !")
        x = float(input("Entrez une valeur comprise entre 0 et 20:"))
print("valeurs <10:", val1)
print("valeurs >=10 et <15:", val2)
print("valeurs =>15:", val3)