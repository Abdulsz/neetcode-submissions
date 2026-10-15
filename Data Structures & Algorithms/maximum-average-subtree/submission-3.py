# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        maxAve = 0
        def dfs(node):
            nonlocal maxAve

            if not node:
                return (0,0)

            leftCnt,leftSum = dfs(node.left)
            rightCnt,rightSum = dfs(node.right)

            cnt = 1+leftCnt+rightCnt
            sums = node.val+leftSum+rightSum

            ave = sums/cnt
            maxAve = max(maxAve,ave)

            return (cnt,sums)

        dfs(root)
        return maxAve

