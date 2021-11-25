import itertools
letter = 'ABCD'

# This includes all possible pairs
A = list(itertools.product(letter, repeat = 2))
print(f'product is {len(A)} and {A}')

# This removes dups - ie. (A,A), (B,B), (C,C), (D,D)
B = list(itertools.permutations(letter, 2)) 
print(f'permutations is  {len(B)} and {B}')

# This removes all dups and order doesn't matter - ie. (A,A)... and (A,B)/(B,A) pair
C = list(itertools.combinations(letter,2))
print(f'combinations is  {len(C)} and {C}')

# This includes all dups and order doesn't matter.
D = list(itertools.combinations_with_replacement(letter,2))
print(f'combinations_w_replacement is  {len(D)} and {D}')

# product is 16 and [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), 
                    # ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), 
                    # ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'), 
                    # ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D')]

# permutations is  12 and [('A', 'B'), ('A', 'C'), ('A', 'D'), 
                        # ('B', 'A'), ('B', 'C'), ('B', 'D'), 
                        # ('C', 'A'), ('C', 'B'), ('C', 'D'), 
                        # ('D', 'A'), ('D', 'B'), ('D', 'C')]

# combinations is  6 and [('A', 'B'), ('A', 'C'), ('A', 'D'), 
                        # ('B', 'C'), ('B', 'D'), 
                        # ('C', 'D')]

# combinations_w_replacement is  10 and [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), 
                                        # ('B', 'B'), ('B', 'C'), ('B', 'D'), 
                                        # ('C', 'C'), ('C', 'D'), 
                                        # ('D', 'D')]