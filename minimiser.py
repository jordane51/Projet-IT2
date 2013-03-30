#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import automaton
from determiniser import *
from mirror import mirror


def minimiser(aut):
    return determiniser(mirror(determiniser(mirror(aut))))


def main():
    automate = automaton.automaton(
        epsilons = [],
        states=['E','a1','a2','a3','a4','a5','b1','b2','b3','b4','b5'],initials=['E'],finals=['a3','b2','b5','a5'],
        transitions=[('E','a','a1'),('a1','a','a1'),('a1','a','a2'),('a1','b','b1'),('b1','b','b1'),('a2','b','b2'),('b1','a','a1'),('b1','a','a2'),('a2','a','a3'),('E','b','b1'),('E','a','a2'),('E','b','b4'),('E','b','b3'),('E','a','a4'),('a4','a','a4'),('a4','b','b3'),('b3','b','b3'),('b3','a','a4'),('b3','b','b4'),('a4','b','b4'),('b4','b','b5'),('b4','a','a5')])
    automate.display(title="Automate",wait=False)
    minimiser(automate).display(title="Minimise",wait=False)


if __name__ == '__main__':
    main()
