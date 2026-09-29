class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = set() # to check for visited nodes
        res = []
        graph = [[] for _ in range(n)]

        #setting up adjacency list
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def explore(node,parent):
            if node in visited:
                return False # for finding cycles
            visited.add(node)
            res.append(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue # skip node
                
                if not explore(neighbor, node):
                    return False
            
            return True # if no cycles were found


                
        
        # explore(0,-1) checks for cycles and len(res) == 0 checks every node that was reached
        return explore(0,-1) and len(res) == n


        