"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #use bfs for exploring graph 
        if not node:
            return None
        
        visited = {} # create
        queue = deque([node])

        #clone starting node
        visited[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:

                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                #connect cloned nodes

                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]

        