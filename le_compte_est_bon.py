#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

"""
Le compte est bon
Séverine Hori Maitrehut

"""
CONST_ADDITION = 1
CONST_SUBSTRACTION = 2
CONST_MULTIPLICATION = 3
CONST_DIVISION = 4

def print_plaques(choice):
    """Fonction qui affiche les plaques à disposition du joueur"""
    print("Plaques disponibles :")
    print("+------+------+------+------+------+------+")
    print("|", end="")
    for nb in choice:
        print(f" {nb:^4} |", end="")
    print()
    print("+------+------+------+------+------+------+")


def is_entry_int_ok(user_input, min_int, max_int):
    """ Fonction qui vérifie la saisie d'un numérique, entre min_int et max_int    """
    cleaned_user_input = user_input.strip()
    if not cleaned_user_input.isdigit():
        return False
    if int(cleaned_user_input) < min_int or int(cleaned_user_input) > max_int:
        return False
    return True


def get_int_input(prompt, min_int, max_int):
    """Fonction qui demande au joueur de saisir un int"""
    input_int = input(prompt)
    while not is_entry_int_ok(input_int, min_int, max_int):
        input_int = input("Saisie incorrecte. Merci de recommencer : ")
    return input_int


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

    # TODO Tant que conditions de fin de sortie non atteintes: Faire
    end_of_game = False
    #while not end_of_game:
    print(f" Le nombre à obtenir est : {nb_to_get}")

    # Appel de la fonction affichage des plaques
    print_plaques(choice)

    # Saisie de l'utilisateur choix d'une opération
    operator_choice = get_int_input("Choix d'une opération (1 +, 2 -, 3 * et 4 /) : ", 1, 4)

    # TODO Saisie de l'utilisateur choix des nombres parmi les plaques (fonctions à écrire)

    # TODO Calcul demandé par l'utilisateur


    # TODO Si sortie de boucle, afficher le dernier nombre atteint



if __name__ == '__main__':
    main_jeu()
