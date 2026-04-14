# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    # Do  inorder traversal (left->node->right)
   

    
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(node, result):
            if not node:
                return
            inorder_traversal(node.left, result)   
            result.append(node.val)
            inorder_traversal(node.right, result)   
        
        if not root:
            return 0
    
        result = []
        inorder_traversal(root, result)             
        return result[k-1]
            