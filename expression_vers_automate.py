#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import automaton
from regular_exp_analyzer import regex_analyzer


def exprToAutRec(E, aut, cpt):
    caractereCourant = E[0]
    if caractereCourant == '+':
        ri1 = cpt
        rf1 = exprToAutRec(E[1], aut, ri1)
        ri2 = rf1 + 1
        rf2 = exprToAutRec(E[2], aut, ri2)
        aut.add_transition(('Init', 'eps', ri1))
        aut.add_transition(('Init', 'eps', ri2))
        aut.add_transition((rf1, 'eps', 'Fin'))
        aut.add_transition((rf2, 'eps', 'Fin'))
        return rf2
    elif caractereCourant == '*':
        """
        ri1 = cpt
        rf1 = exprToAutRec(E[1],aut,ri1)
        aut.add_state(ri1)
        aut.add_transition(('Init','esp',ri1))
        aut.add_transition((rf1,'est','Fin'))
        aut.add_transition(('Init','esp','Fin'))
        aut.add_transition((rf1,'esp',ri1))
        """
        tmp1 = cpt
        ri1 = cpt + 1
        rf1 = exprToAutRec(E[1], aut, ri1)
        tmp2 = rf1 + 1
        aut.add_transition(('Init', 'eps', tmp1))
        aut.add_transition((tmp1, 'eps', ri1))
        aut.add_transition((rf1, 'eps', tmp2))
        aut.add_transition((tmp2, 'eps', 'Fin'))
        aut.add_transition((tmp2, 'eps', tmp1))
        aut.add_transition(('Init', 'eps', 'Fin'))
        return tmp2
    elif caractereCourant == '.':
        ri1 = cpt
        rf1 = exprToAutRec(E[1], aut, ri1)
        ri2 = rf1 + 1
        rf2 = exprToAutRec(E[2], aut, ri2)
        aut.add_transition(('Init', 'eps', ri1))
        aut.add_transition((ri1, 'eps', ri2))
        aut.add_transition((rf2, 'eps', 'Fin'))
    else:
        ri = cpt
        rf = cpt + 1
        aut.add_state(ri)
        aut.add_state(rf)
        aut.add_transition((ri, E[0], rf))
        aut.add_character(caractereCourant)
        return rf


def expression_vers_automate(E):
    # Bon, c'est parti !
    # Fonction récursive, on prend le premier élément, et on le traite puis on appele la fonction avec le reste de la liste. Mucho large complexidad
    #automate = automaton.automaton()
    #exprToAutRec(E)
    automate = automaton.automaton(initials=['Init'], finals=['Fin'])
    exprToAutRec(E, automate, 0)
    return automate


def main():
    # ( a+b*a )*
    #test1 = ['*', ['+', [['a'], ['.', ['*', ['b']], ['a']]]]]
    E = regex_analyzer("(a+b+c)*")
    print(E)
    expression_vers_automate(E).display(title="Automate", wait=False)
    #print(regex_analyzer("(a+b+c)*"))

    # ( a+b+c )
    #test2 = ["+", ["+",["a", "b"]], ["c"]

if __name__ == '__main__':
    main()
