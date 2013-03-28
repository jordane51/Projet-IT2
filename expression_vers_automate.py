import automaton
from regular_exp_analyzer import regex_analyzer

def exprToAutRec(E, aut, cpt):
    courant = E[0]
    print(courant)
    if courant == '*':
        aut = exprToAutRec(E[1],aut,cpt = cpt+1)
        tmp = automaton.automaton()
        tmp.add_initial_state("INIT")
        tmp.add_state("INTER1")
        tmp.add_final_state("FIN")
        tmp.add_state("INTER2")
        tmp.add_transition(("INIT",'e',"INTER1"))
        for initial in aut.get_initial_states():
            tmp.add_transition(("INTER1",'e',initial))
        for transition in aut.get_transitions():
            tmp.add_transition(transition)
        for final in aut.get_final_states():
            tmp.add_transition((final,'e',"INTER2"))
        tmp.add_transition(("INTER2",'e',"FIN"))
        tmp.add_transition(("INIT",'e',"FIN"))
        tmp.add_transition(("INTER2",'e',"INTER1"))
        tmp.display(wait=False)
    elif courant == '.':
        aut = exprToAutRec(E[1],aut,cpt = cpt+1)
        tmp = automaton.automaton()
        tmp.add_initial_state("INIT")
        tmp.add_final_state("FIN")
        initial = None
        final = None
        for init in aut.get_initial_states():
            initial = init
        aut = exprToAutRec(E[1],aut,cpt = cpt+1)
        for transition in aut.get_transitions():
            tmp.add_transition(transition)
        for fin in aut.get_final_states():
            final = fin
        tmp.add_transition((final,'e',"FIN"))
    elif courant == '+':
        aut = exprToAutRec(E[1],aut,cpt = cpt+1)
        tmp = automaton.automaton()
        tmp.add_initial_state("INIT")
        tmp.add_final_state("FIN")
        for initial in aut.get_initial_states():
            tmp.add_transition(("INIT",'e',initial))
        for final in aut.get_final_states():
            tmp.add_transition((final,'e',"FINN"))
        for transition in aut.get_transitions():
            tmp.add_transition(transition)
    else:
        aut = exprToAutRec(E[1],aut,cpt = cpt+1)

    return aut
    """
def exprToAutRec(E, aut, cpt):
    # cas d'arret: liste vide
    if len(E) > 1:
        for caractereCourant in E:
            #print("Itération: "+str(cpt));
            #print(list(caractereCourant))
            if caractereCourant == '*':
                print("*")
                # on commence par récuperer les finaux et initiaux
                finaux = aut.get_final_states()
                E.pop(0)
                print(E)
                initiaux = exprToAutRec(E, aut, cpt = cpt+1).get_initial_states()
                for initial in initiaux:
                    print("initial")
                cpt = cpt + 1
                ri = cpt+1
                rf = cpt+2
                aut.add_initial_state(ri)
                aut.add_final_state(rf)
            elif caractereCourant == '.':
                print(".")
            elif caractereCourant == '+':
                print("+")
            elif len(caractereCourant) == 1:
                print("D:"+str(caractereCourant[-1]))
                cpt = cpt+1
                ri = str(cpt+1)+str(caractereCourant[-1])
                rf = str(cpt+2)+str(caractereCourant[-1])
                aut.add_initial_state(ri)
                aut.add_final_state(rf)
                aut.add_transition((ri,'a',rf))
                exprToAutRec(caractereCourant, aut, cpt = cpt+1)
    
            
    #print("Après récursion")
    return aut
    """
    """
    sousAutomate = automaton.automaton()
    if len(E) > 1:
        sousAutomateDroite = exprToAutRec(E[1],cpt)
        for element in E[0]:
            #element = E[0]
            current = list(E)
            print("Element courant")
            print(element)
            if element == '*':
                print("* FTW")
                
            elif element == '.':
                print(". FTW")
        
            elif element == '+':
                print("+ FTW")

            else:
                print("I'm in the else")
                sousAutomate.add_initial_state(cpt)
                cpt = cpt+1
                sousAutomate.add_final_state(cpt)
                sousAutomate.add_transition((cpt-1,element[0],cpt))

    return sousAutomate
    """

def expression_vers_automate(E):
    # Bon, c'est parti !
    # Fonction récursive, on prend le premier élément, et on le traite puis on appele la fonction avec le reste de la liste. Mucho large complexidad
    #automate = automaton.automaton()
    #exprToAutRec(E)
    automate = automaton.automaton(initials=[1],finals=[2],transitions=[(1,'a',2)])
    return exprToAutRec(E,automate,0)

def main():
    # ( a+b*a )*
    #test1 = ['*', ['+', [['a'], ['.', ['*', ['b']], ['a']]]]]
    expression_vers_automate(regex_analyzer("(a+b+c)*")).display()
    print(regex_analyzer("(a+b+c)*"))

    # ( a+b+c )
    #test2 = ["+", ["+",["a", "b"]], ["c"]

if __name__ == '__main__':
    main()
