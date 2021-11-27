'''
Under each group, it can be for interget or strings, the code is lightly modify based on the input.

Combinations: appliable for selection and subset Qs,--> include/ exclude
    it can be subdivided into 2 methods:
        1.) repetitions
            ie. [1, 3, 7, 9] with only 2 elements and order doesn't matter (1, 3) <=> (3, 1)
                ans = (1, 1), (1, 3), (1, 7), (1, 9), (3,3), (3, 7), (3, 9), etc.
                Total # of possibility is 4 for the 1st position and 4 for the 2nd position => n**2

        2.) Non-repetitions
            ie. [1, 3, 7, 9] with only 2 elements and order doesn't matter (1, 3) <=> (3, 1)
                ans = (1, 3), (1, 7), (1, 9), (3, 7), (3, 9), etc.
                Total # of possibility is 4 for the 1st position and 3 for the 2nd position => n(n-1)

Permutations: appliable for order/ arrangement and generate all output, aka fill in the blanks
    it can be subdivided into 2 methods: 
        1.) repetitions
            (order doesn't matter --> [1, 2, 3, 4] <=> [4, 3, 2, 1])
            ie. _, _, _, _ with [1, 2, 3, 4]
                ans = [1, 1, 1, 1], [1, 1, 2, 4] --> # of possibility is 4!, 4!, 4!, 4!.
                In total, # of possiblity is n for each of the position => n ** n

        2.) Non-repetitions
            ie. _, _, _, _ with [1, 2, 3, 4]
                ans = [1, 2, 3, 4], [2, 1, 4, 3] --> # of possibility is 4! --> 4* (4-1)* (4-2)* (4-3)

BFS and DFS are just methods that can find all the possible answers.
Runtime for both methods:
    O(2**n)n

Space:
for BFS: O(2**n)
for DFS: O(n)

In general, DFS works best!


'''