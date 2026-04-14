from typing import List 
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]: 
        res = []
        cols = set() # for checking for columns
        # '.' indicates an empty space
        board = [["."] * n for _ in range(n)]
        diag1, diag2 = set(), set() #initialize diagonals

        def backtrack(r):
            if r == n: # add copy to result if the index is equal to n
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r+c) in diag1 or (r-c) in diag2:
                    continue
                # adding the queen
                cols.add(c)
                diag1.add(r + c)
                diag2.add(r - c)
                board[r][c] = "Q" # indicator for queen 

                backtrack(r + 1)
                #for removing the queen 
                cols.remove(c)
                diag1.remove(r + c)
                diag2.remove(r - c)
                board[r][c] = "." # indicate empty space






        backtrack(0)
        return res
        