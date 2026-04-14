# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([(root,float("-inf"),float("inf"))])

        while queue:
            node,left_sub,right_sub = queue.popleft()
            if not (left_sub < node.val < right_sub): # if it violates BST property
                return False

            if node.left:
                queue.append((node.left,left_sub,node.val))
            if node.right:
                queue.append((node.right,node.val,right_sub))
        return True
         
        
        