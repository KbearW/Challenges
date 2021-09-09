# https://www.hackerrank.com/challenges/python-tuples/problem

# Task
# Given an integer, , and space-separated integers as input, create a tuple, , of those integers. Then compute and print the result of

# .

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Input Format

# The first line contains an integer,
# , denoting the number of elements in the tuple.
# The second line contains space-separated integers describing the elements in tuple

# .

# Output Format

# Print the result of

# .

# Sample Input 0

# 2
# 1 2

# Sample Output 0

# 3713081631934410656

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # print(n, integer_list)
    list1 = [i for i in range(1, n+1)]
    T= tuple(list1)
    print(hash(T))
#  (as a list is not hashable, but a tuple is)