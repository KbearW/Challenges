board = [
    [" ", "O", "O"],
    [" ", " ", " "],
    ["X", "X", "X"],
]

#Write a function that, given a board as an argument,
#will evauluate whether either player (X or O) is in
#a winning position horizontally - three in a row
#across a row. If so, return 'X' or 'O' as appropriate,
#or None if no player is in a winning condition.

def get_row_col(input):    
    row = ord(input[0])-ord('A') 
    col = int(input[1]) -1
        
    return (row, col)

# print(get_row_col('A1'))
import collections
def winner(board):

    # for row in board:
    #     o_count = 0
    #     x_count = 0
    #     for item in range(0,3):
    #         if row[item] == 'X':
    #             x_count += 1
    #         elif row[item] == 'O':
    #             o_count += 1
    #     if o_count == 3:
    #         return 'O'
    #     elif x_count ==3:
    #         return 'X'
    # return None
    
    res = {}
#     {1:['X': 1, 'O': 3], 2:['X':1, 'O':1]} 
    for row in board:
        for cell in range(0,3): #[0,1,2]            
            item = row[cell]
            if item not in res:
                res[item] = 1
            else: #add 1 to the k/v pair
                res[item] = res[item] + 1
        # print(res)
        signs = ['X','O']
        for sign in signs:
            if res.get(sign,0) == 3:
                print(f'{sign} is the winner')
                return
        res.clear()
        
    print('No winners')
        
    print(res)
    
print(winner(board))