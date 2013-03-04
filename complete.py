import automaton

def complete(aut):
    """Return the Automate completed"""

    aut_bis = aut.clone()

    alphabet = aut_bis.get_alphabet()
    epsilons = aut_bis.get_epsilons()
    states = aut_bis.get_states()
    initials = aut_bis.get_initial_states()
    finals = aut_bis.get_final_states()
    transitions = aut_bis.get_transitions()

    for state in states:
        is_completed = 0
        all_transition =



    return aut_bis


def main():
    pass

if __name__ == '__main__':
    main()
