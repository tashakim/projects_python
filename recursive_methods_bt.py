# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Time complexity: O(n)
        # Space complexity: O(n) worst case - if tree is completely unbalanced
            # O(log(n)) best case - tree is completely balanced
        def bst(root):
            if not root:
                return 0
            left_subtree_depth = bst(root.left)
            right_subtree_depth = bst(root.right)
            
            return max(left_subtree_depth, right_subtree_depth) + 1
        return bst(root)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == 0 or right == 0:
                return max(left, right) + 1
            return min(left,right) + 1

        return dfs(root) 

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def height(self, node):
        if not node:
            return 0
        left_subtree_height = self.height(node.left)
        right_subtree_height = self.height(node.right)
        return max(left_subtree_height, right_subtree_height) + 1

class Solution:
    def isSymmetric(self, root):
        def dfs(left, right):
            if not left and not right:
                 return True
            if not left or not right:
                  return False

            if left.val == right.val:
                return dfs(left.left, right.right) and dfs(left.right, right.left)
            return False
        
        if not root:
            return True
        return dfs(root.left, root.right)