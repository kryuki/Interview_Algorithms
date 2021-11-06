'''
N_Queens problem
(ex: https://leetcode.com/problems/n-queens/
https://leetcode.com/problems/n-queens-ii/
https://www.interviewbit.com/problems/nqueens/)
'''

N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

def inRange(r, c):
    return 0 <= r < N and 0 <= c < N

def canPlace(board, r, c):
    for i in range(1, c + 1):
        if board[r][c - i]:
            return False
        if inRange(r + i, c - i) and board[r + i][c - i]:
            return False
        if inRange(r - i, c - i) and board[r - i][c - i]:
            return False
    return True

def placeQueens(board, c):
    if c == N:
        return 1
    numWaysToPlace = 0
    
    for r in range(N):
        if canPlace(board, r, c):
            board[r][c] = True
            numWaysToPlace += placeQueens(board, c + 1)
            board[r][c] = False
            
    return numWaysToPlace

print(placeQueens(board, 0))