#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import automaton
import complete


def new_finals_states(aut1, aut2, aut_res, inter):
    """ Determine the new finals states for intersection or union operation between two automates """
    for state in aut_res.get_states():
        if state not in aut_res.get_final_states():
            if inter:
                if aut1.state_is_final(state[0]) and aut2.state_is_final(state[1]):
                    aut_res.add_final_state((state[0], state[1]))
            else:
                if aut1.state_is_final(state[0]) or aut2.state_is_final(state[1]):
                    aut_res.add_final_state((state[0], state[1]))


def intersection_union(aut1, aut2, inter):
    """ Returns the intersection or the union of aut1 and aut2
    if inter == True, intersection function is done,
    else, union function is done..
    Expect that the automates are already complete (AND? deterministic)
    Their alphabet must be equals else it return None.
    """
    aut_res = automaton.automaton()

    if aut1.get_alphabet() != aut2.get_alphabet():
        return None

    alphabet_res = aut1.get_alphabet()
    stack = []

    print("initialisation à partir des états initiaux")
    for init_aut1 in aut1.get_initial_states():
        for init_aut2 in aut2.get_initial_states():
            init_state_res = (init_aut1, init_aut2)

            aut_res.add_initial_state(init_state_res)
            aut_res.add_state(init_state_res)

            stack += [init_state_res]

    while len(stack) > 0:
        print(stack)
        #current state
        state = stack.pop()

        for letter in alphabet_res:
            # Evite les liaisons inutiles sur un etat sur lui même.
            if not letter in aut1.get_epsilons():
                access_aut1 = list(aut1.delta(letter, [state[0]]))
                access_aut2 = list(aut2.delta(letter, [state[1]]))

                for al in access_aut1:
                    for ar in access_aut2:
                        new_state = (al, ar)

                        # Nouvel etat à gerer (et toutes les transitions ...)
                        if not aut_res.has_state(new_state):
                            stack += [new_state]
                            aut_res.add_state(new_state)

                        aut_res.add_transition(((state[0], state[1]), letter, new_state))

    new_finals_states(aut1, aut2, aut_res, inter)
    # Si 'pour l'intersection' il n'y a pas d'états finaux, alors l'automate est vide.
    if aut_res.get_final_states() != set():
        return aut_res
    else:
        return "Automate VIDE, (intersection)"


def intersection(aut1, aut2):
    """ Returns the intersection of aut1 inter aut2 """
    return intersection_union(aut1, aut2, True)


def union(aut1, aut2):
    """ Returns the union of aut1 union aut2 """
    return intersection_union(aut1, aut2, False)


def A():
    return automaton.automaton(['a', 'b'], '0', [1, 2], [1], [2], [(1, 'a', 2)])


def B():
    return automaton.automaton(['a', 'b'], '0', [1, 2], [1], [2], [(1, 'b', 2)])


def main():
    A().display(title="Automate A", wait=False)
    B().display(title="Automate B", wait=False)
    comp_aut1 = complete.complete(A())
    comp_aut2 = complete.complete(B())

    comp_aut1.display(title="Automate A complete", wait=False)
    comp_aut2.display(title="Automate B complete", wait=False)

    # Test pour intersection.
    toto = intersection(comp_aut1, comp_aut2)
    #   Test si l'automate retourné est bien l'intersection de A() par B()
    if type(toto) == str:
        print("AUTOMATE VIDE !")
    else:
        toto.display(title="A inter B", wait=False)

    # Test pour union.
    titi = union(comp_aut1, comp_aut2)
    titi.display(title="A union B", wait=False)

if __name__ == '__main__':
    main()
