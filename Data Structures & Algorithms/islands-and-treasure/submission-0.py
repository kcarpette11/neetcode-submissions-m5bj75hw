from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        visited = set()
        INF = 2147483647 # for land cell 
        directions = [(1,0), (-1,0), (0,1),(0,-1)]
        res = []

        row, col = len(grid), len(grid[0])
        queue = deque()

        # use BFS to visit all connected cells
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
     
        while queue:
            i,j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj 
               
                if not (0 <= ni < row and 0 <= nj < col):
                    continue
                if ((ni,nj)) in visited:
                    continue
                    
                if grid[ni][nj] == -1:
                    continue
                grid[ni][nj] = grid[i][j] + 1
                visited.add((ni,nj))
                queue.append((ni,nj)) #process the cell
        