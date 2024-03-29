# https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

# Let's try to understand this with an example.

# You are given an immutable string, and you want to make changes to it.

# Example

# >>> string = "abracadabra"

# You can access an index by:

# >>> print string[5]
# a

# What if you would like to assign a value?

# >>> string[5] = 'k' 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

# How would you approach this?

#     One solution is to convert the string to a list and then change the value.

# Example

# >>> string = "abracadabra"
# >>> l = list(string)
# >>> l[5] = 'k'
# >>> string = ''.join(l)
# >>> print string
# abrackdabra

#     Another approach is to slice the string and join it back.

# Example

# >>> string = string[:5] + "k" + string[6:]
# >>> print string
# abrackdabra

def mutate_string(string, position, character):
    # word = list(string)
    # print(word)
    return string[:position] + character + string[position + 1:]

        # steps:
        # conv input string to an array --> that's only applicable if you want to use the replace method to add the new char to the array
        # Otherwise, can simply use the slice method for it.
        # use slices to get the string from beginning up to int (bc slice is exclusive)
        # add the char w position
        # print the rest of the string
if __name__ == '__main__':
