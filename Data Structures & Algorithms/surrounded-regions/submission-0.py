
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(m, n):
            if (
                m < 0 or m >= rows or
                n < 0 or n >= cols or
                board[m][n] != "O"
            ):
                return

            # Mark this O as connected to the border
            board[m][n] = "T"

            # Recursive calls
            dfs(m + 1, n)
            dfs(m - 1, n)
            dfs(m, n + 1)
            dfs(m, n - 1)

        # Check left and right borders
        for m in range(rows):
            dfs(m, 0)
            dfs(m, cols - 1)

        # Check top and bottom borders
        for n in range(cols):
            dfs(0, n)
            dfs(rows - 1, n)

        # Flip surrounded O cells and restore border-connected cells
        for m in range(rows):
            for n in range(cols):
                if board[m][n] == "O":
                    board[m][n] = "X"
                elif board[m][n] == "T":
                    board[m][n] = "O"

        
        