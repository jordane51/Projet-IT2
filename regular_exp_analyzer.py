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

                    chaine_entre_par = string[index_parg + 1:index_pard]
                    # Cas où il n'y a pas d'étoile après la parenthèse
                    # Il faut concatener 4 cas :
                    # (ui) 1
                    # ui(ui) 2
                    # (ui)ui 3
                    # ui(ui)ui 4
                    if index_pard + 1 > len(string) - 1:
                        # Cas 1
                        return regex_analyzer(chaine_entre_par)

                    if string[index_pard + 1] != '*':
                        if string[:index_parg] != '':
                            if string[index_pard:] != ')':
                                # Cas 4
                                return ['.', regex_analyzer(string[:index_parg]), ['.', regex_analyzer(chaine_entre_par), regex_analyzer(string[index_pard:])]]
                            else:
                                # Cas 2
                                return ['.', regex_analyzer(string[:index_parg]), regex_analyzer(chaine_entre_par)]
                        elif string[:index_parg] == '':
                            if string[index_pard + 1:] != '':
                                # Cas 3
                                return ['.', regex_analyzer(chaine_entre_par), regex_analyzer(string[index_pard:])]

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

        else:
            return ['+', [chaine_gauche], regex_analyzer(chaine_droite)]

    # Fonction concatener pour des chaines de caractères sans autres opérateurs
    return concatener(string)


def concatener(string):
    # Gere uniquement une chaine de caractere de type : "abjkzhfdskjh"
    # Cas particuliers pour des chaines de longueur 1 ou 2 exactement.
    if len(string) == 1:
        return list(string)
    elif len(string) == 2:
        if string[1] != '*':
            return ['.', [string[0]], [string[1]]]
        else:
            return ['*', [string[0]]]

    list_res = []
    list_string = list(string)

    list_res += ['.']
    while(list_string != []):
        if len(list_string) != 1:
            a = list_string.pop(0)
            b = list_string.pop(0)
            if b != '*':
                list_res += [['.', [b], [a]]]
            else:
                list_res += [['*', [a]]]
            continue
        list_res += [[list_string.pop()]]

    return list_res


def main():
    print("-----------------")
    string = "a"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)

    print("-----------------")
    string = "ab"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)

    print("-----------------")
    string = "a+b"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)

    print("-----------------")
    string = "a*"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)

    print("-----------------")
    string = "(a+b)*"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)

    print("-----------------")
    string = "a*b"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)

    print("-----------------")
    string = "(a+b+c)"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)

    print("-----------------")
    string = "a*(a*+b*a)"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)

    print("-----------------")
    string = "a+b*"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)

    print("-----------------")
    string = "a+b+(k*+b)*"
    print(string)
    list_res = regex_analyzer(string)
    print(list_res)


if __name__ == '__main__':
    main()
