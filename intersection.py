# -*- coding: UTF-8 -*-

import automaton


def intersection(aut1, aut2):
    """Returns the intersection of aut1 and aut2"""
    # tests si à determiniser/completer
    # voir si il faut utiliser pretty_set comme dit dans la lib.
    finals_res = set()
    initials_res = set()
    states_res = set()
    alphabet_res = set()
    transitions_res = set()

    # Récupère l'intersection des deux alphabets
    # Méthode frozenset.intersection(frozenset) existe. cf help(frozenset)
    alphabet_res = aut1.get_alphabet().intersection(aut2.get_alphabet())
    #print(alphabet_res)

    # Récupère l'automate ayant le moins d'états.
    aut1_state = aut1.get_states()
    aut2_state = aut2.get_states()

    # Test possible avec l'implémentation même des set / frozenset.
    # cf help(frozenset)
    if aut1_state < aut2_state:
        states_min = aut1_state
        states_max = aut2_state
        aut_min = aut1
        aut_max = aut2
    else:
        states_min = aut2_state
        states_max = aut1_state
        aut_min = aut2
        aut_max = aut1

    # Parcours les etats, (0,0) (0,1) ... (1,1) (1,2) (1,3)...
    for state_min in states_min:
        for state_max in states_max:
            for letter in alphabet_res:
                print("-------------")
                print("state")
                print((state_min, state_max))
                print("letter")
                print(letter)

                # TODO: /!\ Problème de typage : type(access_min) == frozenset
                # retourne : ({1},{1}) pour un état voulu : (1,1)
                # A chercher : moyen de 'gruger' ou de bien faire l'ajout de
                # ces états à states_res

                # Récupère les états ayant des mêmes transitions vers un état.
                access_min = aut1.delta(letter, [state_min])
                access_max = aut2.delta(letter, [state_max])
                #print(access_min, access_max)

                # Si test est vrai, alors il existe pour les deux automates une
                # liaison des états : "state_min" et "state_max" vers
                # "access_min" et acess_max" respectivement en la lettre "letter"
                if access_min != set() and access_max != set():
                    # Nouveaux états et transitions définis :
                    # (new_etat_left , letter, new_etat_right)
                    new_etat_left = (state_min, state_max)
                    # Fonctionne, basé sur un 'hack' en attendant mieux !
                    # TODO: Trouver un moyen de parcourir un frozenset/prettyset
                    for i in access_min:
                        toto = i
                        break

                    for i in access_max:
                        titi = i
                        break

                    new_etat_right = (toto, titi)
#                    new_etat_right = (access_min, access_max)

                    print(new_etat_left, new_etat_right)

                    # TODO: Tests si les états sont déjà finaux ou initiaux  (faire
                    # un automate au début qu'on remplira au fur et à mesure et
                    # utiliser les fonctions "is_final/is_initial"

                    # Gestion des états initiaux et finaux.
                    # Il faut que les deux états gérés soit à la fois initiaux
                    # pour les rajouter dans initial_res.access_max
                    # Raisonnement identique pour les états finaux.
                    if aut_min.state_is_final(state_min) and aut_max.state_is_final(state_max):
                        finals_res.add(new_etat_left)
                    elif aut_min.state_is_initial(state_min) and aut_max.state_is_initial(state_max):
                        initials_res.add(new_etat_left)

                    elif aut_min.state_is_final(access_min) and aut_max.state_is_final(access_max):
                        finals_res.add(new_etat_right)
                    elif aut_min.state_is_initial(access_min) and aut_max.state_is_initial(access_max):
                        initials_res.add(new_etat_right)

                    transitions_res.add((new_etat_left, letter, new_etat_right))
                    states_res.add(new_etat_left)
                    states_res.add(new_etat_right)

    # revoir pour les epsilons transitions.
    # nettoyer également (/!\ important /!\), tous les états inutiles "surplus"
    return automaton.automaton(alphabet_res, aut1.get_epsilons(), states_res,
                               initials_res, finals_res, transitions_res)


def main():
    aut1 = automaton.automaton(
        epsilons=[],
        states=[0, 1], initials=[0], finals=[1],
        transitions=[(0, 'a', 1), (1, 'b', 0)])

    aut1.display()

    aut2 = automaton.automaton(
        epsilons=[],
        alphabet=['a', 'b', 'c'],
        states=[0, 1], initials=[0], finals=[1],
        transitions=[(0, 'a', 1), (1, 'b', 0)])

    #aut2.display()

    toto = intersection(aut1, aut2)

    toto.display()

if __name__ == '__main__':
    main()
