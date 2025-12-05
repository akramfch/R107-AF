import sys
import os

def aide():
    """Affiche un message d'aide sur l'utilisation du script."""
    nom_script = sys.argv[0]
    print(f"Utilisation : python {nom_script} <dossier>")
    print("  <dossier> : chemin du dossier dont vous voulez afficher le contenu")

def affiche(dossier):
    """Affiche le contenu du dossier passé en argument."""
    print(f"Contenu du dossier : {dossier}")
    try:
        # os.listdir(dossier) renvoie la liste des fichiers/dossiers à l'intérieur
        for elt in os.listdir(dossier):
            print(elt)
    except PermissionError:
        print("Permission refusée pour lire ce dossier.")

if __name__ == "__main__":
    # Vérifier qu'un argument a été donné
    if len(sys.argv) != 2:
        print("Erreur : nombre d'arguments invalide.")
        aide()
        sys.exit(1)

    dossier = sys.argv[1]

    # Vérifier que l'argument est un dossier qui existe
    if not os.path.exists(dossier):
        print(f"Erreur : le dossier '{dossier}' n'existe pas.")
        aide()
        sys.exit(1)

    if not os.path.isdir(dossier):
        print(f"Erreur : '{dossier}' n'est pas un dossier.")
        aide()
        sys.exit(1)

    # Si tout est ok, on affiche le contenu
    affiche(dossier)
