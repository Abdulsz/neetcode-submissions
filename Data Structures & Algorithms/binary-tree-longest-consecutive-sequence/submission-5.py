# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        maxSeq = 0
        def dfs(node,prev,sums):
            nonlocal maxSeq

            if not node:
                return 

            if node.val -1 == prev:
                sums+=1
            else:
                sums = 1

            maxSeq = max(maxSeq,sums)
            dfs(node.left,node.val,sums)
            dfs(node.right,node.val,sums)
        dfs(root,-1,1)
        return maxSeq



            