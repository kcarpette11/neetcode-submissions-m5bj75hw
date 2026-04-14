# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self,root):
        #calculate the height of a binary tree
        if not root:
            return 0
            #use recursion
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return max(leftHeight,rightHeight) + 1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        #calculate the diameter
        d = leftHeight + rightHeight

        #find the diameter of left and right subtrees
        left_d = self.diameterOfBinaryTree(root.left)
        right_d = self.diameterOfBinaryTree(root.right)


        return max(d, left_d, right_d)
        