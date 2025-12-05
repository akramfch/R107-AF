import sys
import os

def aide():
    nom_script = sys.argv[0]
    print("Utilisation :")
    print(f"  python {nom_script} -d <dossier> -f <nom_fichier>")
    print("Exemple :")
    print(f"  python {nom_script} -d C:\\temp -f toto.txt")

def recherche(dossier, fichier):
    """
    Recherche tous les fichiers nommés 'fichier' dans 'dossier' et ses sous-dossiers.
    Renvoie la liste de leurs chemins complets.
    """
    listeFichiers = []

    try:
        contenu = os.listdir(dossier)
    except PermissionError:
        print(f"Permission refusée pour : {dossier}")
        return listeFichiers

    for elt in contenu:
        chemin_complet = os.path.join(dossier, elt)

        if os.path.isfile(chemin_complet):
            # On compare seulement le nom du fichier (pas tout le chemin)
            if os.path.basename(chemin_complet) == fichier:
                listeFichiers.append(chemin_complet)

        elif os.path.isdir(chemin_complet):
            # on descend dans le sous-dossier
            sous_fichiers = recherche(chemin_complet, fichier)
            listeFichiers.extend(sous_fichiers)

    return listeFichiers

if __name__ == "__main__":
    # On attend exactement 5 arguments : script, -d, dossier, -f, fichier
    if len(sys.argv) != 5:
        print("Erreur : nombre d'arguments invalide.")
        aide()
        sys.exit(1)

    # Parsing simple : python find.py -d <dossier> -f <fichier>
    if sys.argv[1] != "-d" or sys.argv[3] != "-f":
        print("Erreur : syntaxe incorrecte.")
        aide()
        sys.exit(1)

    dossier = sys.argv[2]
    fichier = sys.argv[4]

    if not os.path.exists(dossier) or not os.path.isdir(dossier):
        print(f"Erreur : '{dossier}' n'est pas un dossier valide.")
        aide()
        sys.exit(1)

    resultats = recherche(dossier, fichier)

    if not resultats:
        print("Aucun fichier trouvé.")
    else:
        for chemin in resultats:
            print(chemin)
