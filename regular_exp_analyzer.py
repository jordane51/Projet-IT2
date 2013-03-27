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
            if '(' not in chaine_gauche:
                return ['+', regex_analyzer(chaine_gauche), regex_analyzer(chaine_droite)]
            elif '(' in chaine_gauche:
                index_parg = string.index('(')

                # Cas où la parenthèse est en début de chaine.
                # On récupère l'indice de la bonne parenthèse ')'
                if index_parg == 0:
                    # Idée : renverser la chaine de caractère avec [::-1]
                    # On récupère l'indice du premier ')' rencontré
                    # on soustrait la longueur de la chaine 'string' par
                    # l'indice trouvé - 1 (pour que ça corresponde vraiment au
                    # bon indice)
                    string_tmp = string[::-1]
                    index_pard = string_tmp.index(')')
                    index_pard = len(string) - index_pard - 1

                    # Gestion d'erreur (bientot)
                    #if index_pard + 1 < len(string):
                    #    if string[index_pard + 1] != '*':
                    #        return "* non présent après )"
                    #    else:
                    #        return "* non présent après )"

                    chaine_entre_par = string[index_parg + 1:index_pard]

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

                # Cas où il y a quelquechose avant '('
                # Forcément une chaine de caractère
                else:
                    return ['.', regex_analyzer(string[:index_parg]), regex_analyzer(string[index_parg:])]

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
    string = "(a+(a+b)*)*"
    string = "toto(a+b)*"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)

if __name__ == '__main__':
    main()
