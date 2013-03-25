#TODO Idée pour les parenthèses etoile. : Appel récursif quand on voit un motif : '(' ..... ')*'
# avec  list_res += ['*', appel_rec]


def regex_analyzer(string):
    liste_res = []

    if '+' in string:
        toto = string.split('+')

    if len(toto) > 1:
        liste_res = ['+']
        for x in toto:
            # N'a qu'un seul element (donc à mettre directement dans la liste
            # resultat
            if len(x) == 1:
                liste_res += [[x]]
            # A plus d'un élément, donc est un 'produit' de type
            # abc -> [., [a], [b], [c]]
            # et/ou bien à une étoile également à gerer..
            else:
                # Gestion des etoiles simple (sans parenthèses pour le moment)
                if '*' in x:
                    titi = ['.']

                    # Parcours des couples de caractères. a* teste si suivant
                    # de 'a' est une étoile, si oui l'ajoute avec le bon format
                    # et incrémente de 2 le curseur.
                    # Sinon rajoute normalement le caractère courant.
                    cpt = 0
                    while cpt < len(x):
                        if cpt + 1 < len(x) and x[cpt + 1] == '*':
                            titi += [['*', x[cpt]]]
                            cpt += 2
                            continue

                        titi += [[x[cpt]]]
                        cpt += 1

                    liste_res += [titi]
                else:
                    titi = ['.']
                    for y in x:
                        titi += [[y]]
                    liste_res += [titi]

        return liste_res
    else:
        return list(string)


def main():
    string = "a+cv*+b*f*"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)

if __name__ == '__main__':
    main()
