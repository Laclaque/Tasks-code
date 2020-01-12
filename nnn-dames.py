import sys

n = int(sys.argv[1])
dame0 = int(sys.argv[2])
dame1 = int(sys.argv[3])
dame2 = int(sys.argv[4])
def isSafe(board, row, col) :
    for i in range(col):  
        if (board[row][i]):  
            return False
    i = row 
    j = col 
    while i >= 0 and j >= 0: 
        if(board[i][j]): 
            return False; 
        i -= 1
        j -= 1
   
    i = row 
    j = col 
    while j >= 0 and i < n: 
        if(board[i][j]): 
            return False
        i = i + 1
        j = j - 1
    return True
    
count = 0
def solveNQUtil(board, col) : 
    global count
    if (col == n):  
        count = count + 1  
        return True
  
    res = False
    for i in range(n): 
        if (isSafe(board, i, col)):  
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0 # BACKTRACK        
    return res 

board = [[0 for j in range(n)]  
            for i in range(n)] 
board[dame0][0] = 1
board[dame1][1] = 1
board[dame2][2] = 1
solveNQUtil(board, 3)
print(count)
