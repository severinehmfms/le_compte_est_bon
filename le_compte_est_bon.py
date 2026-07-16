#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

"""
Le compte est bon
Séverine Hori Maitrehut

"""

def main_jeu():
    """Fonction principale du jeu le compte est bon"""

    # Tirage au sort du nombre à obtenir
    nb_to_get = random.randint(101, 999)

    # On prépare les 24 plaques portant un nombre
    nb_to_choice = []
    for i in range(1, 10):
        nb_to_choice.append(i)
        nb_to_choice.append(i)
    nb_to_choice.append(25)
    nb_to_choice.append(50)
    nb_to_choice.append(75)
    nb_to_choice.append(100)
    #for indice, valeur in enumerate(nb_to_choice):
    #    print(f"[{indice}] = {valeur}")

    # Tirage au sort des 6 plaques différentes (d'ou random.sample) parmi les 24
    choice = random.sample(nb_to_choice, 6)
    #Si on veut un random parmi les indices
    # indices = random.sample(range(len(nb_to_choice)), 6)
    print("Choix")
    for indice, valeur in enumerate(choice):
        print(f"[{indice}] = {valeur}")

    # TODO Tant que conditions de fin de sortie non atteintes: Faire
    print(f" Le nombre à obtenir est : {nb_to_get}")
    # TODO Appel de la fonction affichage des plaques (fonction à écrire)

    # TODO Saisie de l'utilisateur choix d'une opération (fonctions à écrire)

    # TODO Saisie de l'utilisateur choix des nombres parmi les plaques (fonctions à écrire)

    # TODO Calcul demandé par l'utilisateur


    # TODO Si sortie de boucle, afficher le dernier nombre atteint



if __name__ == '__main__':
    main_jeu()
