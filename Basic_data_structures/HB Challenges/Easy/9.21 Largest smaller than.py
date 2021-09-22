# https://fellowship.hackbrightacademy.com/materials/challenges/largest-smaller-than/index.html#largest-smaller-than

# goal: return the index of the largest number in the list that's smaller than that num
# edge: pos and neg num in list, sorted, test out the first and last item first

def find_largest_smaller_than(nums, xnum):
    '''return the index of the largest number in the list that's smaller than xnum'''
    # Method #1
    # if the smallest num doesn't exist given xnum- return None, neg and pos
    # fail fast
    # if nums[0] >= xnum:
    #     return None
    # if nums[-1] < xnum:
    #     return len(nums)-1

    # # Bc the list is sorted, we can do this... Runtime is O(n)
    # for i, num in enumerate(nums):
    #     if num >= xnum:
    #         return i-1

    # Method #2
    from bisect import bisect_left

    # Fail-fast optimization: since our list is sorted, if the first number
    # is bigger, a smaller number isn't in our list
    # sorted list--> bisect library

    # bisect_left--> when item match, insert the INDEX of the left of the first exact match 
    # bisert_right --> when item match, insert the INDEX of the right of the last exact match 

    # other methods within the library: 
    # .insort_left(list, xnum) --> inserts xnum in the ordered list to the left of the match
    # .insort_rithg(list, xnum) --> inserts xnum in the ordered list to the right of the match
    # this library is good for grades... ie
    # def get_grade(score, cutoffs = [60,70,80,90], grades = 'FDCBA')
        # i = bisect.bisect_right(cutoffs, score)
        # return grades[i]

    # grades = [get_grade(score) for score in [52, 99, 77, 70, 89, 90, 100]]
    # print(grades)
    # answer: ['F', 'A', 'C', 'C', 'B', 'A', 'A']
    
    # for more info:
    # https://www.youtube.com/watch?v=pPiSMPWKZ3E

    # Runtime: O(log n)

    if nums[0] > xnum:
        return None

    # find the right most index that's smaller than xnum in sorted list
    insertion_point = bisect_left(nums, xnum)
    print(insertion_point)

    return insertion_point - 1

    if nums[insertion_point] == xnumber:
        return insertion_point - 1

    else:
        return insertion_point


nums = [-5, -2, 8, 12, 32]
xnums = [10, 33, -1, 8, -10]
for xnum in xnums:
    print(find_largest_smaller_than(nums, xnum))
