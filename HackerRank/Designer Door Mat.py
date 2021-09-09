# https://www.hackerrank.com/challenges/designer-door-mat/problem

# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

#     Mat size must be 

# X. ( is an odd natural number, and is times

#     .)
#     The design should have 'WELCOME' written in the center.
#     The design pattern should only use |, . and - characters.

# Sample Designs

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------

# Input Format

# A single line containing the space separated values of
# and

# .

# Constraints

# Output Format

# Output the design pattern.

# Method #1:
n, m = input().split()
for i in range(1, (int(n)//2)+1):
    pattern = '.|.'*(i+i-1) 
    print(pattern.center(int(m),'-'))
print('WELCOME'.center(int(m),'-'))
for i in range(1,(int(n)//2)+1)[::-1]:
    pattern = '.|.'*(i+i-1 ) 
    print(pattern.center(int(m),'-'))

# Method #2:
n, m = input().split()
Top = []
for i in range(1, (int(n)//2)+1):
    pattern = '.|.'*(i+i-1)
    Top.append(pattern.center(int(m),'-'))
print('\n'.join(Top))
print('WELCOME'.center(int(m),'-'))
print('\n'.join(Top)[::-1])