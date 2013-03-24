import automaton

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
    etatInitial = []
    
    etatInitial += aut.get_initial_states()
    
    #Et on l'ajoute au graph
    if len(etatInitial) > 1:
        resultat.add_initial_state(tuple(etatInitial))
    else:
        resultat.add_initial_state(etatInitial[-1])
    
    #Et à la pile, car il faut traiter les transitions
    pile += [etatInitial]
    
    print(etatInitial)
    print(pile)

    #Tant que la pile a un état à traiter
    for etatCourant in pile:
        for letter in alphabet:
            delta = []
            delta += aut.delta(letter,etatCourant)
            print("Etat de la pile: ")
            print(delta)
            print("-----------------")
            nouvelEtat = (tuple(delta))
            if delta != etatCourant:
                resultat.add_state(nouvelEtat)
                resultat.add_transition((etatCourant[-1],letter,nouvelEtat))
            else:
                print("Etat courant:")
                print(etatCourant)
                resultat.add_transition((etatCourant[-1],letter,etatCourant[-1]))
    
    
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
    
    resultat.display()
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
    automate2.display()

if __name__ == '__main__':
    main()
