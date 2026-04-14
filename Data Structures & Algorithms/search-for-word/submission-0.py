class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        visited = set()
        w = len(word)
          
       

        def backtrack(row,col,i):
            if i == w: # if word lengths match 
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False # if it's out of bounds
            if (row,col) in visited or board[row][col] != word[i]:
                return False # if it's used or mismatch
            visited.add((row,col))

            #explore neighbors
            res = (backtrack(row + 1,col, i + 1) or backtrack(row - 1,col, i + 1) or backtrack(row ,col + 1, i + 1) or backtrack(row ,col - 1, i + 1)  )
            visited.remove((row,col)) # remove from set
            return res

        # try every starting cell
        for row in range(rows):
            for col in range(cols):
                if backtrack(row,col,0):
                    return True
            
        return False