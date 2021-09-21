# https://fellowship.hackbrightacademy.com/materials/challenges/fizzbuzz/index.html#fizzbuzz

# Goal: div by 3 --> fizz, div by 5 --> buzz, div by 3 and 5 --> buzzfizz

# input: range 1-20
# def a function
# 4 statments:
# div by 3 --> fizz
# div by 5 --> buzz
# div by 3 and 5 --> fizzbuzz
# else return num

def fizzbuzz():
    nums = [x for x in range(1,21)]
    for num in nums:
        if num % 15 == 0:
            print('fizzbuzz')
        if num % 3 == 0:
            print('fizz')
        if num % 5 == 0:
            print('buzz')
        else:
            print(num)

print(fizzbuzz())