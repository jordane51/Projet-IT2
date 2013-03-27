#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import automaton


def mirror(aut):
    """ Returns the mirror of an automate """
    transitions = []
    transitions_aut = aut.get_transitions()

    for transition in transitions_aut:
        transitions += [(transition[2], transition[1], transition[0])]

    initial_states = aut.get_final_states()
    final_states = aut.get_initial_states()

    return automaton.automaton(aut.get_alphabet(), aut.get_epsilons(), aut.get_states(),
                               initial_states, final_states, transitions)


def main():
    aut1 = automaton.automaton(
        epsilons=[],
        states=[0, 1], initials=[0], finals=[1],
        transitions=[(0, 'a', 1), (1, 'b', 0)])

    aut1.display()
    toto = mirror(aut1)

    toto.display()

if __name__ == '__main__':
    main()
