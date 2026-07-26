# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxPath = 0
        def dfs(node,prev):
            

            if not node:
                return 0
            
            cnt = 0
            if prev and node.val-prev.val == 1:
                cnt +=1

            
            cnt += max(dfs(node.left,node),dfs(node.right,node))
            self.maxPath = max(self.maxPath,cnt)
            return cnt

        dfs(root,None)
        return self.maxPath+1
            
