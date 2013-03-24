import automaton


def determiniser(aut):
    """Retourne un automate déterminisé de l'automate passé en paramètre"""

    #

    #etats = aut.get_states()
    alphabet = aut.get_alphabet()

    #contient les états à traiter
    tableau = []
    #contient les états déjà traités
    traites = []

    #on récupère les états initiaux
    tableau = list(aut.get_initial_states())

    #DEBUG
    print(tableau)

    for current in tableau:
        for letter in alphabet:
            if current not in traites:
                traites += [current]
                toto = aut.delta(letter, [current])
                if toto != set():
                    for elem in toto:
                        tableau += [elem]
        print(aut.delta(current))
    print(traites)
    return aut


def main():
    automate = automaton.automaton(
        epsilons=[],
        states=[0,1],initials=[0],finals=[1],
        transitions=[(0,'a',1),(1,'b',0)])
    #automate.display()
    automate2 = automaton.automaton(
        epsilons = [],
        states=[1,2],initials=[1],finals=[2],
        transitions=[(1,'a',1),(1,'b',1),(1,'a',2)])
    determiniser(automate2)

if __name__ == '__main__':
    main()
