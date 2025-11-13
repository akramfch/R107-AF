hstart=int(input("Donnez l’heure de début de la location (un entier) :"))
hfin=int(input("Donnez l’heure de fin de la location (un entier) :"))
if hstart<0 or hstart>24 or hfin<0 or hfin>24:
    print("Les heures doivent être comprises entre 0 et 24")
if hstart==hfin:
    print("Attention ! l’heure de fin est identique à l’heure de début.")
if hstart>hfin:
    print("Attention ! le début de la location est après la fin ...")
heures1euros =0
heures2euros=0
for h in range (hstart, hfin):
    if 7<=h and h<17:
        heures2euros+=1
    else:
        heures1euros+=1
print("Vous avez loué votre vélo pendant:")
print(f"{heures1euros} au tarif horaire de 1.0 euro(s)")
print(f"{heures2euros} au tarif horaire de 2.0 euro(s)")
total=heures1euros*1+heures2euros*2
print(f"Le montant total à payer est de {total} euro(s).")
