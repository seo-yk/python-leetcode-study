# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [(root, root.val)]
        count = 0

        while stack:
            curr, max_val = stack.pop()
            
            if curr.val >= max_val:
                count += 1
                max_val = curr.val
                
            if curr.left:
                stack.append((curr.left, max_val))
            if curr.right:
                stack.append((curr.right, max_val))

        return count