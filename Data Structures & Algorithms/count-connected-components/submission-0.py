class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0 
        visited = set()
        graph = [[] for _ in range(n)] # adjacency list

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
                   




        return res 
        