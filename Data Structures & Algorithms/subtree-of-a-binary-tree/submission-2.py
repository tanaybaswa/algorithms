# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main tree is empty, subRoot cannot be a subtree
        if not root:
            return False
        
        # If the current trees are identical, we found it!
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, check the left and right subtrees of the main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both are empty -> identical
        if not p and not q:
            return True
        # One is empty and the other isn't -> not identical
        if not p or not q:
            return False
        # Values don't match -> not identical
        if p.val != q.val:
            return False
        
        # Structurally check both left and right children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)