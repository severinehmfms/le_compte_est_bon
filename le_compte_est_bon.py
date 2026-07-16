#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import operator


"""
Le compte est bon
Séverine Hori Maitrehut

"""
CONST_ADDITION = 1
CONST_SUBSTRACTION = 2
CONST_MULTIPLICATION = 3
CONST_DIVISION = 4

CONSTS_OPERATORS = {
    CONST_ADDITION: operator.add,
    CONST_SUBSTRACTION: operator.sub,
    CONST_MULTIPLICATION: operator.mul,
    CONST_DIVISION: operator.truediv
}

CONST_SYMBOLS = {
        CONST_ADDITION: "+",
        CONST_SUBSTRACTION: "-",
        CONST_MULTIPLICATION: "*",
        CONST_DIVISION: "/"
    }

def print_plaques(choice):
    """Fonction qui affiche les plaques à disposition du joueur"""
    print("Plaques disponibles :")
    bordure = "+" + "------+" * len(choice)
    print(bordure)
    print("|", end="")
    for nb in choice:
        print(f" {nb:^4} |", end="")
    print()
    print(bordure)


def remove_plaque(choice, nb_plaque_to_remove):
    """ Fonction qui supprime la plaque dont le nombre est : nb_plaque_to_remove"""
    nb_plaque_to_remove = int(nb_plaque_to_remove)
    choice.remove(nb_plaque_to_remove)


def add_plaque(choice, nb_plaque_to_add):
    """ Fonction qui supprime la plaque dont le nombre est : nb_plaque_to_remove"""
    nb_plaque_to_add = int(nb_plaque_to_add)
    choice.append(nb_plaque_to_add)


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
    return int(input_int)


def is_card_choice_entry_ok(card_choice_input, min_int, max_int, choice):
    """ Fonction qui vérifie la saisie d'un numérique, entre min_int et max_int    """
    cleaned_card_choice_input = card_choice_input.strip()
    if not cleaned_card_choice_input.isdigit():
        return False
    if int(cleaned_card_choice_input) < min_int or int(cleaned_card_choice_input) > max_int:
        return False
    if (int(cleaned_card_choice_input) not in choice):
        return False
    return True


def get_card_choice_input(prompt, min_int, max_int, choice):
    """Fonction qui demande au joueur de saisir le nombre correspondant à la plaque choisie"""
    card_choice_input = input(prompt)
    while not is_card_choice_entry_ok(card_choice_input, min_int, max_int, choice):
        card_choice_input = input("Saisie incorrecte. Merci de recommencer : ")
    return int(card_choice_input)


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

    # Tirage au sort des 6 plaques différentes (d'ou random.sample) parmi les 24
    choice = random.sample(nb_to_choice, 6)

    # TODO Tant que conditions de fin de sortie non atteintes: Faire
    end_of_game = False

    while not end_of_game:
        print(f" Le nombre à obtenir est : {nb_to_get}")
        # Affichage des plaques
        print_plaques(choice)

        # Saisie de l'utilisateur choix d'une opération
        operator_choice = get_int_input("Choix d'une opération (1 +, 2 -, 3 * et 4 /) : ", 1, 4)
        #Saisie de l'utilisateur pour le choix d'un nombres parmi les plaques
        card_choice_1 = get_card_choice_input("Choix d'un chiffre d'une des plaques : ", 1, 100, choice)
        remove_plaque(choice, card_choice_1)
        #print_plaques(choice)
        card_choice_2 = get_card_choice_input("Choix d'un chiffre d'une des plaques : ", 1, 100, choice)
        remove_plaque(choice, card_choice_2)
        #print_plaques(choice)

        #Calcul demandé par l'utilisateur
        result = CONSTS_OPERATORS[int(operator_choice)](card_choice_1, card_choice_2)
        add_plaque(choice, result)
        print(f" Le résultat pour le calcul : {card_choice_1} {CONST_SYMBOLS[int(operator_choice)]} {card_choice_2} est : {result}")

        if (len(choice) == 0):
            end_of_game = True

    # TODO Si sortie de boucle, afficher le dernier nombre atteint



if __name__ == '__main__':
    main_jeu()
