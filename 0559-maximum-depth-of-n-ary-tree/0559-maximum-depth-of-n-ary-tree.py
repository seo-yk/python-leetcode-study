"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        if len(root.children) == 0:
            return 1
        
        max_depth = 0
        def find_depth(node, depth):
            nonlocal max_depth
            if node:
                for n in node:
                    find_depth(n.children, depth+1)
            else:
                max_depth = max(max_depth, depth)
                return

        find_depth(root.children, 1)
        return max_depth