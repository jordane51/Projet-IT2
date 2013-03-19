# -*- coding: UTF-8 -*-

import automaton

def new_finals_states(aut1, aut2, aut_res, inter=True):
	""" Determine the new finals states for intersection or union operation between two automates """
	for state in aut_res.get_states():
		if state not in aut_res.get_final_states(): 
			if inter:
				if aut1.state_is_final(state[0]) and aut2.state_is_final(state[1]):
					aut_res.add_final_state((state[0], state[1]))
			else:
				if aut1.state_is_final(state[0]) or aut2.state_is_final(state[1]):
					aut_res.add_final_state((state[0], state[1]))


def intersection(aut1, aut2):
	"""Returns the intersection of aut1 and aut2"""
	aut_res = automaton.automaton()

	alphabet_res = aut1.get_alphabet().intersection(aut2.get_alphabet())
	stack = []

	print("initialisation à partir des états initiaux")
	for init_aut1 in aut1.get_initial_states():
		for init_aut2 in aut2.get_initial_states():
			init_state_res = (init_aut1, init_aut2)

			aut_res.add_initial_state(init_state_res)
			aut_res.add_state(init_state_res)

			stack += [init_state_res]

	while len(stack) > 0:
		print(stack)
		#current state
		state = stack.pop()

		for letter in alphabet_res:
			# Evite les liaisons inutiles sur un etat sur lui même.
			if not letter in aut1.get_epsilons():
				access_aut1 = list(aut1.delta(letter, [state[0]]))
				access_aut2 = list(aut2.delta(letter, [state[1]]))

				for al in access_aut1:
					for ar in access_aut2:
						new_state = (al, ar)

						# Nouvel etat à gerer (et toutes les transitions ...)
						if not aut_res.has_state(new_state):
							stack += [new_state]
							aut_res.add_state(new_state)

						aut_res.add_transition(((state[0], state[1]), letter, new_state))
				
		#stack.pop()

	new_finals_states(aut1, aut2, aut_res, inter=True)

	return aut_res

#youri's code
def A():
	return automaton.automaton( ['a','b'], '0', [1,2,3,4,5], [1], [3,5],[(1,'a',2), (1, 'b', 3), (2, 'a', 3), (2, 'b', 4), (3, 'a', 4), (3, 'b', 5), (4, 'a', 5), (4, 'b', 1), (5, 'a', 2), (5, 'b', 3)] )


def main():
	toto = intersection(A(), A())
	toto.display()
	A().display()

if __name__ == '__main__':
	main()
