import automaton

def exprToAutRec(E, aut, cpt):
    # cas d'arret: liste vide
    if len(E) > 0:
        for caractereCourant in E[0]:
            print(caractereCourant)
            print(E[1])
    exprToAutRec(E[1], aut, cpt = cpt+1)
    
    
    
    return aut
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
    return exprToAutRec(E,automaton.automaton(),0)

def main():
    # ( a+b*a )*
    test1 = ['*', ['+', [['a'], ['.', ['*', ['b']], ['a']]]]]
    expression_vers_automate(test1).display()


    # ( a+b+c )
    #test2 = ["+", ["+",["a", "b"]], ["c"]

if __name__ == '__main__':
    main()
