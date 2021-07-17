# Given two lists. concatenate them (that is, combine them into a single list).

# For example, given [1, 2] and [3, 4]:

# >>> concat_lists([1, 2], [3, 4])
# [1, 2, 3, 4]

# It should work if either list is empty:

# >>> concat_lists([], [1, 2])
# [1, 2]

# >>> concat_lists([1, 2], [])
# [1, 2]

# >>> concat_lists([], [])
# []

# We’ve included a file, concatlists.py, with a function, concat_lists:

# def concat_lists(list1, list2):
#     """Combine lists."""

# However, this function is unimplemented.

# Runtime:O(n^2)--> should be DRY!
def concat_lists(list1, list2):
    results = []
    for item in list1:
        if type(list1)==list:
            results.append(item)
    for item2 in list2:
        if type(list2)==list:
            results.append(item2)
    print(results)