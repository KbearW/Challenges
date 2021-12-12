# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

"""


4 queen problems.
================

1...
.2..
....
....

1
2


12..
....
....
....


.1..
...2
3...
..4.


rule:
1) not in the same row (ok)
2) not in the same col
    col_set.add(col)
    if col in col_set:
       continue
    ....
    
3) not in the same diag  

            (y = -x + b) ==> x + y = b

       r  c    ==> r+c = 3 (b)
0001  (0, 3)  Q
0010  (1, 2)  ..
0100  (2, 1)  ..
1000  (3, 0)  ..


y = -x + b
line {x1, x2, x3) : slope = -1
line {k1,k2,k3,k4} : slope = -1    
00xk    0+2 = 2  ;  0+3 = 3  (b is different :  x and k are not in the same line.
0xk0
xk00
k000

Q1 at (0, 3)   diag_set.add(0+3)

Q2  is (1,2) ok ?   1+2 = 3    = (0+3)

     if 1+2 in diag_set:
        contiue
        
     diag_set.find(3) :  can not place a new Q at location (1,2)

(3,0)  is in the same line as (0,3) 

      diag_set.add(r+c)
      
      if r+c in diag_set:
          continue 


4) not in the same anti-diag (y = x + b)


1000   0 0     r - c = 0  
0100   1 1
0010   2 2
0001   3 3   

1000   0 0    
2100   1 1   1 0
0210   2 2   2 1
0021   3 3   3 2     r-c=1

    anti_diag_set.add(r-c)
    
    if r-c in anti_diag_set:
            continue
            

4 queens:

1 => row 1
    for each col
        ...
2 => row 2
3 => row 3
4 => row 4


1 ==> row=0: (0,0)  (0, 1)   (0, 2)  (0, 3) ....no solution



# sorting....


[2,4,5,1,2,3] random inputs.

sort them in the following rule

  a <= b >= c <= d
  
  {a, b,c,d.....}


wig sort order.: up down, up down....


O(N) .....
 i ..j .......................
 
 1 2 3 4
 1 3 2 4

 0 1 2 3 (index) 
 i: even
  arr[0] <= arr[1] 
                 i: odd
                 arr[1] >= arr[2]
                 
 4 3 2 1
 3 4 2 1
 3 4 1 2 (stop)
 
 
"""
def wig_sort(a):
    for i in range(len(a)-1):
        print (i)
        if i % 2 == 1: #odd
            print("odd", i)
            if a[i]< a[i+1]:
                #swap
                a[i], a[i+1] = a[i+1], a[i]
                print(a)
        else:  # even   required: goal: ==> arr[0] <= arr[1]
            print("even", i)
            if a[i] > a[i+1]:
                # swap
                a[i], a[i+1] = a[i+1], a[i]
                print(a)
    return a
# print(wig_sort([4,3,2,1]))
  
"""    
    "()()"
    return true if valid
"()()()())(" false
"((()))" --> True
'(()('


p1 p2 p3.................=> string "

DNA:   ATCGATCG.......................
       CG.............................
A->C
T->G


"""

def balance(s):
    
    count_open = 0
    for char in s:
        if char == '(':
            count_open += 1
        else:
            if count_open > 0:
                count_open-=1
            else:  
                return False
                
    return (count_open == 0)
    
arr=['()', ')(', '()()', '(())', '(()(', '()())', '((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))']
for s in arr:
    print(s, balance(s))



      
"""

O(N!)......


class Solution:
    def solveNQueens(self, n):
        # Making use of a helper function to get the
        # solutions in the correct output format
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board
        
        def backtrack(row, diagonals, anti_diagonals, cols, state):
            # Base case - N queens have been placed
            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col
                # If the queen is not placeable
                if (col in cols 
                      or curr_diagonal in diagonals 
                      or curr_anti_diagonal in anti_diagonals):
                    continue

                # "Add" the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                state[row][col] = "Q"

                # Move on to the next row with the updated board state
                backtrack(row + 1, diagonals, anti_diagonals, cols, state)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                state[row][col] = "."

        ans = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans
    
"""  