import automaton

def expression_vers_automate(E):
    for elem in E:


def main():
    # ( a+b*a )*
    test1 = ['*', ['+', [['a'], ['.', ['*', ['b']], ['a']]]]]
    expression_vers_automate(test1)

    # ( a+b+c )
    #test2 = ["+", ["+",["a", "b"]], ["c"]

if __name__ == '__main__':
    main()
