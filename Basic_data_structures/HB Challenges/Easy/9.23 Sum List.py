# https://fellowship.hackbrightacademy.com/materials/challenges/sum-list/index.html#sum-list

# goal: sum the list of num
def sum_list(num_list):

    # Method #1- builtin method
    # return sum(num_list)

    # Method #2
    total = 0
    for num in num_list:
        total += num
    return total

num_list = [5,3,6,2,1]
print(sum_list(num_list))