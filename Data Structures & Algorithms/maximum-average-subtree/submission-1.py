# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxAve = 0
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
            

            def dfs(node):

                if not node:
                    return (0,0)

                left, lcnt = dfs(node.left)
                right, rcnt = dfs(node.right)

                ave = (left+right+node.val)/(lcnt+rcnt+1)
                total = left+right+node.val

                self.maxAve = max(self.maxAve,ave)

                return (total,1+lcnt+rcnt)
            
            dfs(root)
            return self.maxAve





