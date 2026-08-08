# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        stack1 = []
        stack2 = []

        while True:

            while root1:
                stack1.append(root1)
                root1 = root1.left

            while root2:
                stack2.append(root2)
                root2 = root2.right

            if not stack1 or not stack2:
                break

            top1,top2 = stack1[-1],stack2[-1]
            sums = top1.val+top2.val

            if sums == target:
                return True

            if sums<target:
                root1 = stack1.pop().right

            else:
                root2 = stack2.pop().left

        
        return False


            