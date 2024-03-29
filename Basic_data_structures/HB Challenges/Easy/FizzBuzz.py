https://fellowship.hackbrightacademy.com/materials/challenges/fizzbuzz/index.html#fizzbuzz

# Write a program that counts from 1 to 20 in fizzbuzz fashion.

# To do so, loop from 1 to 20 (inclusive). Each time through, if the number is evenly divisible by 3, say ‘fizz’. If the number is evenly divisible by 5, say ‘buzz’. If the number is evenly divisible by both 3 and 5, say ‘fizzbuzz’. Otherwise, say the number.

# For example:

# >>> fizzbuzz()
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizzbuzz
# 16
# 17
# fizz
# 19
# buzz

# We given you a file, fizzbuzz.py, with a method, fizzbuzz:

# def fizzbuzz():
#     """Count from 1 to 20 in fizzbuzz fashion."""

# However, this method is unimplemented.

def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion."""

# # Conditions:
#     %3--> fizz
#     %5--> buzz
#     %3 and /5--> fizzbuzz
#     from 1-20

# sudo:
# iterate over the range(1,21)
# if-elif-elif-else
# if /3 and /5 -->fizzbuzz
# if /3--> fizz
# if /5--> buzz
# else--> num

for num in range(1,21):
    if num % 3 == 0:
        if num % 5 == 0:
            print('fizzbuzz')
        else: 
            print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)