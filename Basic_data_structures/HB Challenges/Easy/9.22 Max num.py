# https://fellowship.hackbrightacademy.com/materials/challenges/max-num/index.html#max-num


# edge case: neg? 
# sorted()
# max()
def max_num(num_list):
    '''find the largest int in a list of int'''
    num_list = sorted(num_list)
    return num_list[-1]

num_list = [5,3,6,2,1]
print(max_num(num_list))

# runtime: sorted()  = binary sort --> O(n log (n)) bc it goes by the midpoint and insert to the left/ right of the midpoint.
# Memory: O(1)