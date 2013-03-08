import automaton


def intersection(aut1, aut2):
    """Returns the intersection of aut1 and aut2"""
    # déjà determinisés ou à déterminiser.

    finals_res = set()
    initials_res = set()
    states_res = set()
    alphabet_res = set()
    transitions_res = set()

    etats_aut1 = aut1.get_states()
    etats_aut2 = aut2.get_states()

    #etats_aut1_finals = aut1.get_final_states()
    #etats_aut2_finals = aut2.get_final_states()

    #etats_aut1_initials = aut1.get_initials_states()
    #etats_aut2_initials = aut2.get_initials_states()

    # Récupère l'intersection des deux alphabets

    alphabet_aut1 = aut1.get_alphabet()
    alphabet_aut2 = aut2.get_alphabet()

    if len(alphabet_aut1) < len(alphabet_aut2):
        alphabet_min = alphabet_aut1
        alphabet_max = alphabet_aut2
    else:
        alphabet_min = alphabet_aut2
        alphabet_max = alphabet_aut1

    for letter in alphabet_min:
        if letter in alphabet_max:
            alphabet_res.add(letter)

    # Parcours les etats, (1,1) (1,2) (1,3)
    for etat_aut1 in etats_aut1:
        for etat_aut2 in etats_aut2:
            for letter in alphabet_res:
                access_aut1 = aut1.delta(etat_aut1, letter)
                access_aut2 = aut2.delta(etat_aut2, letter)

                # Récupere les états ayant des mêmes transitions vers un état.
                if access_aut1 != set() and access_aut2 != set():
                    new_etat_gauche = (etat_aut1, etat_aut2)
                    new_etat_droite = (access_aut1[0], access_aut2[0])
                    states_res.add(new_etat_gauche)
                    states_res.add(new_etat_droite)

                    transitions_res.add((new_etat_gauche, letter, new_etat_droite))

    # revoir pour les epsilons transitions.
    return automaton.automaton(alphabet_res, aut1.get_epsilons(), states_res,
                               initials_res, finals_res, transitions_res)


def main():
    aut1 = automaton.automaton(
        epsilons=[],
        states=[0, 1], initials=[0], finals=[1],
        transitions=[(0, 'a', 1), (1, 'b', 0)])

    #aut1.display()

    aut2 = automaton.automaton(
        epsilons=[],
        states=[0, 1], initials=[0], finals=[1],
        transitions=[(0, 'a', 1), (1, 'b', 0)])

    #aut2.display()

    toto = intersection(aut1, aut2)

    toto.display()

if __name__ == '__main__':
    main()
