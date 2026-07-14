# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # 사이클이 있는지 없는지 판단할 것
        visited = set()
        cur = head

        while cur:
            if cur in visited:
                return True

            visited.add(cur)
            cur = cur.next
            
        return False