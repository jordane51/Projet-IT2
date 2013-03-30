#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import automaton


def complement(aut):
    """ Returns the complement of an automate """
    states = aut.get_states()
    finals = set()

    for state in states:
        if not aut.state_is_final(state):
            finals.add(state)

    return automaton.automaton(aut.get_alphabet(), aut.get_epsilons(), states,
                               aut.get_initial_states(), finals, aut.get_transitions())


def main():
    aut = automaton.automaton(
        epsilons=[],
        states=[0, 1, 2, 3], initials=[0], finals=[1, 2],
        transitions=[(0, 'a', 1), (1, 'b', 0), (0, 'b', 2), (1, 'a', 2), (3, 'a', 2)])

    aut.display()

    aut.display(title="Automate origin", wait=False)
    toto = complement(aut)
    toto.display(title="Automate origin's complement", wait=False)

if __name__ == '__main__':
    main()
