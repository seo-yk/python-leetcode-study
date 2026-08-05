# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        path = []
        
        if not root:
            return ans

        def sum(root, cur):

            cur_node = root

            if not cur_node:
                return

            path.append(cur_node.val)
            cur += cur_node.val

            if cur == targetSum and not cur_node.left and not cur_node.right:
                ans.append(path[:])

            sum(cur_node.left, cur)
            sum(cur_node.right, cur)

            path.pop()

            return ans

        return sum(root, 0)