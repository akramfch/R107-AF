login1 = input("Login du premier étudiant : ")
login2 = input("Login du second étudiant : ")

binome = (login1, login2)

print(f"L’étudiant {binome[0]} est en binome avec l’étudiant {binome[1]}")

#nouveaulogin2 = input("Nouveau login pour le second étudiant : ")
#[1] = nouveau_login2
#Ceci ne marche pas car un tuplet est immuable
#del aussi ne marche pas
#pour pouvoir ajouter un trinome il faut créer un nouveau tuplet car on ne peut pas le modifier