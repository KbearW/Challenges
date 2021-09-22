# https://fellowship.hackbrightacademy.com/materials/challenges/max-of-three/index.html#max-of-three

def max_of_three(num1, num2, num3):
    '''takes in 3 nums as arg and returns the largest num'''
    # Method #1

    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2

    elif num3 >= num1 and num3 >= num2:
        return num3

    else:
        return 'error'
    

    # Method #2
    # numlist = [num1, num2, num3]
    # return max(numlist)

# edge cases: neg? 0? Not empty, whole num
# put in a list and sorted()
# runtime: O(n)
# space: O(1)

num1 = 1
num2 = 5
num3 = 2
print(max_of_three(num1, num2, num3))