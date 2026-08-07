# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    cnt = 0
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
    
        def dfs(node):
            
            if not node:
                return True

            left = dfs(node.left)
            right = dfs(node.right)

            if not left or not right:
                return False

            if node.left and node.left.val != node.val or node.right and node.right.val != node.val:
                return False
             
            self.cnt+=1
            return True

            
        dfs(root)
        return self.cnt

            
            

            