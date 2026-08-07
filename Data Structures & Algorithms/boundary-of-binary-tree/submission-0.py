# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        def is_leaf(node):
            return node and not node.left and not node.right

        res = []

        if not is_leaf(root):
            res.append(root.val)

        curr = root.left
        while curr:
            if not is_leaf(curr):
                res.append(curr.val)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        
        def get_leaves(node):
            if not node:
                return

            if is_leaf(node):
                res.append(node.val)
                return

            get_leaves(node.left)
            get_leaves(node.right)
        
        get_leaves(root)

        right = []
        curr = root.right
        while curr:

            if not is_leaf(curr):
                right.append(curr.val)
            
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        
        res.extend(reversed(right))
        return res
        
        

