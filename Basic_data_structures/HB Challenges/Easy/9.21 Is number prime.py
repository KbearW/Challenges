# https://fellowship.hackbrightacademy.com/materials/challenges/is-prime/index.html#is-prime

# goal: if prime--> True, else--> False
# edge: if less than or equ to 1 --> False

def is_prime(num):
    # primes = [2,3,5,7,11,13,17]
    if num <= 1:
        return False
    for n in range(2,num):
        if num % n == 0:
            return False
    return True


num = 11
print(is_prime(num))