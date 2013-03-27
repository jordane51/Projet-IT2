import automaton
from determiniser import isDeterministe
from determiniser import determiniser
from mirror import mirror

def minimiser(aut):
    aut2 = aut
    #avant de commencer, on le déterminise si nécessaire
    if not isDeterministe(aut):
        aut2 = determiniser(aut)
    return determiniser(mirror(determiniser(mirror(aut2))))

def main():
    automate = automaton.automaton(
        epsilons=[],
        states=[0, 1], initials=[0], finals=[1],
        transitions=[(0, 'a', 1), (1, 'b', 0)])
    minimiser(automate).display()


if __name__ == '__main__':
    main()