import sys
import os

def aide():
    nom_script = sys.argv[0]
    print(f"Utilisation : python {nom_script} <dossier>")
    print("  <dossier> : chemin du dossier dans lequel faire la recherche")

def recherche(dossier):
    """
    Recherche tous les fichiers et dossiers dans 'dossier' et ses sous-dossiers.
    Renvoie (listeFichiers, listeDossiers).
    """
    listeFichiers = []
    listeDossiers = []

    try:
        contenu = os.listdir(dossier)
    except PermissionError:
        print(f"Permission refusée pour : {dossier}")
        return listeFichiers, listeDossiers

    for elt in contenu:
        chemin_complet = os.path.join(dossier, elt)

        if os.path.isfile(chemin_complet):
            # fichier standard
            listeFichiers.append(chemin_complet)

        elif os.path.isdir(chemin_complet):
            # dossier
            listeDossiers.append(chemin_complet)

            # on fait la recherche aussi dans ce sous-dossier (récursivité)
            sous_fichiers, sous_dossiers = recherche(chemin_complet)
            listeFichiers.extend(sous_fichiers)
            listeDossiers.extend(sous_dossiers)

    return listeFichiers, listeDossiers

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Erreur : nombre d'arguments invalide.")
        aide()
        sys.exit(1)

    dossier = sys.argv[1]

    if not os.path.exists(dossier) or not os.path.isdir(dossier):
        print(f"Erreur : '{dossier}' n'est pas un dossier valide.")
        aide()
        sys.exit(1)

    fichiers, dossiers = recherche(dossier)

    print("Liste des dossiers trouvés :")
    for d in dossiers:
        print(d)

    print("\nListe des fichiers trouvés :")
    for f in fichiers:
        print(f)
