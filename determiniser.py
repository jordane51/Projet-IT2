import automaton

def isDeterministe(aut):
    """Retourne True si l'automate est déterministe, False sinon"""
    for etatCourant in aut.get_states():
        for letter in aut.get_alphabet():
            if len(aut.delta(letter,[etatCourant])) > 1:
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

    #etatInitial +=

    #print("ETATT INITIAL:")
    #print(etatInitial)

    #Et on l'ajoute au graphe
    resultat.add_initial_state(tuple(etatInitial))

    #Et à la pile, car il faut traiter les transitions
    pile += [etatInitial]

    #print(etatInitial)
    #print(pile)

    #Tant que la pile a un état à traiter
    for etatCourant in pile:
        for letter in alphabet:
            hasFinalState = False
            delta = list(aut.delta(letter, etatCourant))
            #print("Etat de la pile: ")
            #print(pile)
            #print("-----------------")

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
                    #print("Etat courant:")
                    #print(etatCourant)
                    resultat.add_transition((tuple(etatCourant), letter, tuple(etatCourant)))
            traites += [etatCourant]

            #Si il y a un final, on passe l'etat en final
            if hasFinalState:
                resultat.add_final_state(nouvelEtat)
            if nouvelEtat not in traites:
                pile += [nouvelEtat]

    """
        Ok, je comprend décidemment rien au différents types de structures qu'on doit utiliser

    initialState = set()
    for initial in aut.get_initial_states():
        initialState.add(initial)
    resultat.add_initial_state(automaton.pretty_set(initialState))

    cpt = 0

    for current in tableau:
        cpt = cpt+1
        #for letter in alphabet:


        print(cpt)

    """
    """
    #on récupère les états initiaux
    tableau = [resultat.get_initial_states()]

    #DEBUG
    #print(tableau)

    for current in tableau:
        for letter in alphabet:
            #print(letter)
            print(aut.delta(letter,[current]))
            etatComposite = list()
            for letatTmp in current:
                etatComposite += aut.delta(letter,letatTmp)
            if etatComposite not in traites:
                isFinalComposite = False

                for stateTmp in etatComposite:
                    if aut.state_is_final(stateTmp):
                        isFinalComposite = True
                if isFinalComposite:
                    resultat.add_final_state(automaton.pretty_set(etatComposite))
                else:
                    resultat.add_state(automaton.pretty_set(etatComposite))
                if len(traites) > 0:
                    #print(list(traites[-1]))
                    #print(letter)
                    #print(list(etatComposite))
                    resultat.add_transition((traites[-1],letter,etatComposite))
                    traites += current
                    tableau += etatComposite
            print(etatComposite)
    #r

#l'ajouter au res
    #print(etatComposite)
#print(traites)"""

    #resultat.display(title="Determinisé", wait=False)
    return resultat


def main():
    automate = automaton.automaton(
        epsilons=[],
        states=[0, 1], initials=[0], finals=[1],
        transitions=[(0, 'a', 1), (1, 'b', 0)])
    #automate.display()
    #automate2 = automaton.automaton(
    #    epsilons = [],
    #    states=[1,2],initials=[1],finals=[2],
    #    transitions=[(1,'a',1),(1,'b',1),(1,'a',2)])
    automate3 = automaton.automaton(
    epsilons = [],
    states=['E','a1','a2','a3','a4','a5','b1','b2','b3','b4','b5'],initials=['E'],finals=['a3','b2','b5','a5'],
    transitions=[('E','a','a1'),('a1','a','a1'),('a1','a','a2'),('a1','b','b1'),('b1','b','b1'),('a2','b','b2'),('b1','a','a1'),('b1','a','a2'),('a2','a','a3'),('E','b','b1'),('E','a','a2'),('E','b','b4'),('E','b','b3'),('E','a','a4'),('a4','a','a4'),('a4','b','b3'),('b3','b','b3'),('b3','a','a4'),('b3','b','b4'),('a4','b','b4'),('b4','b','b5'),('b4','a','a5')])

    #automate.display(title="Origine", wait=False)
    #determiniser(automate)
    #print(isDeterministe(automate))
    automate4 = determiniser(automate)
    #print(isDeterministe(automate4))
    automate4.display(title="2", wait=False)

if __name__ == '__main__':
        main()
