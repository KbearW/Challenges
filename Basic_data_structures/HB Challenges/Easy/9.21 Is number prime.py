# https://fellowship.hackbrightacademy.com/materials/challenges/is-prime/index.html#is-prime

# goal: if prime--> True, else--> False
# edge: if less than or equ to 1 --> False
import math

def is_prime(num):
    '''if num is prime, return True, else False'''
    if num <= 1:
        return False

    # Method #1
    # for n in range(2,num):
    #     if num % n == 0:
    #         return False
    # return True

    # Method #2
    '''this method is faster bc the begining of the factorization and ending of it will be div by the sqrt
    of the num, therefore, the run time of this is log(n) w base 2.'''
    # max_divisor = math.floor(math.sqrt(num))
    # for n in range(2, max_divisor + 1):
    #     if num % n == 0:
    #         return False
    # return True

    # Method #3
    '''this method will elimate all the even num that's greater than 2 to cutdown on runtime--> log(n/2)'''
    max_divisor = math.floor(math.sqrt(num))
    for n in range(2, max_divisor + 1, 2):  # the last elem of the range function is 'step', how many # to skip over
        if num % n == 0:
            return False
    return True

num = 4
print(is_prime(num))