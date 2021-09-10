# https://www.hackerrank.com/challenges/python-lists/problem

# Consider a list (list = []). You can perform the following commands:

#     insert i e: Insert integer 

# at position
# .
# print: Print the list.
# remove e: Delete the first occurrence of integer
# .
# append e: Insert integer

#     at the end of the list.
#     sort: Sort the list.
#     pop: Pop the last element from the list.
#     reverse: Reverse the list.

# Initialize your list and read in the value of
# followed by lines of commands where each command will be of the

# types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Example





# : Append to the list,
# .
# : Append to the list,
# .
# : Insert at index ,
# .

#     : Print the array.
#     Output:

if __name__ == '__main__':
    N = int(input())
    lis=list()
    # print(N)
    for _ in range(N):
        s=input().strip().split(" ")
        if s[0]=="insert":
            lis.insert(int(s[1]),int(s[2]))
        if s[0]=="print":
            print(lis) 
        if s[0]=="remove":
            lis.remove(int(s[1]))
        if s[0]=="append":
            lis.append(int(s[1]))
        if s[0]=="sort":
            lis.sort()
        if s[0]=="pop":
            lis.pop()
        if s[0]=="reverse":
            lis.reverse()

