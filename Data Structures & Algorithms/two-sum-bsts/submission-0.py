# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        set1 = set()
        set2 = set()

        def dfs(node,first):
            if not node:
                return None

            if first:
                set1.add(node.val)
            else:
                set2.add(node.val)


            dfs(node.left,first)
            dfs(node.right,first)

        dfs(root1,True)
        dfs(root2,False)

        for num in set1:
            
            if target-num in set2:
                return True

        return False
        