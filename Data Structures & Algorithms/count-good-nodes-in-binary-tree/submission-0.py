# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = deque([(root,root.val)]) # store tuples

        while queue:
            node, max_val = queue.popleft()
            if node.val >= max_val:
                res += 1
            max_val = max(max_val,node.val)
            #add children with max value at both subtrees
            if node.left:
               
                queue.append((node.left,max_val))
                
            if node.right:
                queue.append((node.right,max_val))
            



        return res
        