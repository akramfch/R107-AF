# a) Création liste
L1 = [0] * 3
print("L1 =", L1)
print("type(L1) =", type(L1))
print("id(L1) =", id(L1))
# b)
print("\nÉléments de L1 avant modification :")
for elt in L1:
    print("valeur :", elt, "| type :", type(elt), "| id :", id(elt))

# c) Modification
L1[1] += 1
print("\nL1 après modification de L1[1] :")
print("L1 =", L1)
print("id(L1) =", id(L1))

print("\nÉléments de L1 après modification :")
for elt in L1:
    print("valeur :", elt, "| id :", id(elt))

# e)
s = "machaine"
print("\nChaîne s :", s)
print("id(s) =", id(s))

print("\nÉléments de s :")
for c in s:
    print("caractère :", c, "| id :", id(c))
