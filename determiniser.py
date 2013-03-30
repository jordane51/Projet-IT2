#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import automaton


def isDeterministe(aut):
    """Retourne True si l'automate est déterministe, False sinon"""
    for etatCourant in aut.get_states():
        for letter in aut.get_alphabet():
            if len(aut.delta(letter, [etatCourant])) > 1:
                #print("Supérieur pour" + letter + ":" + etatCourant)
                return False
    return True


def determiniser(aut):
    """Retourne un automate déterminisé de l'automate passé en paramètre"""
    #etats = aut.get_states()
    alphabet = aut.get_alphabet()
    #contient les états à traiter
    pile = []
    #contient les états déjà traités
    traites = []
    #contient le graph résultat que l'on construit au fur et à mesure
    resultat = automaton.automaton(alphabet=alphabet)

    #En premier, on crée l'état initial à partir de tous les états initiaux
    etatInitial = tuple(aut.get_initial_states())

    #Et on l'ajoute au graphe
    resultat.add_initial_state(tuple(etatInitial))

    #Et à la pile, car il faut traiter les transitions
    pile += [etatInitial]

    #Tant que la pile a un état à traiter
    for etatCourant in pile:
        for letter in alphabet:
            hasFinalState = False
            delta = list(aut.delta(letter, etatCourant))

            #On regarde s'il y a un état final dans le lot
            for etatTmp in delta:
                if aut.state_is_final(etatTmp):
                    hasFinalState = True
            nouvelEtat = tuple(delta)

            if len(delta) > 0:
                if delta != etatCourant:
                    resultat.add_state(nouvelEtat)
                    resultat.add_transition((tuple(etatCourant), letter, nouvelEtat))
                else:
                    resultat.add_transition((tuple(etatCourant), letter, tuple(etatCourant)))
            traites += [etatCourant]

            #Si il y a un final, on passe l'etat en final
            if hasFinalState:
                resultat.add_final_state(nouvelEtat)
            if nouvelEtat not in traites:
                pile += [nouvelEtat]
    return resultat


def main():
    #automate = automaton.automaton(
    #    epsilons=[],
    #    states=[0, 1], initials=[0], finals=[1],
    #    transitions=[(0, 'a', 1), (1, 'b', 0)])
    automate3 = automaton.automaton(
        epsilons = [],
        states=['E','a1','a2','a3','a4','a5','b1','b2','b3','b4','b5'],initials=['E'],finals=['a3','b2','b5','a5'],
        transitions=[('E','a','a1'),('a1','a','a1'),('a1','a','a2'),('a1','b','b1'),('b1','b','b1'),('a2','b','b2'),('b1','a','a1'),('b1','a','a2'),('a2','a','a3'),('E','b','b1'),('E','a','a2'),('E','b','b4'),('E','b','b3'),('E','a','a4'),('a4','a','a4'),('a4','b','b3'),('b3','b','b3'),('b3','a','a4'),('b3','b','b4'),('a4','b','b4'),('b4','b','b5'),('b4','a','a5')])

    automate3.display(title="Automate", wait=False)
    automate4 = determiniser(automate3)
    automate4.display(title="Determinise", wait=False)

if __name__ == '__main__':
    main()
