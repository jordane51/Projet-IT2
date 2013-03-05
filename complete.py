import automaton


def complete(aut):
    """Return the Automate completed"""
    trash_is_here = False
    aut_bis = aut.clone()

    alphabet = aut_bis.get_alphabet()
    states = aut_bis.get_states()

    for state in states:
        for letter in alphabet:
            transition_tmp = aut_bis.delta(letter, [state])
            if transition_tmp == set():
                if not trash_is_here:
                    aut_bis.add_state("Trash")
                    trash_is_here = True
                aut_bis.add_transition((state, letter, "Trash"))
            if trash_is_here:
                aut_bis.add_transition(("Trash", letter, "Trash"))

    return aut_bis


def main():
    aut1 = automaton.automaton(
        epsilons=[],
        states=[0, 1], initials=[0], finals=[1],
        transitions=[(0, 'a', 1), (1, 'b', 0)])

    toto = complete(aut1)

    toto.display()

if __name__ == '__main__':
    main()
