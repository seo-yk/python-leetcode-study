# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        
        if not root1 or not root2:
            return False

        list1 = []
        list2 = []
        
        def dfs(root, list):
            if root:
                if not root.left and not root.right:
                    return list.append(root.val)
            
                dfs(root.left, list)
                dfs(root.right, list)

        dfs(root1, list1)
        dfs(root2, list2)
        
        return list1 == list2
            


            