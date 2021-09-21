# https://fellowship.hackbrightacademy.com/materials/challenges/concat-lists/index.html#concat-lists


# Goal: Given two lists, Concatenate into one single list

# def a function
# look at the samples
# figure out how it works
# figure out what function should be used  --> .extend()
# look at the edge cases

def concat_lists(list1, list2):
    '''concatenate two lists into one'''
    
    # solution #1: time--> O(k), where k is the length of list that need to be added
    list1.extend(list2)
    return list1

    # solution #2:  time--> O(1)
    # for num in list2:
    #     list1.append(num)
    # return list1



list1 = [1,2]
list2 = [3,4]
print(concat_lists(list1, list2))

# Notes: .extend will only takes one agr and can do return statement