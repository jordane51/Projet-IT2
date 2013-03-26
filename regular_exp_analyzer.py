def regex_analyzer(string):
    if '+' in string:
        plus_index = string.index('+')
        chaine_gauche = string[:plus_index]
        chaine_droite = string[plus_index + 1:]

        #print("chaine_gauche")
        #print(chaine_gauche)
        #print("chaine_droite")
        #print(chaine_droite)
        #print("--------------")
        if chaine_droite == '':
            print("ERREUR, + mal placé")

        if len(chaine_gauche) >= 2:
            print("OH EA")
            if '(' not in chaine_gauche:
                return ['+', regex_analyzer(chaine_gauche), regex_analyzer(chaine_droite)]
            elif '(' in chaine_gauche:
                index_parg = string.index('(')
                index_pard = string.index(')')
                chaine_entre_par = string[index_parg + 1:index_pard]
                print("chaine entre par")
                print(chaine_entre_par)

                if index_pard + 1 > len(string) or string[index_pard + 1] != '*':
                    print("ERREUR, * absent après parenthèse")

                # Cas où il n'y a rien après l'étoile
                if index_pard + 2 >= len(string):
                    return ['*', regex_analyzer(chaine_entre_par)]
                else:
                    # Si à la suite de l'étoile il y a un '+' alors :
                    if string[index_pard + 2] == '+':
                        return ['+', ['*', regex_analyzer(chaine_entre_par)], regex_analyzer(string[index_pard + 3:])]
                    # Cas où c'est forcément une lettre ou une parenthèse
                    # ouvrante
                    # elif string[index_pard + 2] == '(':
                    else:
                        return ['.', ['*', regex_analyzer(chaine_entre_par)], regex_analyzer(string[index_pard + 2:])]

        return ['+', [chaine_gauche], regex_analyzer(chaine_droite)]

    # TODO: Manque les étoiles sans parentheses...
    #if '*' in string:
    #    # Récupère l'indice du premier '*' dans la chaine string
    #    if len(string) > 2:
    #        etoile_index = string.index('*')
    #        chaine_gauche = string[:etoile_index - 1]
    #        chaine_droite = string[etoile_index:]

    #        list_regex_gauche = regex_analyzer(chaine_gauche)
    #        list_regex_droite = regex_analyzer(chaine_droite)

    #        if list_regex_gauche:
    #            if list_regex_droite:
    #                return [list_regex_gauche, ['*', string[etoile_index - 1]], list_regex_droite]
    #            return [list_regex_gauche, ['*', [string[etoile_index - 1]]]]
    #        return ['*', [string[etoile_index - 1]]]

    #    return ['*', [string[0]]]

    # Cas où il n'y a plus de '+' ou de ')(' à gerer.
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
        # Cas où il n'y a qu'un seul caractere dans la chaine.
        list_res += [string]

    return list_res


def main():
    string = "a*b"
    list_res = regex_analyzer(string)
    print(list_res)

if __name__ == '__main__':
    main()
