# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #using bfs traversal
        if not root:
            return "N"
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if not node: # for null placeholders
                res.append("N")
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res) 

        


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]: 
        vals = data.split(",")
        queue = deque([root])
        res = []
        if vals[0] == "N":
            return None 
        
        v = len(vals)
        index = 1 
        while queue and index < v :
            node = queue.popleft()
            if index < v and vals[index] != "N": # create left child if exists and not null
               node.left = TreeNode(int(vals[index]))
               queue.append(node.left)
            index += 1
            if  index < v and vals[index] != "N":
                 node.right = TreeNode(int(vals[index]))
                 queue.append(node.right)
               
            index += 1
        return root
