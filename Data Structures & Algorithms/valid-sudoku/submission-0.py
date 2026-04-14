class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]  # 9 rows
        cols = [set() for _ in range(9)]  # 9 columns
        squares = [set() for _ in range(9)]  # 9 squares
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                num = int(board[i][j])
                sq_index = (i // 3) * 3 + (j // 3)
                
                if (num in rows[i] or num in cols[j] or num in squares[sq_index]):
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                squares[sq_index].add(num)
        
        return True




        








































































