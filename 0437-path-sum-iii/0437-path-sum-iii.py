# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        path_sum = {0:1}
        
        def dfs(root, sum):
            if not root:
                return 0
            
            sum += root.val
            count = path_sum.get(sum-targetSum, 0)
            path_sum[sum] = path_sum.get(sum, 0)+1

            count += dfs(root.left, sum)
            count += dfs(root.right, sum)

            path_sum[sum] -= 1

            return count
        
        return dfs(root, 0)
            


            