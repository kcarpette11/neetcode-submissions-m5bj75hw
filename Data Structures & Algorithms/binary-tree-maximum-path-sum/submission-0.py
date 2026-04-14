# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
 
   def maxPathSum(self, root: Optional[TreeNode]) -> int:
    # do postorder traversal (left->right->node)
    self.max_sum = float('-inf')
    
    def postorder_traversal(node):
        if not node:
            return 0
        
        # Remove max() - just get the values
        left_max = postorder_traversal(node.left)
        right_max = postorder_traversal(node.right)
        
        # Calculate the full path sum with current node as root
        current_path_sum = node.val + left_max + right_max
        
        # Update global maximum
        self.max_sum = max(self.max_sum, current_path_sum)
        
        # Return the max path sum that can be extended upward
        # Use max(0, ...) and only one branch
        return max(0, node.val + max(left_max, right_max))
    
    # Actually call the function
    postorder_traversal(root)
    return self.max_sum