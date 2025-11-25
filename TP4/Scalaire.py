nMax = 10
v1 = []
v2 = []

n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
while n < 1 or n > nMax:
    print("La taille doit être comprise entre 1 et", nMax)
    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))


print("\nSaisie du premier vecteur :")
for i in range(n):
    val = int(input(f"v1[{i}] = "))
    v1.append(val)


print("\nSaisie du second vecteur :")
for i in range(n):
    val = int(input(f"v2[{i}] = "))
    v2.append(val)

scal = 0.0
for i in range(n):
    scal += v1[i] * v2[i]

print(f"\nLe produit scalaire de v1 par v2 vaut {scal}")