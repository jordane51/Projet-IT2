import automaton

def main():
    # ( a+b*a )*
    test1 = ["*", ["+", ["a", [".", ["*","b"], ["a"]]]]]

    # ( a+b+c )
    test2 = ["+", ["+",["a", "b"]], ["c"]

if __name__ == '__main__':
    main()