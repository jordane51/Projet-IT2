import automaton


def complement(aut):
    """Returns the complement of an automate"""
    states = aut.get_states()
    finals = set()

    for state in states:
        if not aut.state_is_final(state):
            finals.add(state)

    return automaton.automaton(aut.get_alphabet(), aut.get_epsilons(), states,
                               aut.get_initial_states(), finals, aut.get_transitions())


def main():
    aut1 = automaton.automaton(
        epsilons=[],
        states=[0, 1], initials=[0], finals=[1],
        transitions=[(0, 'a', 1), (1, 'b', 0)])

    aut1.display()
    toto = complement(aut1)

    toto.display()

if __name__ == '__main__':
    main()
