class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #using dfs
        if not grid:
            return 0 
        m,n = len(grid), len(grid[0])

        visited = set()

        maxArea = 0

        def dfs(i,j):
            if (i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (i,j) in visited):
                return 0 
            visited.add((i,j))

            area = 1



            area += dfs(i - 1,j)
            area += dfs(i + 1,j)
            area += dfs(i, j - 1)
            area += dfs(i, j + 1)

            return area
        
        for i in range(m):
            for j in range(n):
               maxArea = max(maxArea, dfs(i,j))
        
        return maxArea
        


    
        