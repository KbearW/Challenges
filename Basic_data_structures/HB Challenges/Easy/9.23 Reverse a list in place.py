# https://fellowship.hackbrightacademy.com/materials/challenges/rev-list-in-place/index.html#rev-list-in-place

'''goal: reverse a list in place and uses O(1) Memory only, runtime: O(n/2)'''

# swap order, try not to use the built in method

def rev_list_in_place(lst):
    '''reverse list in place, don't use reversed(), .reverse() or list slice assignment'''
    for i in range(int(len(lst) // 2)):
        # print(i+1, -(i+1))
        lst[i], lst[-(i+1)] = lst[-(i+1)], lst[i]
    return lst

lsts = [[1,2,3], [3,4,6,7], [1,2,3,4,5,6,7,8,9]]
for lst in lsts:
    print(rev_list_in_place(lst))