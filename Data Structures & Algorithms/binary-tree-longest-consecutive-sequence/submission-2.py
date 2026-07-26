# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxPath = 0
        def dfs(node):

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            curr = 1

            if node.left and node.left.val-node.val ==1:
                curr = max(curr,left+1)

            if node.right and node.right.val - node.val == 1:
                curr = max(curr,right+1)

            self.maxPath = max(self.maxPath,curr)

            return curr

        dfs(root)
        return self.maxPath
            
