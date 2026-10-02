class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n + 1)]
        visited = set()

        def dfs(node, parent):
            if node == parent:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                if dfs(neighbor, parent):
                    return True

            return False

        for a, b in edges:
            visited.clear()

            if dfs(a, b):
                return [a, b]

            graph[a].append(b)
            graph[b].append(a)

        return []
            
        
        
            


        