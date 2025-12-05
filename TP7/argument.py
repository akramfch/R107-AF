import sys

if __name__ == "__main__":
    # nombre total d'arguments
    nb_args = len(sys.argv)

    # sys.argv[0] = nom du script
    nom_script = sys.argv[0]

    if nb_args == 1:
        print(f"Pas assez d'arguments pour le script '{nom_script}'")
    else:
        print(f"Nombre d'arguments : {nb_args}")
        print("Liste des arguments :")
        # on parcourt la liste des arguments
        for i in range(nb_args):
            print(f"argv[{i}] = {sys.argv[i]}")
