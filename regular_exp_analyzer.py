def regex_analyzer_bis(string):
    if '+' in string:
        # Récupère l'indice du premier '+' dans la chaine string.
        plus_index = string.index('+')
        chaine_gauche = string[:plus_index]
        chaine_droite = string[plus_index + 1:]
        return ['+', [regex_analyzer_bis(chaine_gauche)], [regex_analyzer_bis(chaine_droite)]]

    if '(' in string:
        # TODO enlever les indices des '(' et ')*'
        index_parg = string.index(')')
        index_pard = string.index(')')
        chaine_gauche = string[:index_parg]
        chaine_droite = string[index_pard:]

        #Trouver les indices exact de la chaine entre parentheses
        chaine_entre_par = string[:]

        list_regex_gauche = regex_analyzer_bis(chaine_gauche)
        list_regex_droite = regex_analyzer_bis(chaine_droite)

        if list_regex_gauche:
            if list_regex_droite:
                return [[list_regex_gauche], ['*', [regex_analyzer_bis(chaine_entre_par)]], [list_regex_droite]]
            return [[list_regex_gauche], ['*', [regex_analyzer_bis(chaine_entre_par)]]]
        return ['*', [regex_analyzer_bis(chaine_entre_par)]]

    if '*' in string:
        # Récupère l'indice du premier '*' dans la chaine string
        if len(string) > 2:
            etoile_index = string.index('*')
            chaine_gauche = string[:etoile_index - 1]
            chaine_droite = string[etoile_index:]
            list_regex_gauche = regex_analyzer_bis(chaine_gauche)
            list_regex_droite = regex_analyzer_bis(chaine_droite)

            if list_regex_gauche:
                if list_regex_droite:
                    return [list_regex_gauche, ['*', string[etoile_index - 1]], list_regex_droite]
                return[list_regex_gauche, ['*', string[etoile_index - 1]]]
            return [['*', string[etoile_index - 1]]]

        return [['*', string[0]]]

    list_res = []
    i = 0
    if len(string) >= 2:
        while(i < len(string) - 1):
            if (i + 1 < len(string)):
                list_res += [['.', [string[i]], [string[i + 1]]]]
                i += 1
            if i > len(string):
                break
    else:
        list_res += [string]

    if len(list_res) == 1:
        return list_res[0]
    return list_res


def main():
    string = "a+b"
    list_res = regex_analyzer_bis(string)
    print(list_res)

if __name__ == '__main__':
    main()
