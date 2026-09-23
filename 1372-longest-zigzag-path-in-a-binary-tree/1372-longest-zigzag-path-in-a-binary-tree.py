# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        
        self.max_len = 0
        def dfs(root, isLeft, step):
            if root:
                self.max_len = max(self.max_len, step)

                if isLeft:
                    dfs(root.left, False, step+1)
                    dfs(root.right, True, 1)
                else:
                    dfs(root.left, False, 1)
                    dfs(root.right, True, step+1)

        dfs(root, True, 0)
        return self.max_len