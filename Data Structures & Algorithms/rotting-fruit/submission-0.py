from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m,n = len(grid), len(grid[0])
        queue = deque()

        empty = 0
        fresh, rotten = 1,2
        fresh_count = 0 # count of fresh oranges 

        directions = [(-1,0), (1,0), (0,-1), (0,1)]# enqueue neighbors
        # adding rotten oranges and count fresh oranfes
        for i in range(m):
            for j in range(n):
                if grid[i][j] == rotten:
                    queue.append((i,j))
                elif grid[i][j] == fresh:
                    fresh_count +=1

        minutes = 0 # for counting minutes

        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                i,j = queue.popleft()

                for di, dj in directions:
                    new_i = i + di
                    new_j = j + dj

                    if (0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == fresh):
                        grid[new_i][new_j] = rotten
                        fresh_count -= 1
                        queue.append((new_i,new_j))
            minutes += 1 # update minutes

        if fresh_count > 0:
            return -1
            

        return minutes               

        



        

        