class Solution:
    #using DFS to travers each group independently
   
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m,n = len (grid), len(grid[0])

        visited = set()

        islands = 0

   
        
        def dfs(i,j):
            if (i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0" or (i,j) in visited):
                return
            
            visited.add((i,j))
            #explore neighbors with function call

            dfs(i - 1,j)
            dfs(i + 1,j)
            dfs(i ,j - 1)
            dfs(i ,j + 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    islands += 1




        return islands  
     
    
        
            
        